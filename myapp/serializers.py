from rest_framework import serializers
from .models import *

# validators
# def start_with_r(value):
#     if value[0].lower() !='r':
#         raise serializers.ValidationError('Name should staet with R')



# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100,validators=[start_with_r])
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=40)
    
    
#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)
    
    
#     def update(self, instance, validated_data):
#         print(validated_data)
#         instance.name=validated_data.get('name',instance.name)
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
    
    
#     #field level validation
#     def validate_roll(self,value):
#         if value >=200:
#             raise serializers.ValidationError('seat full')
#         return value
    
    
#     #object level validation
#     def validate(self,data):
#         print(data)
#         nm=data.get('neme')
#         ct=data.get('city')
#         if nm == 'vijay' and ct != 'valshad':
#             raise serializers.ValidationError('City must be Valshad')
#         return data
    
    


class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    class Meta:
        model=Student
        fields='__all__'
        # read_only_fields=['name']
        # extra_kwargs={'name':{'read_only':True}}
        
     #field level validation
    # def validate_roll(self,value):
    #     if value >=200:
    #         raise serializers.ValidationError('seat full')
    #     return value
    
    
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','duration','singer']    
    
class SingerSerializer(serializers.ModelSerializer):
    # song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    # song=serializers.StringRelatedField(many=True,read_only=True)
    songby=SongSerializer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields=['id','name','gender','songby']
        


