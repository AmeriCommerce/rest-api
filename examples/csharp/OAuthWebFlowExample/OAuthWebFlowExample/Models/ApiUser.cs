using System;

namespace OAuthWebFlowExample.Models
{
    public class ApiUser
    {
        public string AccessToken { get; set; }
        public string RefreshToken { get; set; }
        public DateTime? Expires { get; set; }
        public string Username { get; set; }
    }
}