import json
import os


class PreferencesManager:
    def __init__(self, preferences_file='user_preferences.json'):
        self.preferences_file = preferences_file
        self.preferences = self.load_preferences()

    def load_preferences(self):
        """Loads user preferences from a JSON file."""
        if not os.path.exists(self.preferences_file):
            return {}

        with open(self.preferences_file, 'r') as file:
            return json.load(file)

    def save_preferences(self):
        """Saves user preferences to a JSON file."""
        with open(self.preferences_file, 'w') as file:
            json.dump(self.preferences, file, indent=4)

    def get_preference(self, key, default=None):
        """Retrieves a preference value by key."""
        return self.preferences.get(key, default)

    def set_preference(self, key, value):
        """Sets a preference value."""
        self.preferences[key] = value
        self.save_preferences()

    def remove_preference(self, key):
        """Removes a preference value."""
        if key in self.preferences:
            del self.preferences[key]
            self.save_preferences()

    def list_preferences(self):
        """Lists all preferences."""
        return self.preferences

    def reset_preferences(self):
        """Resets all preferences."""
        self.preferences = {}
        self.save_preferences()
