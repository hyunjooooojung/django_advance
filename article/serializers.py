from rest_framework import serializers
from article.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = '__all__'