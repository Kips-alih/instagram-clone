from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$',views.index,name= 'index'),
  url('profile/', views.profile, name='profile'),
  url(r'^search/', views.search_results, name='search_results'),
  url(r'^new/image$', views.new_image, name='newImage'),
  url(r'^image/',views.image,name ='image'),
  url('like/', views.like_image, name='like-image'),
  url('comment/', views.comment, name='comment'),


]