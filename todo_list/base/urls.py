from django.conf import settings
from django.urls import path
from .views import RegisterPage, TaskDelete, TaskDetail, TaskList,TaskCreate,TaskUpate,CustomeLoginView
from django.contrib.auth.views import LogoutView


from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    
    path('login/', CustomeLoginView.as_view(), name='login'),  
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
    path('register/', RegisterPage.as_view(), name='register'), 

    path('', TaskList.as_view(), name='tasks'),  
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),  
    path('task-create', TaskCreate.as_view(), name='task-create'),  
    path('task-update/<int:pk>/', TaskUpate.as_view(), name='task-update'),  
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)