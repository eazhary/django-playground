from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
#from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
from .models import Album, Song
from .forms import EmailForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    albums = Album.objects.all()
    return render(request, "polls/index.html", {"albums": albums})


# Create your views here.

class Index(ListView):
    model = Album


@method_decorator(login_required, name='dispatch')
class Detail(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        context['songs'] = Song.objects.filter(album=self.get_object().id)
        return context


class NewAlbum(CreateView):
    model = Album
    fields = ['title','year','artist']
    success_url = reverse_lazy('index2')
#    form_class = EmailForm

class EmailView(FormView):
    template_name = 'polls/email.html'
    form_class = EmailForm
    success_url = reverse_lazy('index2')
    def form_valid(self, form):
        if 'cancel' in self.request.POST:

            return HttpResponseRedirect(self.get_success_url())
        return super(EmailView, self).form_valid(form)