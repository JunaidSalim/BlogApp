from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api import views as api_views

urlpatterns = [
    # User API Endpoints
    path('user/token/',api_views.myTokenObtainPairView.as_view()),
    path('user/token/refresh/',TokenRefreshView.as_view()),
    path('user/register/',api_views.RegisterView.as_view()),
    path('user/profile/<user_id>/',api_views.ProfileView.as_view()),

    # Post API Endpoints
    path('post/category/list/',api_views.CategoryListAPIView.as_view()),
    path('post/category/posts/<category_slug>',api_views.PostCategoryListAPIView.as_view()),
    path('post/lists/',api_views.PostListAPIView.as_view()),
    path('post/detail/<slug>',api_views.PostDetailsAPIView.as_view()),
    path('post/like-post/',api_views.LikePostAPIView.as_view()),
    path('post/comment-post/',api_views.PostCommentAPIView.as_view()),
    path('post/bookmark-post/',api_views.BookmarkPostAPIView.as_view()),
    
    # Dashboard API Endpoints
    path('author/dashboard/stats/<user_id>/',api_views.DashboardStats.as_view()),
    path('author/dashboard/post-list/<user_id>/',api_views.DashboardPostLists.as_view()),
    path('author/dashboard/comment-list/<user_id>/',api_views.DashboardCommentsLists.as_view()),
    path('author/dashboard/notification-list/<user_id>/',api_views.DashboardNotificationLists.as_view()),
    path('author/dashboard/notification-mark-as-seen/',api_views.DashboardMarkNotificationAsSeen.as_view()),
    path('author/dashboard/reply-comment/',api_views.DashboardReplyCommentAPIView.as_view()),
    path('author/dashboard/create-post/',api_views.DashboardPostCreateAPIView.as_view()),
    path('author/dashboard/update-post/<user_id>/<post_id>/',api_views.DashboardPostEditAPIView.as_view()),
    
]
