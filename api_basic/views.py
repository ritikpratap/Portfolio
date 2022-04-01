from django.shortcuts import render
from rest_framework import generics, filters
from .forms import DictionaryForm

def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'oxf.html', {'form': form, 'search_result': search_result})