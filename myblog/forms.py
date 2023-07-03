from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Feedback, Comment, Post

class PostForm(forms.ModelForm):
    h1 = forms.CharField(widget=forms.TextInput())
    title = forms.CharField(widget=forms.TextInput())
    url = forms.SlugField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(required=False)
    tag = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Post
        fields = ['h1', 'title', 'url', 'description', 'content', 'image', 'tag']

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields  = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'raiting': 'Рейтинг',
        }

class SigUpForm(forms.Form):
    
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
        }),
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth

class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        })
    )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widget = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }