from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from article.models import Article
from article.serializers import ArticleSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True).data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        article = ArticleSerializer(data=request.data)
        # if article.is_valid():
        #     article.save(author=request.user)
        #     return Response(article.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(article.errors, status=status.HTTP_400_BAD_REQUEST)
        
        article.is_valid(raise_exception=True)
        article.save(author=request.user)
        return Response(article.data)