from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template import Template, Context

from .models import CryptoModel, Publisher
from .forms import ContractForm


import datetime

# Create your views here.

def review_detail(request, year, month, day):
    print('%s %s %s' % (year, month, day))
    return HttpResponse("Good.")

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context(({'current_date': now })))

    return HttpResponse(html)

def display_header(request):

    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unkown'
    
    values = request.META.items()

    html = []

    for k,v in values:
        html.append('<tr><td>%s<td>%s</td></td></tr>' %(k,v))

    return HttpResponse("<table>%s</table>" %('\n'.join(html)))


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours(s), it will be %s</body></html>" % (offset, dt)

    return HttpResponse(html)

class PublisherList(ListView):
    template_name = "publisher_list.html"
    model = Publisher

class PublisherDetail(DetailView):
    model = Publisher
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()    

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['publisher_list'] = Publisher.objects.all()
        return context

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ChatView(TemplateView):
    template_name = 'chat.html'

class CryptoListView(ListView):
    template_name = 'cryptocurrency.html'
    
    model = CryptoModel    

class CryptoDetailView(DetailView):
    template_name = 'cryptocurrency_detail.html'

    model = CryptoModel

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    errors = []

    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a serach term')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            publisher_name = request.GET['q']
            publisher = Publisher.objects.filter(name=publisher_name)

            return render(request, 'search_result.html',
            {
                'publisher': publisher, 
                'query':publisher_name
            })
        
    return render(request, 'search_form.html',
    {
        'errors': errors
    })

def contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'han@gridwiz.com'),
                ['han@gridwiz.com'],
            )
            return HttpResponseRedirect('/contract/thanks/')
    else:
        form = ContractForm(
            initial = {
                'subject': 'I love your site!'
            }
        )
    
    return render(request, 'contract_form.html', {'form':form})
    