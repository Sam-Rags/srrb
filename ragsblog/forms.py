from django import forms
from .models import Image, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
        ]

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    class Meta:
        model = Image
        fields = ("image",)