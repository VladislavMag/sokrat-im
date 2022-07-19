from django.shortcuts import render
from .models import Link
from django.views.generic import ListView, CreateView


def home(request):
    return render(request, 'home/home.html')


class NewLinkView(CreateView, ListView):
    model = Link
    template_name = 'home/link.html'
    context_object_name = 'links'
    fields = ['link', 'title']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)

def about(request):
    return render(request, 'home/about.html')