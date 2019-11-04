from rest_framework import serializers
from fileapp.models import *


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class FileUploadByMD5Serializer(serializers.Serializer):
    user_id = serializers.IntegerField(write_only=True)  # 关联用户的主键
    filename = serializers.CharField(max_length=150)  # 文件名

    def create(self, value):
        local_file = self.context['local_file']  # 单独传入处理 一个数据对象
        file = File.objects.create(
            storage=local_file.storage,
            size=local_file.size,
            md5=local_file.md5,
            mimetype=local_file.mimetype,
            type=local_file.type,
            addr=local_file.addr,
            **value,
        )
        return file


class ShareSerializer(serializers.Serializer):
    token = serializers.CharField()
    file_id = serializers.IntegerField()
    timestamp = serializers.CharField()
    from_user_id = serializers.IntegerField(allow_null=True)
    recv_user_id = serializers.IntegerField(allow_null=True)
    is_trash = serializers.IntegerField(default=1)
    password = serializers.CharField(allow_null=True)

    def create(self, validated_data):
        storage = Share.objects.create(**validated_data)
        return storage


class ShareModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'


class LikeDSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    file_id = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        print(validated_data)
        storage = Liked.objects.create(**validated_data)
        return storage


class RecentlySerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    operation = serializers.CharField()

    def create(self, validated_data):
        print(validated_data)
        storage = Recently.objects.create(**validated_data)
        return storage


class RecentlyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recently
        fields = '__all__'
