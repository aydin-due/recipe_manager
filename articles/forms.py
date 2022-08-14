from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if title.lower().strip() == 'the office':
            raise forms.ValidationError('title already used')
        return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return cleaned_data