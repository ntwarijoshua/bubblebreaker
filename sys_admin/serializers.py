from rest_framework import serializers
from .models import SystemAdmin
class SystemAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAdmin
        fields = '__all__'
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(required = True, max_length = 100)
    first_name = serializers.CharField(required = True, max_length = 100)
    last_name = serializers.CharField(required = True, max_length = 100)
    email = serializers.EmailField(required = True, max_length = 100)
    password = serializers.CharField(required = True, min_length = 6, max_length = 100, write_only=True)
    is_staff = serializers.BooleanField(default= True)
    is_active = serializers.BooleanField(default=True)


    """
    validate the data before creation
    """
    def create(self, validated_data):
        return SystemAdmin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.first_name)
        instance.username = validated_data.get('username',instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.is_staff = validated_data.get('is_staff',instance.is_staff)
        instance.is_active = validated_data.get('is_active',instance.is_active)

        if validated_data.get('password',None):
            instance.set_password(validated_data.get('password'))

        instance.save()
        return instance
