from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import markdown2
from django.urls import reverse
from random import randint

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    entry = util.get_entry(title)
    if (entry == None):
        return render(request, "encyclopedia/error.html", {
            "name": title
        })
    else:
        converted_entry = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry.html", {
            "entry": converted_entry,
            "title": title
        })

def edit(request, title):
    entry = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "entry": entry  
    })


def new_page(request):
    return render(request, "encyclopedia/new_page.html")

def overlap_error(request):
    return render(request, "encyclopedia/overlap_error.html")

def add_page(request):
    
    if(request.method == "POST"):
        title = request.POST.get("title", False)
        if (util.get_entry(title) != None):
            return HttpResponseRedirect(reverse("overlap_error"))
        else:
            path = "entries/" + title + ".md"
            md_file = open(path, "w")
            md_file.write(request.POST.get("content", False))
            return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))

def confirm_edit(request, title):
    
    if(request.method == "POST"):
        path = "entries/" + title + ".md"
        md_file = open(path, "w")
        md_file.write(request.POST.get("content", False))
        return HttpResponseRedirect(reverse('page', args=(title,)))
    return HttpResponseRedirect(reverse("index"))

def search(request):
    query = request.GET.get("q")
    return search_title(request, query)
    

def search_title(request, title):
    entry = util.get_entry(title)
    if (entry == None):
        page_list = []
        pages = util.list_entries()
        for page in pages:
            if title in page:
                page_list.append(page)
        return render(request, "encyclopedia/search.html", {
            "entries": page_list,
            "title": title
        })
    else:
        converted_entry = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry.html", {
            "entry": converted_entry,
            "title": title
        })
    
def random(request):
    entries = util.list_entries()
    int = randint(0, len(entries) - 1)
    title = entries[int]
    return page(request, title)
