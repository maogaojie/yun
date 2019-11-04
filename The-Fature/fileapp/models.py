from django.db import models
from userapp.models import BaseModel, User, UserInfo


# Create your models here.

class Storage(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='关联用户')
    is_active = models.BooleanField(default=True, verbose_name='是否可用')
    size = models.FloatField(verbose_name='节点大小')
    used = models.FloatField(verbose_name='已使用大小')
    path = models.CharField(max_length=150, verbose_name='存储位置')

    @property  # 把一个类中方法  定义为属性
    def used_percent(self):
        return ('%.2f' % (self.used / self.size))  # 使用百分比

    def __str__(self):
        return self.user.display_name + ' : ' + self.used_percent


class MIMEType(BaseModel):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class File(BaseModel):
    # Linux下一切皆文件
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='关联用户')
    # 如何实现 文件上传重复 引用 数据指纹 md5 ->
    storage = models.ForeignKey(
        Storage, on_delete=models.CASCADE, verbose_name='所属节点')  #
    filename = models.CharField(max_length=150, verbose_name='文件名')
    size = models.FloatField(verbose_name='文件大小')  #
    md5 = models.CharField(max_length=150, verbose_name='文件md5值')  #
    mimetype = models.CharField(max_length=150, verbose_name='文件MIME类型')  #
    is_trash = models.BooleanField(default=False, verbose_name='文件是否被删除')
    type_choices = (
        (1, 'File'),
        (2, 'Directory'),
    )
    type = models.IntegerField(choices=type_choices, verbose_name='文件类型')  #
    directory = models.ForeignKey(
        'self', models.SET_NULL, null=True, blank=True, verbose_name='文件父级目录')
    addr = models.CharField(max_length=150, verbose_name='文件存储地址')  #

    def __str__(self):
        return self.filename


class Share(BaseModel):
    # 分享文件， 文件一定不能存储在像 static这样的地方下
    # a(file) -> b(django) -> Views -> Streaming -> vue
    # token值 -> 访问的文件是哪个？
    token = models.CharField(max_length=150, verbose_name='分享Token')
    file = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name='分享文件')
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='from_user', verbose_name='分享者')
    timestamp = models.CharField(max_length=128)
    recv_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='recv_user', verbose_name='接收分享者')
    is_trash = models.IntegerField(default=1, verbose_name='是否删除分享')
    password = models.CharField(max_length=120, null=True, blank=True, verbose_name='访问密码')

    def __str__(self):
        return self.from_user.display_name


class Liked(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='收藏者')
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, verbose_name='收藏文件')
    is_active = models.BooleanField(default=True, verbose_name='收藏状态')

    class Meta:
        unique_together = ('user', 'file')

    def __str__(self):
        return self.user.display_name + ' : ' + self.file.filename


class Recently(BaseModel):  # 最近记录
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operation = models.CharField(max_length=255)

    class Meta:
        db_table = 'Recently'
