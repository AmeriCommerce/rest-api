using Newtonsoft.Json;

namespace OAuthDesktopFlowExample.Helpers
{
    public static class JsonHelper
    {
        private static readonly SnakeCaseContractResolver _resolver = new SnakeCaseContractResolver();
        private static readonly JsonSerializerSettings _settings;

        static JsonHelper()
        {
            _settings = new JsonSerializerSettings
            {
                ContractResolver = _resolver,
                Formatting = Formatting.None,
                DateFormatHandling = DateFormatHandling.IsoDateFormat
            };
        }

        public static string ToJson(this object obj)
        {
            return JsonConvert.SerializeObject(obj, _settings);
        }

        public static T FromJson<T>(this string json)
        {
            return JsonConvert.DeserializeObject<T>(json, _settings);
        }
    }
}