public class OAuthVerifyRequestModel {
    private int _appId;
    private int _authId;
    private String _signature;

    public int getAppId() {
        return _appId;
    }
    public void setAppId(int value) {
        _appId = value;
    }

    public int getAuthId() {
        return _authId;
    }
    public void setAuthId(int value) {
        _authId = value;
    }

    public String getSignature() {
        return _signature;
    }
    public void setSignature(String value) {
        _signature = value;
    }
}
