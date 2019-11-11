using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace OAuthWebFlowExample.Filters
{
    public class OAuthAttribute : ActionFilterAttribute
    {
        public override void OnActionExecuting(ActionExecutingContext filterContext)
        {
            var httpContext = filterContext.HttpContext;

            if (httpContext.Session != null && httpContext.Session["ApiUser"] != null)
            {
                base.OnActionExecuting(filterContext);
                return;
            }

            var requestUri = httpContext.Request.Url.ToString();
            var routeDictionary = new RouteValueDictionary
            {
                {"controller", "sessions"},
                {"action", "index"},
                {"r", requestUri}
            };
            filterContext.Result = new RedirectToRouteResult(routeDictionary);
        }
    }
}