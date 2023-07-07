from django.urls import path
from .views import *


urlpatterns =[
    path('single_student/',single_st,name='student'),
    path('all_student/',all_st,name='all_st'),
    path('stcreate/',st_create,name='stcreate'),
    path('stupdate/',st_update,name='stupdate'),
    path('stdelete/',st_delete,name='stdelete'),
    path('st_get_api/',st_get_api,name='st_get_api'),
    path('st_post_api/',st_post_api,name='st_post'),
    path('stu_list_gen/',StudentList.as_view(),name='stu_list_gen'),
    path('stu_create_gen/',StudentCreate.as_view(),name='stu_create_gen'),
    path('stu_retrieve_gen/<int:pk>',StudentRetrieve.as_view(),name='stu__retrieve_gen'),
    path('stu_update_gen/<int:pk>',StudentUpdate.as_view(),name='stu__update_gen'),
    path('stu_delete_gen/<int:pk>',StudentDestroy.as_view(),name='stu__destroy_gen'),
    
    

]