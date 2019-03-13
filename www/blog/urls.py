from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'archive/<int:year>/',
        views.ArchiveYearView.as_view(),
        name='archive_year'),
    path(
        'archive/<int:year>/<int:month>/',
        views.ArchiveMonthView.as_view(),
        name='archive_month'),
    path(
        'entry/<int:year>/<int:month>/<slug:slug>/',
        views.EntryView.as_view(),
        name='entry')
]
