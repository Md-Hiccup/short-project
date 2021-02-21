from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from .models import Books
from .form import BooksForm, UpdateBooksForm

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello world!</h1>')
    book_list = Books.objects.all()
    return render(request, 'component/home.html', {'book_list': book_list})

def book_detail_view(request, book_id, *args, **kwargs):
    try:
        obj = Books.objects.get(id=book_id)
    except:
        raise Http404
    return HttpResponse(f'<h1>Book name: "{obj.name}" Author: "{obj.author}"</h1>')

def book_create_view(request, *args, **kwargs):
    form = BooksForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BooksForm()
    return render(request, 'component/form.html', context={'form': form})

def book_update_view(request, book_id, *args, **kwargs):
    try:
        obj = Books.objects.get(id=book_id)
    except:
        raise Http404
    form = UpdateBooksForm(request.POST or None)
    if form.is_valid():
        obj.name = form.cleaned_data.get('name')
        obj.save()
        return redirect(home_view)
    return render(request, 'component/form.html', context={'form': form})

def book_delete_view(request, book_id, *args, **kwargs):
    try:
        obj = Books.objects.get(id=book_id)
    except:
        raise Http404
    # obj.delete()
    print(obj)
    return redirect(home_view)

