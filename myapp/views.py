from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import viewsets
from rest_framework import status
from  rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from  rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from .customauth import CustomAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throtlling import DemoRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from .paginations import MyPageNumberPagination,MyLimitPagination



class SingerViewset(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
    
    
class SongViewset(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer



class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyLimitPagination
    # filter_backends=[OrderingFilter]
    # search_fields=['^city']
    # authentication_classes = [SessionAuthentication]
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes=[AnonRateThrottle,DemoRateThrottle]
    
    # python manage.py drf_create_token username(command to ganerate token)

class StudentViewset(viewsets.ViewSet):
    def list(self, request):
        try:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  

    def retrieve(self, request, pk=None):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    


    def create(self, request):
        try:
            serializer = StudentSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Successfully created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
  

    def update(self, request, pk=None):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data updated successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
   

    def partial_update(self, request, pk=None):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data updated successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
    def delete(self, request,pk=None):
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
        
            return Response({'msg':'data deleted successfully'})
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.filter(roll__lt=100)
    serializer_class=StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Create your views here.
def single_st(request):
    st_data=Student.objects.get(id=1)
    serialize_obj=StudentSerializer(st_data)
    json_data=JSONRenderer().render(serialize_obj.data)
    return HttpResponse(json_data,content_type="application/json")


def all_st(request):
    st_data=Student.objects.all()
    serialize_obj=StudentSerializer(st_data,many=True)
    json_data=JSONRenderer().render(serialize_obj.data)
    return HttpResponse(json_data,content_type="application/json")


@csrf_exempt
def st_create(request):
    if request.method == 'POST':
        jsondata=request.body
        stem=io.BytesIO(jsondata)
        pythondata=JSONParser().parse(stem)
        serialize_obj=StudentSerializer(data=pythondata)
        if serialize_obj.is_valid():
            serialize_obj.save()
            msg={'msg':'data created'}
            jsondata=JSONRenderer().render(msg)
            return HttpResponse(jsondata,content_type='application/json')
        jsondata=JSONRenderer().render(serialize_obj.errors)
        return HttpResponse(jsondata,content_type='application/json')
        
@csrf_exempt       
def st_update(request):
    if request.method=='PUT':
        jsondata=request.body
        steam=io.BytesIO(jsondata)
        pythondata=JSONParser().parse(steam)
        id=pythondata.get('id')
        st_obj=Student.objects.get(id=id)
        serialize_obj=StudentSerializer(st_obj,data=pythondata,partial=True)
        if serialize_obj.is_valid():
            serialize_obj.save()
            res={'msg':'data updated successfully'}
            jsondata=JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
        json_data=JSONRenderer().render(serialize_obj.errors)
        return HttpResponse(json_data,content_type="application/json")
    
@csrf_exempt     
def st_delete(request):
    json_data=request.body
    stream=io.BytesIO(json_data)
    pythondata=JSONParser().parse(stream )
    id=pythondata.get('id')
    stu=Student.objects.get(id=id)
    stu.delete()
    
    response={'msg':'data deleted successfully'}
    # json_data=JSONRenderer().render(response)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(response,safe=False)

@api_view()
def st_get_api(request):
    if request.method == 'GET':
        stu_data=Student.objects.all()
        seialize_obj=StudentSerializer(stu_data,many=True)
        return Response(seialize_obj.data)
    
@api_view(['POST'])
def st_post_api(request):
    if request.method == 'POST':
        jsondata=request.data
        serilize_obj=StudentSerializer(data=jsondata)
        if serilize_obj.is_valid():
            serilize_obj.save()
            return Response({'msg':'data created successfully'})
        return Response(serilize_obj.errors)