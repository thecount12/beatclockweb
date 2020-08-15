from django.shortcuts import render
from book.models import Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BookLisView(ListView):
    model = Book
    paginate_by = 10
    # queryset = Post.objects.order_by('-created')
    # or
    #
    # class Meta:
    #     ordering = ['-created']


class BookDetailView(DetailView):
    model = Book
