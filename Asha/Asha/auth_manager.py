import hashlib
import uuid


class AuthManager:
    def __init__(self):
        self.sessions = {}
        self.users = {}

    def hash_password(self, password):
        """Hashes a password using SHA256 (simulated)."""
        salt = uuid.uuid4().hex
        hashed = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        return salt, hashed

    def verify_password(self, stored_password, salt, provided_password):
        """Verifies a password against the stored hash (simulated)."""
        return stored_password == hashlib.sha256(salt.encode() + provided_password.encode()).hexdigest()

    def register_user(self, username, password):
        """Registers a new user with username and password."""
        if username in self.users:
            return False
        salt, hashed_password = self.hash_password(password)
        self.users[username] = (salt, hashed_password)
        print(f"User '{username}' registered successfully.")
        return True

    def authenticate_user(self, username, password):
        """Authenticates a user and starts a session."""
        if username not in self.users:
            return False
        salt, stored_password = self.users[username]
        if not self.verify_password(stored_password, salt, password):
            return False

        session_token = uuid.uuid4().hex
        self.sessions[session_token] = username
        print(f"User '{username}' authenticated successfully. Session started.")
        return session_token

    def end_session(self, session_token):
        """Ends a user session."""
        if session_token in self.sessions:
            username = self.sessions.pop(session_token)
            print(f"Session for user '{username}' ended.")
            return True
        return False

    def get_logged_in_user(self, session_token):
        """Retrieves the username for a given session token."""
        return self.sessions.get(session_token)

    def list_users(self):
        """Lists all registered users (for debugging purposes)."""
        return list(self.users.keys())

    def list_sessions(self):
        """Lists all active sessions (for debugging purposes)."""
        return list(self.sessions.keys())