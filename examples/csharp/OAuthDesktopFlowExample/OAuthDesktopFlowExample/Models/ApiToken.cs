using System;

namespace OAuthDesktopFlowExample.Models
{
    public class ApiToken
    {
        public string AccessToken { get; set; } 
        public string RefreshToken { get; set; }
        public DateTime? Expires { get; set; }
    }
}