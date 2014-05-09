using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OAuthDesktopFlowExample
{
    class Program
    {
        static void Main(string[] args)
        {
            var domain = ConfigurationManager.AppSettings["StoreDomain"];
            var secret = ConfigurationManager.AppSettings["AppSecret"];
            var appId = Convert.ToInt32(ConfigurationManager.AppSettings["AppId"]);
            var appScope = ConfigurationManager.AppSettings["AppScope"];

            var api = new AmeriCommerceApi(domain, appId, appScope, secret);

            Console.Write("Username: ");
            var username = Console.ReadLine();

            Console.Write("API Key: ");
            var key = Console.ReadLine();

            var token = api.GetToken(username, key);
            var productList = api.GetProductList(token);

            Console.WriteLine();

            foreach (var product in productList.Products)
                Console.WriteLine("{0}: {1:C}", product.ItemName, product.Price);

            Console.ReadKey();
        }
    }
}
