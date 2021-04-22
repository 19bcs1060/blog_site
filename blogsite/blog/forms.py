from django import forms
from .models import Blog
MAX_LENGTH= 240
class Create_form(forms.ModelForm):
   
    class Meta:
        model= Blog
        fields =['content_title', 'content']
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_LENGTH:
            raise forms.ValidationError("This form is not valid")
        return content