using Newtonsoft.Json.Serialization;

namespace OAuthDesktopFlowExample.Helpers
{
    public class SnakeCaseContractResolver : DefaultContractResolver
    {
        protected override string ResolvePropertyName(string propertyName)
        {
            return propertyName.ToSnakeCase();
        }
    }
}