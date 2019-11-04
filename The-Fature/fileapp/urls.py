from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.Upload.as_view(), name='upload'),
    path('upload_md5/', views.UploadMd5.as_view(), name='upload_md5'),
    path('all/', views.GetAllFile.as_view(), name='all'),
    path('share_file/', views.ShareFile.as_view(), name='share_file'),
    path('share/', views.MyShareFile.as_view(), name='share'),
    path('liked_file/', views.LikeDAPIView.as_view(), name='liked'),
    path('recently/', views.RecentlyAPIView.as_view(), name='recently'),
    path('liked/', views.MyLikeAPIView.as_view(), name='liked'),
    path('delete_liked/', views.DeleteLikeAPIView.as_view(), name='liked'),
]
