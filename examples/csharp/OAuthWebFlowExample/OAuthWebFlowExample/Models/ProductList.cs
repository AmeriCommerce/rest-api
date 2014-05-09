using System.Collections.Generic;

namespace OAuthWebFlowExample.Models
{
    public class ProductList
    {
        public int TotalCount { get; set; }
        public string NextPage { get; set; }
        public string PreviousPage { get; set; }
        public List<Product> Products { get; set; } 

        public int CurrentPage { get; set; }
    }
}