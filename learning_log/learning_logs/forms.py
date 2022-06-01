from django.forms import ModelForm, TextInput, Textarea

from .models import Topic, Entry, Feedback

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': TextInput(attrs={
                "placeholder": "Введите название темы",
            }),
        }


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': Textarea(attrs={
                'cols': 100,
                "placeholder": "Введите текст записи",
            },),
        }


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'comment']
        labels = {'name': 'Имя:', 'email': 'Email:', 'phone': 'Телефон:', 'comment': 'Сообщение:'}
        widgets = {
            'name': TextInput(attrs={
                'name': 'name',
                'type': 'text',
                'id': 'name',
                'placeholder': 'Введите Ваше имя',
                'autofocus': 'on',
        }, ),
            'email': TextInput(attrs={
                'name': 'email',
                'type': 'text',
                'id': 'email',
                'placeholder': 'Введите адрес Вашей почты',
        }, ),
            'phone': TextInput(attrs={
                'name': 'phone',
                'type': 'tel',
                'id': 'phone',
                'placeholder': 'Введите номер телефона. Образец: 375337005500',
                'pattern': '375[0-9]{9}'
        }, ),
            'comment': Textarea(attrs={
                'name': 'comment',
                'id': 'comment',
                'placeholder': 'Текст сообщения',
        }, ),
        }
