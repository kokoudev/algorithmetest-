import os

class Config:
    """Configuration de base"""
    DEBUG = os.environ.get('DEBUG', False)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    ENV = os.environ.get('ENV', 'development')

class ProductionConfig(Config):
    """Configuration de production (Railway/Render)"""
    DEBUG = False
    ENV = 'production'

class DevelopmentConfig(Config):
    """Configuration de développement local"""
    DEBUG = True
    ENV = 'development'

# Sélectionner la config appropriée
config = ProductionConfig() if os.environ.get('ENV') == 'production' else DevelopmentConfig()
