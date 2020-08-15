from django.urls import path

from book.views import BookDetailView
from book.views import BookLisView

urlpatterns = [
    path('', BookLisView.as_view(), name='book-list'),
    path('<int:pk>', BookDetailView.as_view(), name='post-detail'),

]
