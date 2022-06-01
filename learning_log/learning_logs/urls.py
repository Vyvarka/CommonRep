from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    # Список всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для создания новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для создания новой записи
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # Страница для редактирования записей
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    # Список новостей
    path('articles/', views.articles, name='articles'),
    # Содержание конкретной новости
    path('articles/<int:article_id>', views.article, name='article'),
    # Обратная связь
    path('feedback/', views.feedback, name='feedback'),
    # Обратная связь. Информация для администратора
    path('feedbacks/', views.feedbacks, name='feedbacks'),
]
