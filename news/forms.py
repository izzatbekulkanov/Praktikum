from django import forms
from .models import Contact, News

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
class NewsForm(forms.ModelForm):
    class Meta:
        model = News  # News modelini foydalanamiz
        fields = ('title', 'body', 'image', 'category', 'status')  # Barcha maydonlarni o'zgartirishga ruxsat beramiz
class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, label='Category Name')