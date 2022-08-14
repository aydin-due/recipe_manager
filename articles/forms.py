from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'the office':
    #         raise forms.ValidationError('title already used') #errorlist
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'the office':
            self.add_error('title', 'title already used') #errorlist
            # raise forms.ValidationError('title already used') #errorlist nonfield
        if 'office' in content or 'office' in title.lower():
            self.add_error('content', 'content cannot contain office')
            raise forms.ValidationError('office is not allowed')
        return cleaned_data