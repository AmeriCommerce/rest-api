namespace OAuthWebFlowExample.Models
{
    public class VerifyRequestBody
    {
        public string AppId { get; set; } 
        public string AuthId { get; set; }
        public string Signature { get; set; }
    }
}