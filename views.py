from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('emp.html')
  return HttpResponse(template.render())