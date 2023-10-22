from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

def index(request, id):
    ls = TodoList.objects.get(id=id)
     
    {"save":["save"], "c1":["clicked"]}
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
              if response.POST.get("c" + str(item.id)) == 'clicked':
                item.complete = True
            else: 
                item.complete = False

                item.save()

    elif response.POST.get("newItem"):
         txt = response.POST.get("new")

         if len(text) >2:
            ls.item_set.create(text=text, complete=False)
         else:
            print("invalid")    

    return render(response, "polls/list.html",{"ls":ls})


def home(response):
    return render(response, "polls/home.html",{}) 

def create(response):
    if response.method == "POST":
       form = CreateNewList(response.POST)

       if form.is_valid():
          n = form.cleaned_data["name"]
          t = TodoList(name=n)
          t.save()

    return HttpResponseRedirect
#else:
    form = CreateNewList()
    return render(response, "polls/create.html",{"form":form}) 


