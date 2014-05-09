using System.Collections.Generic;

namespace OAuthDesktopFlowExample.Models
{
    public class ProductList
    {
        public int TotalCount { get; set; }
        public string NextPage { get; set; }
        public string PreviousPage { get; set; }
        public List<Product> Products { get; set; }
    }
}