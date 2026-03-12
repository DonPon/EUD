from rest_framework import serializers

class DynamicSerializerFactory:
    @staticmethod
    def create_serializer(model_class, config=None):
        """Create a ModelSerializer for a given model on the fly."""
        config = config or {}
        
        class Meta:
            model = model_class
            fields = config.get('fields', '__all__')
        
        serializer_name = f"{model_class.__name__}Serializer"
        return type(serializer_name, (serializers.ModelSerializer,), {'Meta': Meta})
