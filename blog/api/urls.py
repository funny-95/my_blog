from rest_framework import routers
from django.conf.urls import url, include
from .admin_view import CategoryViewSet
from .client_view import AuthView, UserArticlesView, CategoryView


admin_router = routers.DefaultRouter()
admin_router.register(r"categories", CategoryViewSet, base_name="test")

urlpatterns = [
    url(r"^admin/", include(admin_router.urls)),
    url(r"^auth/", AuthView.as_view(), name="auth"),
    url(r"^user_articles/", UserArticlesView.as_view(), name="user_articles"),
    url(r"^categories/", CategoryView.as_view(), name="categories")
]
