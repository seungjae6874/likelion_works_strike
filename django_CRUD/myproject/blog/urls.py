from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello,name = 'hello'),
    path('intro/',views.intro, name = 'intro'),
    path('new/', views.new, name= 'new'),
    path('create/',views.create, name= 'create'),
    path('<int:blog_id>/update/',views.update, name= 'update'),
    path('<int:blog_id>/delete/',views.delete, name= 'delete'),
    path('<int:blog_id>/',views.detail, name = 'detail'),
    path('fake/',views.fake, name = 'fake'),

    
]