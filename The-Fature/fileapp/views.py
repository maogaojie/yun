from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
import psutil
import os
import re
import random
from hashlib import md5
import mimetypes
import uuid
from django.http import StreamingHttpResponse, Http404, FileResponse, HttpResponse, HttpResponseNotModified
from django.views import View
import base64
import stat
from django.views.static import was_modified_since
from django.utils.http import http_date
from django.utils.encoding import escape_uri_path
from fileapp.serializer import *
from fileapp.models import *

CHAR_ = [chr(var) for var in range(97, 123)] + [chr(var) for var in range(65, 91)]
NUM_ = [str(var) for var in range(9)]


def get_dickusage(path):
    return psutil.disk_usage(path)


def calMD5(str):
    m = md5()
    m.update(str)

    return m.hexdigest()


def calMD5ForBigFile(file):
    m = md5()
    buffer = 8192  # why is 8192 | 8192 is fast than 2048
    while 1:
        chunk = file.read(buffer)
        if not chunk: break
        m.update(chunk)
    return m.hexdigest()


def get_file_mime(file):
    mime = mimetypes.guess_type(file)[0]
    if not mime:
        return 'application/octet-stream'  # 取不到类型的 都认为是二进制
    return mime


def upload_file_by_chunks(path, file_name, upload_file):
    with open(os.path.join(path, file_name), 'wb') as fp:
        for buf in upload_file.chunks():
            fp.write(buf)


class UploadMd5(APIView):
    def post(self, request):
        data = {}
        user_id = request.session['user_id']
        path = Storage.objects.get(user_id=user_id).path  # 存储节点
        file_md5 = request.data['file_md5']  # 待上传文件的md5值
        file_name = request.data['filename']
        files = File.objects.filter(
            md5=file_md5
        )
        if not files:
            data['message'] = '没有出现过同样的md5文件，不可以秒传'
            data['code'] = 40004
        else:  # 判断秒传文件名是否重复
            if file_name in os.listdir(path):  # 获取当前存储目录下的所有文件
                ran_ = ''.join(random.sample(CHAR_ + NUM_, 6))
                file_name = os.path.splitext(file_name)[0] + '_' + ran_ + os.path.splitext(file_name)[-1]
            file_upload_by_md5 = FileUploadByMD5Serializer(
                data={'filename': file_name, 'user_id': user_id}, context={'local_file': files[0]}
            )
            if file_upload_by_md5.is_valid():
                file_upload_by_md5.save()

                operation = '上传了文件%s' % file_name
                datas = {}
                datas['operation'] = operation
                datas['user_id'] = user_id
                rec = RecentlySerializer(data=datas)
                if rec.is_valid():
                    rec.save()

                else:
                    print(rec.errors)
                data['message'] = '秒传Success'
                data['code'] = 0
            else:
                data['message'] = '秒传失败:%s' % str(file_upload_by_md5.errors)
                data['code'] = 40003
        return Response(data)


class Upload(APIView):
    def post(self, request):
        # 先取出节点
        data = {}
        user_id = request.session['user_id']
        storage = Storage.objects.get(user_id=user_id)
        upload_file = request.data['file']  # 上传的文件 本身就是个打开的文件
        file_md5 = request.data['file_md5']  # 待上传文件的md5值
        if upload_file.name in os.listdir(storage.path):  # 获取当前存储目录下的所有文件
            ran_ = ''.join(random.sample(CHAR_ + NUM_, 6))
            file_name = os.path.splitext(upload_file.name)[0] + '_' + ran_ + os.path.splitext(upload_file.name)[-1]
        else:
            file_name = upload_file.name
        if upload_file.size < (storage.size * .8) and upload_file.size < get_dickusage(storage.path).free:
            upload_file_by_chunks(storage.path, file_name, upload_file)  # 保存文件至本地目录
            upload_file_mime = get_file_mime(os.path.join(storage.path, file_name))  # 上传文件的MIME类型
            File.objects.create(
                user_id=user_id,  # 假设
                storage_id=storage.id,  # 用户所属节点
                filename=file_name,
                size=upload_file.size,
                md5=file_md5,
                mimetype=upload_file_mime,
                type=1,  # 上传的是文件
                addr=os.path.join(storage.path, file_name),  # 真实存储的物理地址
            )
            data['message'] = '上传成功'
            data['code'] = 0
            operation = '上传了文件%s' % file_name

            datas = {}
            datas['operation'] = operation
            datas['user_id'] = user_id
            rec = RecentlySerializer(data=datas)
            if rec.is_valid():
                rec.save()
            else:
                print(rec.errors)
        else:
            data['message'] = 'Storage is full'
            data['code'] = "4001"
        return Response(data)


class CreateFloder(APIView):
    pass


class GetAllFile(APIView):  # 获取所有当前用户一级文件
    def get(self, request):
        user_id = request.session['user_id']  # 获取当前登陆用户
        print('获取到的user_id', user_id)
        data = {}
        files = File.objects.filter(
            user_id=user_id,  # 当前用户的文件
            directory=None,
        ).all()
        files_data = FileSerializer(files, many=True)
        # 用户每次访问全部数据时，返回随机token, 这个token代表用户本身，之后对于用户本身资源的访问必须携带该token
        data['data'] = files_data.data
        data['message'] = '当前用户的文件数据'
        data['code'] = 0
        return Response(data)


class ImageFile(View):  # 页面all接口 返回之后 页面里的数据 如图片会二次请求 img
    def get(self, request, md5):
        user_id = request.session.get('user_id')
        file = File.objects.filter(md5=md5, user_id=user_id).first()
        if file and 'image' in file.mimetype:  # 用户有权看到图片，此图片属于用户
            try:
                response = FileResponse(open(file.addr, 'rb'))
                response['Content-Type'] = file.mimetype
                # response['Content-Disposition'] = 'attachment;filename=' + file.filename
                return response
            except Exception as e:
                # print(e)
                raise Http404
        else:
            raise Http404


class DownlaodFile(View):
    def get(self, request, md5):
        user_id = request.session.get('user_id')
        if not user_id:
            raise Http404
        file = File.objects.filter(md5=md5, user_id=user_id).first()

        if not file:
            raise Http404
        statobj = os.stat(file.addr)
        if not was_modified_since(
                request.META.get('HTTP_IF_MODIFIED_SINCE'),
                statobj.st_mtime, statobj.st_size
        ):
            return HttpResponseNotModified()

        # 文件起点位置
        start_bytes = re.search(r'bytes=(\d+)-', request.META.get('HTTP_RANGE', ''), re.S)
        start_bytes = int(start_bytes.group(1)) if start_bytes else 0

        # 移动文件至上次下载位置
        the_file = open(file.addr, 'rb')
        the_file.seek(start_bytes, os.SEEK_SET)

        '''
        status=200表示下载开始，status=206表示下载暂停后继续，为了兼容火狐浏览器而区分两种状态
        关于django的response对象，参考：https://www.cnblogs.com/scolia/p/5635546.html
        关于response的状态码，参考：https://www.cnblogs.com/DeasonGuan/articles/Hanami.html
        FileResponse默认block_size = 4096，因此迭代器每次读取4KB数据
        '''
        response = FileResponse(
            the_file,
            content_type=file.mimetype or 'application/octet-stream',
            status=206 if start_bytes > 0 else 200)

        # 文件修改时间
        response['Last-Modified'] = http_date(statobj.st_mtime)

        # 这里'Content-Length'表示剩余待传输的文件字节长度
        if stat.S_ISREG(statobj.st_mode):
            response['Content-Length'] = statobj.st_size - start_bytes

        response['Content-Range'] = 'bytes %s-%s/%s' % (
            start_bytes,  # 起点
            statobj.st_size - 1,  #
            statobj.st_size
        )
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        # 设置默认下载文件名，当下载文件为中文命名时，特殊构造一波
        response['Content-Disposition'] = "attachment;filename={}".format(escape_uri_path(file.filename))
        operation = '下载了文件%s' % file.filename
        datas = {}
        datas['operation'] = operation
        datas['user_id'] = user_id
        rec = RecentlySerializer(data=datas)
        if rec.is_valid():
            rec.save()
        else:
            print(rec.errors)
        return response

        # if file: # 用户有权看到图片，此图片属于用户
        #     try:
        #         response = FileResponse(open(file.addr, 'rb'))
        #         response['Content-Type'] = file.mimetype or 'application/octet-stream'
        #         response['Content-Disposition'] = 'attachment;filename=' + file.filename
        #         return response
        #     except Exception as e:
        #         # print(e)
        #         raise Http404
        # else:
        #     raise Http404


class ShareFile(APIView):
    def post(self, request):
        mes = {}
        data = request.data.copy()
        if data['recv_user_id'] == '':
            data['recv_user_id'] = ''
        else:
            user = User.objects.filter(account=data['recv_user_id']).first()
            data['recv_user_id'] = user.id
        data['token'] = str(uuid.uuid1())
        data['from_user_id'] = request.session.get('user_id')

        file = File.objects.get(id=data['file_id'])
        share = ShareSerializer(data=data)
        if share.is_valid():
            share.save()

            operation = '分享了文件%s' % file.filename
            datas = {}
            datas['operation'] = operation
            datas['user_id'] = request.session.get('user_id')
            rec = RecentlySerializer(data=datas)
            if rec.is_valid():
                rec.save()
            else:
                print(rec.errors)
            mes['code'] = 200
            mes['message'] = '分享成功分享链接为:',
        else:
            print(share.errors)
            mes['code'] = 1001
            mes['message'] = '分享失败'
        return Response(mes)


class MyShareFile(APIView):
    def get(self, request):
        user_id = request.session.get('user_id')
        my_share_file = Share.objects.filter(from_user_id=user_id).all()
        my_share_file = ShareModelSerializer(my_share_file, many=True)
        mes = {}
        mes['code'] = 200
        mes['message'] = '获取成功'
        mes['data'] = my_share_file.data
        return Response(mes)


class LikeDAPIView(APIView):
    def post(self, request):
        mes = {}
        data = request.data.copy()
        user_id = request.session.get('user_id')
        data['user_id'] = user_id
        like = LikeDSerializer(data=data)
        if like.is_valid():
            like.save()
            file = File.objects.get(id=data['file_id'])
            operation = '收藏了文件%s' % file.filename
            datas = {}
            datas['operation'] = operation
            datas['user_id'] = request.session.get('user_id')
            rec = RecentlySerializer(data=datas)
            if rec.is_valid():
                rec.save()
            else:
                print(rec.errors)

            mes['code'] = 200
            mes['message'] = '收藏成功'
        else:
            mes['code'] = 1001
            mes['message'] = like.errors

        return Response(mes)


class RecentlyAPIView(APIView):
    def get(self, request):
        mes = {}
        id = request.session.get('user_id')
        rec = Recently.objects.filter(user_id=id).order_by('-ctime')
        print(rec)
        rec = RecentlyModelSerializer(rec, many=True)
        mes['code'] = 200
        mes['data'] = rec.data
        return Response(mes)


class MyLikeAPIView(APIView):
    def get(self, request):
        mes = {}
        id = request.session.get('user_id')
        print(id)
        like_list = Liked.objects.filter(user_id=id,is_active=True).all()
        file_list = []
        for i in like_list:
            file = File.objects.get(id=i.file_id)
            file = FileSerializer(file, many=False)
            file_list.append(file.data)
        print(file_list)
        mes['code'] = 200
        mes['data'] = file_list
        return Response(mes)


class DeleteLikeAPIView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        id = request.session.get('user_id')
        Liked.objects.filter(user_id=id, file_id=data['id']).update(is_active=False)
        mes = {}
        mes['code'] = 200
        return Response(mes)
