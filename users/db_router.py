class AuthSchemaRouter:
    """
    A database router to direct Django auth tables to auth schema.
    """
    schema_name = "auth"

    auth_models = {
        "auth", "users",
    }

    def db_for_read(self, model, **hints):
        """Direct all auth-related models to auth schema"""
        if model._meta.app_label in self.auth_models:
            return "default"
        return None

    def db_for_write(self, model, **hints):
        """Direct all auth-related models to auth schema"""
        if model._meta.app_label in self.auth_models:
            return "default"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Allow migrations only for auth models in auth schema"""
        if app_label in self.auth_models:
            return db == "default"
        return None
