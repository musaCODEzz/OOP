class BadEmailService:

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    # We could also force clients to call connect, authenticate, send_email, and disconnect to send an email. That wouldn't be very nice tho! No abstraction means more effort for client/dev.
    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")


email = BadEmailService()

email.send_email()
