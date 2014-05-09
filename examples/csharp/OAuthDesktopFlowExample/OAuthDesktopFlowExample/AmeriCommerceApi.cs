using System.IO;
using System.Linq;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using OAuthDesktopFlowExample.Helpers;
using OAuthDesktopFlowExample.Models;

namespace OAuthDesktopFlowExample
{
    public class AmeriCommerceApi
    {
        private readonly string _domain;
        private readonly int _appId;
        private readonly string _scope;
        private readonly string _secret;
        private readonly string _initUri;
        private readonly string _verifyUri;
        private readonly string _resourcePrefix;

        public AmeriCommerceApi(string domain, int appId, string scope, string secret)
        {
            _domain = domain;
            _appId = appId;
            _scope = scope;
            _secret = secret;

            _initUri = string.Format("https://{0}/api/oauth", _domain);
            _verifyUri = string.Format("https://{0}/api/oauth/access_token", _domain);
            _resourcePrefix = string.Format("https://{0}/api/v1", _domain);
        }

        public ApiToken GetToken(string username, string userApiKey)
        {
            var initResponse = StartNegotiation(username, userApiKey);
            var token = Verify(initResponse);

            return token;
        }

        public ProductList GetProductList(ApiToken token)
        {
            var uri = _resourcePrefix + "/products";
            return SendRequest<ProductList>(uri, "GET", token);
        }

        private TokenInitResponse StartNegotiation(string username, string userApiKey)
        {
            var signature = CreateSignature(_secret, username, userApiKey, _appId, _scope, _domain);
            var tokenInit = new TokenInitialization
            {
                AppId = _appId,
                Scope = _scope,
                RedirectUrl = _domain,
                Username = username,
                Signature = signature
            };

            var response = SendRequest<TokenInitResponse>(_initUri, "POST", tokenInit);

            return response;
        }

        private ApiToken Verify(TokenInitResponse initResponse)
        {
            var signature = CreateSignature(_secret, initResponse.Code, _appId, _scope, _domain);
            var verify = new TokenVerify
            {
                AppId = _appId,
                AuthId = initResponse.AuthId,
                Signature = signature
            };

            var response = SendRequest<ApiToken>(_verifyUri, "POST", verify);

            return response;
        }

        private T SendRequest<T>(string uri, string method, object body = null)
        {
            return SendRequest<T>(uri, method, null, body);
        }

        private T SendRequest<T>(string uri, string method, ApiToken token, object body = null)
        {
            var req = (HttpWebRequest)WebRequest.Create(uri);

            req.Method = method;
            req.ContentType = "application/json";

            if (token != null)
                req.Headers.Add("X-AC-Auth-Token", token.AccessToken);

            if (body != null)
            {
                using (var writer = new StreamWriter(req.GetRequestStream()))
                {
                    writer.Write(body.ToJson());
                }
            }

            var res = (HttpWebResponse)req.GetResponse();
            T result;

            using (var reader = new StreamReader(res.GetResponseStream()))
            {
                result = reader.ReadToEnd().FromJson<T>();
            }

            return result;
        }

        private string CreateSignature(params object[] args)
        {
            var combined = string.Join("", args);
            var algorithm = SHA256.Create();
            var hash = algorithm.ComputeHash(Encoding.UTF8.GetBytes(combined));

            return hash.Aggregate(string.Empty, (current, b) => current + b.ToString("x2"));
        }
    }
}