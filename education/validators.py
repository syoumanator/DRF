import re
from rest_framework import serializers


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile("^(https?://)?(www\.)?youtube\.com/.+$")
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise serializers.ValidationError("Неправильный URL YouTube")

