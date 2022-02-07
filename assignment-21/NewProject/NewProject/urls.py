"""NewProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views

from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    # path('', TemplateView.as_view(template_name="home.html")),
    # 
    path('admin/', admin.site.urls),
    # path('messages/', include('chat.urls')),
    path('add/', views.add, name='add'),
    path('', views.show, name='show'),
    path('update/<int:sid>', views.update, name='update'),
    path('delete/<int:sid>', views.delete, name='delete'),
    path('upload/',views.upload,name='upload'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)