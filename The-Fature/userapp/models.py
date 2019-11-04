from django.db import models
# Create your models here.


class BaseModel(models.Model):
    mtime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        abstract = True  # 抽象基类


class User(BaseModel):
    display_name = models.CharField(max_length=30, verbose_name='昵称')
    account = models.CharField(max_length=30, unique=True, verbose_name='账号')
    password = models.CharField(max_length=255, verbose_name='')

    def __str__(self): return self.display_name


class UserInfo(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='关联用户')
    data = models.TextField(verbose_name='用户详情')

    def __str__(self):
        return self.user.display_name


