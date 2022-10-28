from rest_framework import serializers
from article.models import Article

# 방법 1
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']
        # fields = '__all__'
        
# 방법 2        
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
        
#         extra_kwargs = {
#             'author': {'read_only': True}
#         }


# 방법 3
# class ArticleSerializer(serializers.ModelSerializer):
#     author = serializers.SerializerMethodField()
    
#     def get_user(self, obj):
#         return obj.author.username
    
#     class Meta:
#         model = Article
#         fields = '__all__'
        
#         extra_kwargs = {
#             'author': {'read_only': True}
#         }