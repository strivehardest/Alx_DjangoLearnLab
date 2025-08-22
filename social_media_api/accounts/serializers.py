from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source="followers.count", read_only=True)
    following_count = serializers.IntegerField(source="following.count", read_only=True)

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name",
            "bio", "profile_picture", "followers_count", "following_count",
        ]
        read_only_fields = ["id", "followers_count", "following_count"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    token = serializers.SerializerMethodField()  # Dynamically include token

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password", "token"]

    def create(self, validated_data):
        # ✅ Explicitly use get_user_model().objects.create_user
        user = get_user_model().objects.create_user(**validated_data)
        # ✅ Explicitly create token
        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid username or password.")

        token, _ = Token.objects.get_or_create(user=user)
        attrs["user"] = user
        attrs["token"] = token.key
        return attrs
