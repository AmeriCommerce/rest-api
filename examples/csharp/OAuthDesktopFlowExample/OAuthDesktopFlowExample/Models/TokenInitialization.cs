namespace OAuthDesktopFlowExample.Models
{
    public class TokenInitialization
    {
        public int AppId { get; set; } 
        public string Scope { get; set; }
        public string RedirectUrl { get; set; }
        public string Username { get; set; }
        public string Signature { get; set; }
    }

    public class TokenInitResponse
    {
        public int AuthId { get; set; }
        public string Code { get; set; }
    }
}