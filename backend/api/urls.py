from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views as api_views

urlpatterns = [
    path('user/token/',api_views.myTokenObtainPairView.as_view()),
    path('user/token/refresh/',TokenRefreshView.as_view()),
    path('user/register/',api_views.RegisterView.as_view()),
    path('user/profile/<user_id>/',api_views.ProfileView.as_view()),

    path('post/category/list/',api_views.CategoryListAPIView.as_view()),
    path('post/category/posts/<category_slug>',api_views.PostCategoryListAPIView.as_view()),

]
