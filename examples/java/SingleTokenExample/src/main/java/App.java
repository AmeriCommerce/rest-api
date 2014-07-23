import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.PropertyNamingStrategy;

import javax.net.ssl.*;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.MessageDigest;
import java.security.cert.X509Certificate;

public class App {

    private static final String STORE_DOMAIN = "<< YOUR STORE DOMAIN >>";
    private static final String ACCESS_TOKEN = "<< YOUR ACCESS TOKEN >>";

    public static void main(String[] args) throws Exception {

        // For development use only (i.e. self-signed SSLs) - do not use in production
        // installAllTrustingTrustManager();

        ObjectMapper mapper = new ObjectMapper();

        mapper.setPropertyNamingStrategy(PropertyNamingStrategy.CAMEL_CASE_TO_LOWER_CASE_WITH_UNDERSCORES);
        mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);

        URL url = new URL("https://" + STORE_DOMAIN + "/api/v1/products");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        conn.setRequestProperty("X-AC-Auth-Token", ACCESS_TOKEN);

        InputStream in = conn.getInputStream();
        ProductList list = mapper.readValue(in, ProductList.class);

        for(Product p : list.getProducts()) {
            System.out.println(p.getItemName() + ": " + p.getPrice());
        }

    }

    /* Only necessary if using a self-signed or otherwise invalid cert for development testing.
     * Insecure for production use.
     *
    private static void installAllTrustingTrustManager() throws Exception {
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
    } */

}
