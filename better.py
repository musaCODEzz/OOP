class EmailService:
    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        # All the necessary operations for sending an email are handled internally
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")

# Client code:
email = EmailService()
email.send_email()

# LOGS:
# Connecting to email server...
# Authenticating...
# Sending email...
# Disconnecting from email server...
