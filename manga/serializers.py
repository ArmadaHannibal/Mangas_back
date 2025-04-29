from rest_framework import serializers
from .models import Manga, Commentaire, Favories, Vue
from django.contrib.auth.models import User  # ou from .models import User si vous avez défini votre propre modèle User

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'

class CommentaireMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

class FavoryMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favories
        fields = '__all__'

class VueMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vue
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_image')  # Spécifiez les champs que vous souhaitez sérialiser/désérialiser
