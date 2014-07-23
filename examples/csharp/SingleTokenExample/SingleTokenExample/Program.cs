using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using Newtonsoft.Json;

namespace SingleTokenExample
{
    class Program
    {
        private const string STORE_DOMAIN = "<< YOUR STORE DOMAIN >>";
        private const string ACCESS_TOKEN = "<< YOUR ACCESS TOKEN >>";

        static void Main(string[] args)
        {
            var settings = new JsonSerializerSettings
            {
                ContractResolver = new SnakeCaseContractResolver(),
                DateFormatHandling = DateFormatHandling.IsoDateFormat
            };

            var req = (HttpWebRequest) WebRequest.Create(string.Format("https://{0}/api/v1/products", STORE_DOMAIN));
            req.Headers.Add("X-AC-Auth-Token", ACCESS_TOKEN);

            var res = (HttpWebResponse) req.GetResponse();
            ProductList list = null;

            using (var stream = res.GetResponseStream())
            {
                if (stream != null)
                {
                    using (var reader = new StreamReader(stream))
                    {
                        list = JsonConvert.DeserializeObject<ProductList>(reader.ReadToEnd(), settings);
                    }
                }
            }

            res.Close();

            if (list != null)
            {
                foreach (var product in list.Products)
                {
                    Console.WriteLine("{0}: {1:C}", product.ItemName, product.Price);
                }
            }

            Console.WriteLine("Press any key to continue...");
            Console.ReadKey();
        }
    }

    public class Product
    {
        public string ItemName { get; set; }
        public decimal Price { get; set; }
    }

    public class ProductList
    {
        public List<Product> Products { get; set; } 
        public string NextPage { get; set; }
        public string PreviousPage { get; set; }
        public int TotalCount { get; set; }
    }
}
