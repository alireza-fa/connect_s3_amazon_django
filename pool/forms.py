from django import forms
from .models import Upload


class UploadImageForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image.size > 500000:
            raise forms.ValidationError('you can just upload file less than 0.5m')
        return image

    @staticmethod
    def save(user, image):
        instance = Upload.objects.create(user=user, image=image)
        return instance
