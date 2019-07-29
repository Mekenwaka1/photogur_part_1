from django.http import HttpResponse
from django.shortcuts import render

def pictures(request):
    context = {'Sea Power': "http://bitmakerlabs.s3.amazonaws.com/photogur/wave.jpg", 
    'The old church on the coast of White sea': "http://bitmakerlabs.s3.amazonaws.com/photogur/house.jpg"} 
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)