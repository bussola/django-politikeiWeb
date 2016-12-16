from django.shortcuts import render_to_response

def index(request):    
    return render_to_response('politikando-django/FrontEndPolitikando/index.html', locals())
