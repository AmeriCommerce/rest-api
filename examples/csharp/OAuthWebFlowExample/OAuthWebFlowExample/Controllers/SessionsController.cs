using System.Configuration;
using System.IO;
using System.Linq;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using System.Web;
using System.Web.Mvc;
using Newtonsoft.Json.Linq;
using OAuthWebFlowExample.Helpers;
using OAuthWebFlowExample.Models;

namespace OAuthWebFlowExample.Controllers
{
    public class SessionsController : Controller
    {
        public ActionResult Index(string r)
        {
            var callbackUrl = HttpUtility.UrlEncode(Url.Action("Callback", "Sessions", new {r}, "http"));

            var oauthUrl = string.Format("https://{0}/api/oauth?app_id={1}&scope={2}&redirect_url={3}",
                ConfigurationManager.AppSettings["StoreDomain"],
                ConfigurationManager.AppSettings["AppId"],
                ConfigurationManager.AppSettings["AppScope"],
                callbackUrl);

            return Redirect(oauthUrl);
        }

        public ActionResult Callback(CallbackInput model)
        {
            var callbackUrl = HttpUtility.UrlEncode(Url.Action("Callback", "Sessions", new {r = model.R}, "http"));
            var accessTokenUrl = string.Format("https://{0}/api/oauth/access_token", ConfigurationManager.AppSettings["StoreDomain"]);
            var req = (HttpWebRequest) WebRequest.Create(accessTokenUrl);
            var sig = CreateSignature(ConfigurationManager.AppSettings["AppSecret"], model.Code, ConfigurationManager.AppSettings["AppId"], ConfigurationManager.AppSettings["AppScope"], callbackUrl);

            req.Method = "POST";
            req.ContentType = "application/json";

            using (var writer = new StreamWriter(req.GetRequestStream()))
            {
                var verifyBody = new VerifyRequestBody
                {
                    AppId = ConfigurationManager.AppSettings["AppId"],
                    AuthId = model.AuthId,
                    Signature = sig
                };
                writer.Write(verifyBody.ToJson());
            }

            var res = req.GetResponse();
            ApiUser apiUser;

            using (var reader = new StreamReader(res.GetResponseStream()))
            {
                apiUser = reader.ReadToEnd().FromJson<ApiUser>();
            }
            Session["ApiUser"] = apiUser;

            return Redirect(model.R);
        }

        public ActionResult Refresh(string r)
        {
            return View();
        }

        private string CreateSignature(params string[] args)
        {
            var combined = string.Join("", args);
            var algorithm = SHA256.Create();
            var hash = algorithm.ComputeHash(Encoding.UTF8.GetBytes(combined));

            return hash.Aggregate(string.Empty, (current, b) => current + b.ToString("x2"));
        }
    }
}