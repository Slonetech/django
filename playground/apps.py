# Import the AppConfig class from the django.apps module
from django.apps import AppConfig

# Define a custom configuration class named PlaygroundConfig, which inherits from AppConfig
class PlaygroundConfig(AppConfig):
    # Set the default auto field for models to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Set the name attribute for the app to 'playground'
    name = 'playground'
