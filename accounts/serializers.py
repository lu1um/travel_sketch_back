from rest_framework import serializers
from django.contrib.auth import get_user_model

from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=10)
    picture = serializers.ImageField(use_url=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['picture'] = self.validated_data.get('picture', '')
        return data_dict