using Newtonsoft.Json.Serialization;

namespace OAuthWebFlowExample.Helpers
{
    public class SnakeCaseContractResolver : DefaultContractResolver
    {
        protected override string ResolvePropertyName(string propertyName)
        {
            return propertyName.ToSnakeCase();
        }
    }
}