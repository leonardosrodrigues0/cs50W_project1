from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from markdown2 import Markdown

from . import util


def content(entry):
    return Markdown().convert(util.get_entry(entry))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    return render(request, f"encyclopedia/entries.html", {
            "entry": entry,
            "content": content(entry)
        })


def search(request):
    q = request.GET.get("q")
    qlower = q.lower()
    results = []

    for entry in util.list_entries():
        entrylower = entry.lower()

        if qlower == entrylower:
            return HttpResponseRedirect(reverse("entry", args=(entry,)))

        elif qlower in entrylower:
            results.append(entry)

    return render(request, f"encyclopedia/search.html", {
        "q": q,
        "results": results
    })

