from django.http import Http404
from django.contrib.auth.models import User
from . import models


def check_topic_owner(request, value):
    """Проверяет связан ли пользователь с текущей темой"""
    if value.owner != request.user:
        raise Http404


lst_articles = [{'title': 'Название статьи 1', 'text': 'Содержание стати 1'},
                {'title': 'Название статьи 2', 'text': 'Содержание стати 2'},
                {'title': 'Название статьи 3', 'text': 'Содержание стати 3'},
                ]


def load_articles(owner=1):
    # title
    # text
    # owner
    author = User.objects.get(id=owner)
    for el in lst_articles:
        new_article = models.Article(title=el['title'], text=el['text'], owner=author)
        new_article.save()


