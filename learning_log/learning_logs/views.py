from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from . import logic
from . import models
from .forms import TopicForm, EntryForm, FeedbackForm


def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Страница со всеми созданными темами данного пользователя"""
    topics = models.Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Страница конкретной темы со всеми вложениями"""
    topic = models.Topic.objects.get(id=topic_id)
    # Проверка того, что тема принадлежит текущему пользователю.
    logic.check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Страница для создания новых тем другими пользователями"""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            n_topic = form.save(commit=False)
            n_topic.owner = request.user
            n_topic.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Добавляет новую запись для конкретной темы"""
    topic = models.Topic.objects.get(id=topic_id)
    logic.check_topic_owner(request, topic)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Редактируем запись по конкретной теме"""
    entry = models.Entry.objects.get(id=entry_id)
    topic = entry.topic
    logic.check_topic_owner(request, topic)
    if request.method != 'POST':
        # Данные не редактировались; открывается форма со старой записью.
        form = EntryForm(instance=entry)
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'topic': topic, 'form': form, 'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)


def articles(request):
    """Страница со всеми созданными темами данного пользователя"""
    articles = models.Article.objects.order_by('-date_added')
    context = {'articles': articles}
    return render(request, 'learning_logs/articles.html', context)


def article(request, article_id):
    """Показываем содержание статьи"""
    article = models.Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'learning_logs/article.html', context)


def feedback(request):
    error = ''
    admin = False
    if request.method != 'POST':
        form = FeedbackForm()
        if request.user.id == 1:
            admin = True
    else:
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:index')
        error = 'Вы ввели некорректные данные'
    context = {'form': form, 'error': error, 'admin': admin}
    return render(request, 'learning_logs/feedback.html', context)

@login_required
def feedbacks(request):
    feedbacks = feedbacks = models.Feedback.objects.order_by('-date_added')
    if request.user.id != 1:
        raise Http404
    context = {'feedbacks': feedbacks}
    return render(request, 'learning_logs/feedbacks.html', context)
