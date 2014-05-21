import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class OAuthVerifyResponseModel {
    private String _accessToken;
    private String _refreshToken;
    private Date _expires;
    private String _username;

    public String getAccessToken() {
        return _accessToken;
    }
    public void setAccessToken(String value) {
        _accessToken = value;
    }

    public String getRefreshToken() {
        return _refreshToken;
    }
    public void setRefreshToken(String value) {
        _refreshToken = value;
    }

    public Date getExpires() {
        return _expires;
    }
    public void setExpires(String value) throws Exception {
        DateFormat format = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.FFFFFFK");
        _expires = format.parse(value);
    }

    public String getUsername() {
        return _username;
    }
    public void setUsername(String value) {
        _username = value;
    }
}
