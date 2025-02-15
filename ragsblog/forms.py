from django import forms
from .models import Image, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "text",
        ]

class ImageForm(forms.Form):
    image = forms.ImageField(
        label="Image",
        required=False
    )

    class Meta:
        model = Image
        fields = ["image",]