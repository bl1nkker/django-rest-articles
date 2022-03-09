from django.urls import path
from .views import ArticleDetailsAPIView, GenericAPIView, article_details, article_list, ArticleAPIView

urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<int:pk>', article_details)

    path('articles/', ArticleAPIView.as_view()),
    # path('articles/<int:pk>', ArticleDetailsAPIView.as_view())

    path('articles/<int:id>', GenericAPIView.as_view()),
]