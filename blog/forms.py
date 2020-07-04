from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    publish_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'image', 'content', 'draft', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError('This title has already been used. Please try again!')
        return title

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')