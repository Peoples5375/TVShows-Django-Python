from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show

def index(request):
    context={
        'allshows':Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    context={
        'allshows':Show.objects.all()
    }
    return render(request, 'new.html', context)

def newshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:

        show=Show.objects.create(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release_date"], desc = request.POST["desc"])
        return redirect(f'/shows2/{show.id}')

def shows2(request, id):
    context={
        'allshows':Show.objects.get(id=id)
    }
    return render(request, 'shows2.html', context)

def delete_show_on_list(request, id):
    c = Show.objects.get(id=id)
    c.delete()
    return redirect ('/')

def edit(request, id):
    context={
        'allshows':Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def edit_show(request, id):
    errors = Show.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        c = Show.objects.get(id=id)
        c.title = request.POST['title']   
        c.network = request.POST['network']   
        c.release_date = request.POST['release_date']
        c.desc = request.POST['desc']
        c.save()
        return redirect (f'/shows2/{id}')