from django.urls import path
from .views import *
urlpatterns = [
    path('', AListView.as_view(), name='home' ),
    path('<int:pk>/', ADetailView.as_view(), name='article_detail' ),
    path('<int:pk>/edit/', AUpdateView.as_view(), name='article_edit' ),
    path('<int:pk>/delete/', ADeleteView.as_view(), name='article_delete' ),
    path('new/', ACreatView.as_view(), name='article_new')
]