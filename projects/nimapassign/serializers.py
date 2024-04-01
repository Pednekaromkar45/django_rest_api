from rest_framework import serializers
from .models import Client, Project, User
from rest_framework import serializers
from .models import Client

       
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name']
     
class ProjectSerializer(serializers.ModelSerializer):
    
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = Project
        fields = ['id', 'project_name','created_at','created_by','client_name']
        

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'client_name','created_at','created_by']        

class ClientDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'client_name','created_at','created_by','updated_at']  

class ClientDetailSerializerget(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)
    class Meta:
        model = Client
        fields = ['id', 'client_name','created_at','created_by','updated_at','projects']          



class ProjectSerializer_for_post(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'user']

    def create(self, validated_data):
        users_data = validated_data.pop('user', [])
        project = Project.objects.create(**validated_data)
        project.user.set(users_data)
        return project