from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from pool.models import Upload


class HomeView(LoginRequiredMixin, View):
    template_name = 'core/home.html'

    def get(self, request):
        context = {}
        if request.user.is_staff:
            context['objects'] = Upload.objects.all()
        else:
            context['objects'] = Upload.objects.filter(user=request.user)
        return render(request, self.template_name, context)
