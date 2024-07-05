from django.forms import ModelForm
from django import forms 
from projects.models import Project , Review


class projectform(ModelForm):
    class Meta:
        model = Project
        fields = ["title","description", "featured_image", "demo_link", "source_link", "tags"]
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(projectform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class':'input' ,})


class reviewform(ModelForm):
    class Meta:
        model = Review
        fields = ['vote', 'body']

        labels = {
            'vote':'Please vote for project',
            'body': 'Write your comments here'
        }

    def __init__(self, *args, **kwargs):
        super(reviewform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})