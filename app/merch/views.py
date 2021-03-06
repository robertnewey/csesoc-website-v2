from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm,Textarea
from django.core.mail import send_mail
from models import Hoodie
import httplib
import urllib

class HoodieForm(ModelForm):
   class Meta:
      model = Hoodie
      exclude = ('payment_status',)

def hoodies(request):
    if request.method == 'POST': # form submitted
      form = HoodieForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect("https://www.csesoc.unsw.edu.au/finance/20140002/8771d81806d361be65c066d71038d1d7")
    else:
      form = HoodieForm() # unbound form
    return render_to_response('merch/hoodies.html', {'form' : form}, context_instance=RequestContext(request))