from django import forms
from post.models import News, Posts


class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class PostsDetailForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'