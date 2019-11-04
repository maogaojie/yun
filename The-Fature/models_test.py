class User:
    # 用户表
    # username
    # email
    # password -> hash

class UserInfo:
    # 用户信息
    # User
    # data: {个人信息json}

class UserStorgae
    # 用户存储节点信息
    # 存储节点路径
    # 配额
    # 已使用大小
    # 节点状态(0,1)

class File
    # 文件
    # User
    # UserStorgae
    # 文件名
    # 文件大小
    # 文件md5 唯一
    # MimeType
    # 文件状态(trash)
    # Directory(父级)
    # PATH
    # 文件类型: 文件还是目录

class MimeType:
    # 文件mimetype类型
    # 类型

class Liked:
    # 文件收藏
    # User
    # File

class Share:
    # 文件共享
    # token
    # 密码
    # 共享时效(-1 -> forever)
    # 共享连接
    # 分享类型
        # 0 连接分享
        # 1 用户分享
    # User 接收分享用户
    # File

class ActiveType:
    # 动态类型
        # 分享
        # 创建文件
        # 删除文件
        # 修改文件
        # 移动
    # 

class Active
    # 文件动态

class Comment:
    # 评论
    # File
    # User
    # Message

class Tag:
    # 文件标签