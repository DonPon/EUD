class CrudRegistry:
    _registry = {}

    @classmethod
    def register(cls, model_class, config=None):
        """
        Registers a model for CRUD generation.
        config can include:
            - section: The UI section this model belongs to (e.g. 'np', 'le')
            - fields: list of fields to include in serializers/views
            - list_display: fields to show in DataTables
            - search_fields: fields to include in search
            - filter_fields: fields to include in filters
        """
        model_name = model_class._meta.model_name
        cls._registry[model_name] = {
            'model': model_class,
            'config': config or {}
        }
        return model_class

    @classmethod
    def get_registered_models(cls, section=None):
        """Returns registered models, optionally filtered by section."""
        if section:
            filtered = {}
            for name, details in cls._registry.items():
                model_section = details['config'].get('section')
                # Check if requested section matches a single value or is within a list
                if isinstance(model_section, list):
                    if section in model_section:
                        filtered[name] = details
                elif model_section == section:
                    filtered[name] = details
            return filtered
        return cls._registry

    @classmethod
    def get_config(cls, model_name):
        return cls._registry.get(model_name)
