from rest_framework import serializers
from userapp.models import User
from django.contrib.auth.hashers import make_password, check_password
from fileapp.models import *


class UserSignUpSerializer(serializers.ModelSerializer):
    def create(self, value):
        password = value.pop('password')
        value['display_name'] = value['account']
        oc_user = User(
            **value
        )
        oc_user.password = make_password(password)
        oc_user.save()
        return oc_user

    class Meta:
        model = User
        fields = ['account', 'password']


class StorageSerializerAPIView(serializers.Serializer):
    user_id = serializers.IntegerField(allow_null=True)
    is_active = serializers.BooleanField(default=True)
    size = serializers.FloatField()
    used = serializers.FloatField()
    path = serializers.CharField()

    def create(self, validated_data):
        storage = Storage.objects.create(**validated_data)
        return storage



