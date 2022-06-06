from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Article, Comment



def article_list_or_create(request):
    pass


def article_detail_or_update_or_delete(request, article_pk):
    pass


def like_article(request, article_pk):
    pass


def create_comment(request, article_pk):
    pass


def comment_update_or_delete(request, article_pk, comment_pk):
    pass


def search(request):
    pass


def news_list_or_create(request):
    pass