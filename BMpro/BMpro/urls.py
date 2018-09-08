from django.contrib import admin
from django.urls import path,include
from QueAns import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',include('QueAns.urls')),
    path('',views.Index,name='index'),
]
