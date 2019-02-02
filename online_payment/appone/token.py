from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class tokengenerate(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.id)+six.text_type(timestamp)+six.text_type(user.active)
        )

activation_token=tokengenerate()