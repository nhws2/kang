"""kang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import main.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.index,name='index'),
    path('read/<int:post_id>',main.views.read,name='read'),
    path('update/<int:post_id>/',main.views.update,name='update'),
    path('delete/<int:post_id>/',main.views.delete,name='delete'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('intro/', main.views.intro, name='intro'),
    path('notion/', main.views.notion, name='notion'),
    path('QnA/', main.views.QnA, name='QnA'),
    path('wholeLecture/', main.views.wholeLecture, name='wholeLecture'),
    path('localLecture/', main.views.localLecture, name='localLecture'),
    path('subjectLecture/', main.views.subjectLecture, name='subjectLecture'),
    path('wholeClass/', main.views.wholeClass, name='wholeClass'),
    path('localClass/', main.views.localClass, name='localClass'),
    path('subjectClass/', main.views.subjectClass, name='subjectClass'),
    path('lectureFunding/', main.views.lectureFunding, name='lectureFunding'),
    path('classFunding/', main.views.classFunding, name='classFunding'),
    path('fundingResult/', main.views.fundingResult, name='fundingResult'),
    path('createLec/', main.views.createLec, name='createLec'),
    path('createCla/', main.views.createCla, name='createCla'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
