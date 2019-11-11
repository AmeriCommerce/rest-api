using System.Configuration;
using System.IO;
using System.Net;
using System.Web.Mvc;
using Newtonsoft.Json;
using OAuthWebFlowExample.Filters;
using OAuthWebFlowExample.Helpers;
using OAuthWebFlowExample.Models;

namespace OAuthWebFlowExample.Controllers
{
    [OAuth]
    public class ProductsController : Controller
    {
        public ActionResult Index(int page = 1)
        {
            var url = string.Format("https://{0}/api/v1/products", ConfigurationManager.AppSettings["StoreDomain"]);

            if (page > 1)
                url += "?page=" + page;

            var apiUser = (ApiUser) Session["ApiUser"];

            var req = (HttpWebRequest) WebRequest.Create(url);
            req.Headers.Add("X-AC-Auth-Token", apiUser.AccessToken);

            var res = (HttpWebResponse) req.GetResponse();
            ProductList result;

            using (var reader = new StreamReader(res.GetResponseStream()))
            {
                result = reader.ReadToEnd().FromJson<ProductList>();
            }

            result.CurrentPage = page;
            return View(result);
        }
    }
}