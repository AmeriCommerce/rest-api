import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.PropertyNamingStrategy;

import javax.net.ssl.*;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.MessageDigest;
import java.security.cert.X509Certificate;
import java.util.Properties;

public class AmeriCommerceApi {

    private String _storeDomain;
    private int _appId;
    private String _scope;
    private String _secret;
    private ObjectMapper _objectMapper;

    final private static char[] hexArray = "0123456789abcdef".toCharArray();

    public AmeriCommerceApi() {
        Properties prop = new Properties();
        InputStream input = null;

        _objectMapper = new ObjectMapper();
        _objectMapper.setPropertyNamingStrategy(PropertyNamingStrategy.CAMEL_CASE_TO_LOWER_CASE_WITH_UNDERSCORES);
        _objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);

        try {
            input = getClass().getResourceAsStream("/demo.properties");
            prop.load(input);

            _storeDomain = prop.getProperty("storeDomain");
            _appId = Integer.parseInt(prop.getProperty("appId"));
            _scope = prop.getProperty("appScope");
            _secret = prop.getProperty("appSecret");

            // For development use only (i.e. self-signed SSLs) - do not use in production
            // installAllTrustingTrustManager();

        } catch(Exception ex) {
            ex.printStackTrace();
        } finally {
            if(input != null) {
                try {
                    input.close();
                } catch(IOException ex) {
                    ex.printStackTrace();
                }
            }
        }
    }

    public OAuthVerifyResponseModel getToken(String username, String apiKey) throws Exception {
        OAuthInitResponseModel initResponse = startNegotiation(username, apiKey);
        OAuthVerifyResponseModel verifyResponse = verify(initResponse);

        return verifyResponse;
    }

    public ProductList getProductList(String accessToken) throws Exception {
        URL url = new URL("https://" + _storeDomain + "/api/v1/products");
        HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();

        urlConnection.setRequestProperty("X-AC-Auth-Token", accessToken);

        InputStream in = urlConnection.getInputStream();

        return _objectMapper.readValue(in, ProductList.class);
    }

    private OAuthInitResponseModel startNegotiation(String username, String apiKey) throws Exception {
        String sig = createSignature(_secret, username, apiKey, _appId, _scope, _storeDomain);
        OAuthInitRequestModel tokenInitData = new OAuthInitRequestModel();

        tokenInitData.setAppId(_appId);
        tokenInitData.setScope(_scope);
        tokenInitData.setRedirectUrl(_storeDomain);
        tokenInitData.setUsername(username);
        tokenInitData.setSignature(sig);

        URL url = new URL("https://" + _storeDomain + "/api/oauth");
        HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();

        urlConnection.setRequestMethod("POST");
        urlConnection.setRequestProperty("Content-Type", "application/json");
        urlConnection.setDoOutput(true);

        OutputStream out = urlConnection.getOutputStream();
        _objectMapper.writeValue(out, tokenInitData);

        InputStream in = urlConnection.getInputStream();

        return _objectMapper.readValue(in, OAuthInitResponseModel.class);
    }

    private OAuthVerifyResponseModel verify(OAuthInitResponseModel initResponse) throws Exception {
        String sig = createSignature(_secret, initResponse.getCode(), _appId, _scope, _storeDomain);
        OAuthVerifyRequestModel verifyData = new OAuthVerifyRequestModel();

        verifyData.setAppId(_appId);
        verifyData.setAuthId(initResponse.getAuthId());
        verifyData.setSignature(sig);

        URL url = new URL("https://" + _storeDomain + "/api/oauth/access_token");
        HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();

        urlConnection.setRequestMethod("POST");
        urlConnection.setRequestProperty("Content-Type", "application/json");
        urlConnection.setDoOutput(true);

        OutputStream out = urlConnection.getOutputStream();
        _objectMapper.writeValue(out, verifyData);

        InputStream in = urlConnection.getInputStream();

        return _objectMapper.readValue(in, OAuthVerifyResponseModel.class);
    }

    private String createSignature(Object... args) throws Exception {
        String combined = joinArray("", args);
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(combined.getBytes("UTF-8"));
        return convertBytesToHex(hash);
    }

    private String joinArray(String delimiter, Object... args) {
        StringBuilder output = new StringBuilder();
        for (Object arg : args) {
            if (output.length() > 0)
                output.append(delimiter);
            output.append(arg);
        }
        return output.toString();
    }

    private String convertBytesToHex(byte[] b) {
        char[] hexResults = new char[b.length * 2];
        for(int i = 0; i < b.length; i++) {
            int x = b[i] & 0xFF;
            hexResults[i*2] = hexArray[x >>> 4];
            hexResults[i*2+1] = hexArray[x & 0x0F];
        }
        return new String(hexResults);
    }

    /* Only necessary if using a self-signed or otherwise invalid cert for development testing.
     * Insecure for production use. */
    private void installAllTrustingTrustManager() throws Exception {
        TrustManager[] trustAllCerts = new TrustManager[] {
                new X509TrustManager() {
                    public X509Certificate[] getAcceptedIssuers() {
                        return null;
                    }
                    public void checkClientTrusted(X509Certificate[] certs, String authType) {
                    }
                    public void checkServerTrusted(X509Certificate[] certs, String authType) {
                    }
                }
        };

        SSLContext sc = SSLContext.getInstance("SSL");
        sc.init(null, trustAllCerts, new java.security.SecureRandom());
        HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());

        HostnameVerifier allHostsValid = new HostnameVerifier() {
            public boolean verify(String s, SSLSession sslSession) {
                return true;
            }
        };

        HttpsURLConnection.setDefaultHostnameVerifier(allHostsValid);
    }

}
