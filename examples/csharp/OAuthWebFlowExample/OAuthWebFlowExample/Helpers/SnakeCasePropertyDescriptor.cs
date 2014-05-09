using System;
using System.ComponentModel;

namespace OAuthWebFlowExample.Helpers
{
    public class SnakeCasePropertyDescriptor : PropertyDescriptor
    {
        public PropertyDescriptor Inner { get; private set; }

        public SnakeCasePropertyDescriptor(string name, PropertyDescriptor inner)
            : base(name, null)
        {
            Inner = inner;
        }

        public override bool CanResetValue(object component)
        {
            return Inner.CanResetValue(component);
        }

        public override object GetValue(object component)
        {
            return Inner.GetValue(component);
        }

        public override void ResetValue(object component)
        {
            Inner.ResetValue(component);
        }

        public override void SetValue(object component, object value)
        {
            Inner.SetValue(component, value);
        }

        public override bool ShouldSerializeValue(object component)
        {
            return Inner.ShouldSerializeValue(component);
        }

        public override Type ComponentType
        {
            get { return Inner.ComponentType; }
        }

        public override bool IsReadOnly
        {
            get { return Inner.IsReadOnly; }
        }

        public override Type PropertyType
        {
            get { return Inner.PropertyType; }
        }
    }
}