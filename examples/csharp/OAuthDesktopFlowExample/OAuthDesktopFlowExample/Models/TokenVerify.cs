namespace OAuthDesktopFlowExample.Models
{
    public class TokenVerify
    {
        public int AppId { get; set; } 
        public int AuthId { get; set; }
        public string Signature { get; set; }
    }
}