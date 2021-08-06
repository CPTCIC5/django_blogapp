from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:question_id>/',views.detail,name='detail'),
    path('delete/<int:question_id>/',views.delete_post,name='delete_post'),
    path('about/',views.about,name='about'),
    path('addpost/',views.addpost,name='addpost'),
]
