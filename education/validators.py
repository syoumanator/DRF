from rest_framework.serializers import ValidationError


def validate_url(value):
    valid_url = "https://youtube.com/"
    if not value.startswith(valid_url):
        raise ValidationError('Неверный URL YouTube')
