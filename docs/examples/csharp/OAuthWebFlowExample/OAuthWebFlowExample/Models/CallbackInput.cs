namespace OAuthWebFlowExample.Models
{
    public class CallbackInput
    {
        public string AuthId { get; set; }
        public string Code { get; set; }
        public string R { get; set; }
        public string Error { get; set; }
        public string ErrorReason { get; set; }
        public string ErrorDescription { get; set; }
    }
}