from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Entry


class EntryView(generic.DetailView):
    model = Entry
    template_name = 'blog/entry.html'
    # entry = get_object_or_404(Entry, slug=slug)
    # context = {'entry': entry}
    # return render(request, 'blog/entry.html', context)


class ArchiveYearView(generic.ListView):
    model = Entry
    template_name = 'blog/archive-year.html'


class ArchiveMonthView(generic.ListView):
    model = Entry
    template_name = 'blog/archive-month.html'


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        return Entry.objects.order_by('-date_published')[:5]
