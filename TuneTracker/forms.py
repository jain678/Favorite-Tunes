from django import forms
from .models import Song,Artist

class songForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist','album_cover']
        # widgets = {
        #     'title':forms.Textarea(attrs={"rows":1,"style":"border-radius:1rem"}),
        #     'artist':forms.Textarea(attrs={"rows":1,"style":"border-radius:1rem"})
        # }

class artistForm(forms.ModelForm):
    class Meta:
        model =Artist
        fields = ['name','age','profile_pic']
        # widgets = {
        #     'name':forms.Textarea(attrs={"rows":1,"style":"border-radius:1rem"}),
        #     'age':forms.Textarea(attrs={"rows":1,"style":"border-radius:1rem"})
        # }