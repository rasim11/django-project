from django.shortcuts import render

def home(request):
    return  render(request,'base.html')
# Create your views here.
def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search':search,
    }
    return render(request,'my_app/new_search.html',stuff_for_frontend)