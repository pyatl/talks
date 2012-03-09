# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def hello(request):
    return render_to_response('hello.html', 
            context_instance=RequestContext(request, {
                'greeting': 'Guten Abend'
            }))

