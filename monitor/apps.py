import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = 'monitor'
    MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeModel.joblib")
    model = joblib.load(MODEL_FILE)