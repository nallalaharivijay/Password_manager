from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings

# Generate and store a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

class PasswordEntry(models.Model):
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    encrypted_password = models.TextField()

    def save_password(self, password):
        self.encrypted_password = cipher_suite.encrypt(password.encode()).decode()

    def get_password(self):
        return cipher_suite.decrypt(self.encrypted_password.encode()).decode()

    def __str__(self):
        return f"{self.website} - {self.username}"
