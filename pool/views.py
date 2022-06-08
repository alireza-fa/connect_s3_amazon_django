from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UploadImageForm
from .tasks import delete_object_task
from .models import Upload


class UploadImageView(LoginRequiredMixin, View):
    template_name = 'pool/upload.html'
    class_form = UploadImageForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.class_form()})

    def post(self, request):
        form = self.class_form(files=request.FILES)
        if form.is_valid():
            # t = threading.Thread(target=form.save, args=(request.user, form.cleaned_data.get('image')))
            # t.start()
            form.save(request.user, form.cleaned_data.get('image'))
            # upload_image_task.delay([request.user.id], [form.cleaned_data.get('image')])
            # messages.success(request, 'your image upload a few moment later.')
            messages.success(request, 'your image uploaded successfully.')
            return redirect('core:home')
        return render(request, self.template_name, {"form": form})


class DeleteObjectView(LoginRequiredMixin, View):

    def get(self, request, pk):
        if request.user.is_staff:
            file = get_object_or_404(Upload, pk=pk)
        else:
            file = get_object_or_404(Upload, pk=pk, user=request.user)
        delete_object_task.delay(file.image.name)
        file.delete()
        messages.success(request, 'your object delete soon.')
        return redirect('core:home')
