from django.contrib import admin
from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


#creating router object
router=DefaultRouter()

#router register
router.register('studentapi',StudentModelViewset,basename='student')
router.register('singer',SingerViewset,basename='singer')
router.register('song',SongViewset,basename='song')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('',include(router.urls)),
    path('api/', include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refreshtoken'),
    path('varifytoken/',TokenVerifyView.as_view(),name='verifytoken'),
    
]
