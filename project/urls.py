from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from blog import views

router = routers.DefaultRouter()
router.register('blog', views.BlogViewSet, basename='blog')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/viewset/', include(router.urls)),
    path('api/generics/blog/', views.BlogListCreateView.as_view()),
    path('api/generics/blog/<int:pk>/', views.BlogRetrieveUpdateDeleteView.as_view()),
    path('api/views/blog/', views.BlogViewListCreate.as_view()),
    path('api/views/blog/<int:pk>/', views.BlogViewDetail.as_view()),
    path('api/function/blog/', views.blog_list_create),
    path('api/function/blog/<int:pk>/', views.blog_detail),

]
