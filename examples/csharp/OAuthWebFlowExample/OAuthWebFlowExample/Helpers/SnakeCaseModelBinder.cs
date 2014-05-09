using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Web.Mvc;

namespace OAuthWebFlowExample.Helpers
{
    public class SnakeCaseModelBinder : DefaultModelBinder
    {
        protected override PropertyDescriptorCollection GetModelProperties(ControllerContext controllerContext, ModelBindingContext bindingContext)
        {
            var result = base.GetModelProperties(controllerContext, bindingContext);
            var additional = new List<PropertyDescriptor>();

            foreach (var p in GetTypeDescriptor(controllerContext, bindingContext).GetProperties().Cast<PropertyDescriptor>())
            {
                var propName = p.Name.ToSnakeCase();

                if (String.Equals(propName, p.Name, StringComparison.CurrentCultureIgnoreCase))
                    continue;

                additional.Add(new SnakeCasePropertyDescriptor(propName, p));

                if (bindingContext.PropertyMetadata.ContainsKey(p.Name))
                    bindingContext.PropertyMetadata.Add(propName, bindingContext.PropertyMetadata[p.Name]);
            }

            return new PropertyDescriptorCollection(result.Cast<PropertyDescriptor>().Concat(additional).ToArray());
        }
    }
}