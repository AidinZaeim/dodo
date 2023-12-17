from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# -------------------------------------------------------------------------------------------------------------------------------
class EnhancedTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...
        return token
# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'firstName', 'lastName', 'password']

# -------------------------------------------------------------------------------------------------------------------------------
class CodeValidationSerializers(serializers.ModelSerializer):
    email = serializers.CharField()
    code = serializers.CharField()
    class Meta:
        model = User
        fields = ['email', 'code']
# -------------------------------------------------------------------------------------------------------------------------------
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'firstName', 'lastName', 'role','image']
# -------------------------------------------------------------------------------------------------------------------------------
class PasswordChangeRequestSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    class Meta:
        model = User
        fields = [ 'email']
# -------------------------------------------------------------------------------------------------------------------------------
class PasswordChangeSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    code = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = [ 'email', 'code','password']
# -------------------------------------------------------------------------------------------------------------------------------
class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image',)
        partial = True
# -------------------------------------------------------------------------------------------------------------------------------
