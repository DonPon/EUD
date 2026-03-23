from rest_framework import serializers

class DynamicSerializerFactory:
    @staticmethod
    def create_serializer(model_class, config=None):
        """Create a ModelSerializer for a given model on the fly."""
        config = config or {}
        
        # Get the base fields from config
        base_fields = config.get('fields', '__all__')
        
        # Add custom fields for Relationship models
        extra_fields = {}
        relationship_fields = [
            'related_banking_relationship',
            'related_name_of_banking_relationship',
            'related_first_name',
            'related_last_name',
            'related_client_link'
        ]
        
        if model_class.__name__ in ['Relationship', 'LE_Relationship']:
            for field_name in relationship_fields:
                extra_fields[field_name] = serializers.CharField(read_only=True)
            # Include the extra fields in the fields list
            if base_fields == '__all__':
                base_fields = [f.name for f in model_class._meta.fields] + relationship_fields
            else:
                base_fields = list(base_fields) + relationship_fields

        class Meta:
            model = model_class
            fields = base_fields

        serializer_name = f"{model_class.__name__}Serializer"
        return type(serializer_name, (serializers.ModelSerializer,), {
            'Meta': Meta,
            **extra_fields
        })
