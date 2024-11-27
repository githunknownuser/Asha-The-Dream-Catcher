import joblib
from sklearn.linear_model import LinearRegression


class MLModelManager:
    def __init__(self):
        self.models = {}

    def train_model(self, model_name, X, y):
        """Trains a new machine learning model."""
        model = LinearRegression()
        model.fit(X, y)
        self.models[model_name] = model
        print(f"Model '{model_name}' trained successfully.")
        return model

    def save_model(self, model_name, file_path):
        """Saves a trained model to a file."""
        if model_name in self.models:
            joblib.dump(self.models[model_name], file_path)
            print(f"Model '{model_name}' saved to {file_path}.")
        else:
            print(f"Model '{model_name}' not found.")

    def load_model(self, model_name, file_path):
        """Loads a model from a file."""
        try:
            model = joblib.load(file_path)
            self.models[model_name] = model
            print(f"Model '{model_name}' loaded from {file_path}.")
        except FileNotFoundError:
            print(f"File {file_path} not found.")

    def predict(self, model_name, X):
        """Uses a trained model to make predictions."""
        if model_name in self.models:
            return self.models[model_name].predict(X)
        else:
            print(f"Model '{model_name}' not found.")
            return None

    def list_models(self):
        """Lists all trained models."""
        return list(self.models.keys())

    def delete_model(self, model_name):
        """Deletes a model from the manager."""
        if model_name in self.models:
            del self.models[model_name]
            print(f"Model '{model_name}' deleted.")
        else:
            print(f"Model '{model_name}' not found.")