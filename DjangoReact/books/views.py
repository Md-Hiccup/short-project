from json.encoder import JSONEncoder
from django.http import HttpResponse, Http404
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Books
from .form import BooksForm, UpdateBooksForm

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello world!</h1>')
    book_list = Books.objects.all()
    # return render(request, 'component/home.html', {'book_list': book_list})
    return render(request, 'pages/home.html', context={'book_list': book_list}, status=200)

def book_detail_view(request, book_id, *args, **kwargs):
    data = {
        'id': book_id
    }
    status = 200
    try:
        obj = Books.objects.get(id=book_id)
        data['name'] = obj.name
        data['author'] = obj.author
        data['description'] = obj.description
    except:
        data['message'] = 'Not Found'
        status = 404
        # raise Http404
    # return HttpResponse(f'<h1>Book name: "{obj.name}" Author: "{obj.author}"</h1>')
    return JsonResponse(data, status=status)

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

def book_list(request, *args, **kwargs):
    blist = Books.objects.all()
    books = [{"id": x.id, "name": x.name, "author": x.author, "description":x.description} for x in blist]
    data = {
        "response": books
    }
    return JsonResponse(data)