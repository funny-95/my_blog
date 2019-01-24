from rest_framework.views import APIView
from ..serializers.client import UserSerializer
from ..models import User


class AuthView(APIView):

    def post(self, request):
        """
        用户注册登录
        """
        pass


class UserArticlesView(APIView):
    def post(self, request):
        """
        创建文章
        """
        pass

    def get(self, request):
        """
        列出某类别下所有文章
        """
        pass


class CategoryView(APIView):
    def get(self, request):
        """
        类别列表
        """
        pass
