"""
URL configuration for sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from rest_framework.authtoken.views import ObtainAuthToken
router.register('api/batches',views.BatchView,basename="batches")
router.register('api/waitinglists',views.WaitingListView,basename="waiyinglists")
router.register('api/addedstudents',views.AddedView,basename="addedstudents")




urlpatterns = [
    path('admin/', admin.site.urls),
    
     path('batch/<int:batch_id>/add-student/', views.AddStudentToBatch.as_view(), name='add-student-to-batch'),
     path('api/token/',ObtainAuthToken.as_view()),
      path('register/',views. StudentRegistrationView.as_view(), name='student-registration'),
    
    
    
     
]+router.urls
