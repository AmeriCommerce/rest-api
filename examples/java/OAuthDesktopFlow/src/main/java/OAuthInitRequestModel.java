public class OAuthInitRequestModel {
    private int _appId;
    private String _scope;
    private String _redirectUrl;
    private String _username;
    private String _signature;

    public int getAppId() {
        return _appId;
    }
    public void setAppId(int value) {
        _appId = value;
    }

    public String getScope() {
        return _scope;
    }
    public void setScope(String value) {
        _scope = value;
    }

    public String getRedirectUrl() {
        return _redirectUrl;
    }
    public void setRedirectUrl(String value) {
        _redirectUrl = value;
    }

    public String getUsername() {
        return _username;
    }
    public void setUsername(String value) {
        _username = value;
    }

    public String getSignature() {
        return _signature;
    }
    public void setSignature(String value) {
        _signature = value;
    }
}
