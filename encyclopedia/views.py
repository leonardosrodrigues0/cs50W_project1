from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from markdown2 import Markdown
import random
from . import util


# Validor to check if the entry exists
def validate_entry(name):
    namelower = name.lower()

    for entry in util.list_entries():
        if namelower == entry.lower():
            raise ValidationError(
                gettext_lazy('A page for "%(name)s" already exists'),
                params={'name': name},
            )


# Form for new pages
class NewEntryForm(forms.Form):
    name = forms.CharField(
        label = "",
        widget = forms.TextInput(attrs={'placeholder':'Page name'}),
        max_length = 25,
        validators = [validate_entry]
    )

    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder':'Content'})
    )


# Form to edit pages
class EditEntryForm(forms.Form):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder':'Content'})
    )


# Returns HTML content for entry
def content(entry):
    return Markdown().convert(util.get_entry(entry))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    entries = util.list_entries()

    if entry in entries:
        return render(request, "encyclopedia/entries.html", {
                "entry": entry,
                "content": content(entry)
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Page doesn't exist"
        })


def search(request):
    q = request.GET.get("q")
    qlower = q.lower()
    results = []

    for entry in util.list_entries():
        entrylower = entry.lower()

        if qlower == entrylower:
            return HttpResponseRedirect(reverse("entry", args = (entry,)))

        elif qlower in entrylower:
            results.append(entry)

    return render(request, "encyclopedia/search.html", {
        "q": q,
        "results": results
    })


def newpage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            util.save_entry(entry, content)
            return HttpResponseRedirect(reverse("entry", args = (entry,)))
        else:
            return render(request, "encyclopedia/newpage.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/newpage.html", {
            "form": NewEntryForm()
        })


def editpage(request, entry):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(entry, content)
            return HttpResponseRedirect(reverse("entry", args = (entry,)))
        else:
            return render(request, "encyclopedia/editpage.html", {
                "form": form,
                "entry": entry
            })
    else:
        form = EditEntryForm()
        form.fields["content"].initial = util.get_entry(entry)

        return render(request, "encyclopedia/editpage.html", {
            "form": form,
            "entry": entry
        })


def randompage(request):
    entry = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry", args = (entry,)))
