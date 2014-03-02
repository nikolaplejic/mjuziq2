from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from mjuziqmgr.models import Album
import calendar

def index(request):
  year = timezone.now().year
  months = range(1, timezone.now().month + 1)
  ctx = {
    "albums_by_month": {},
    "in_progress": Album.objects.filter(in_progress=True),
    "year": year,
    "active_view": "index",
  }

  for month in months:
    month_name = calendar.month_name[month]
    try:
      ctx["albums_by_month"][month_name] = Album.objects.filter(listened=True, date_listened__year=year, date_listened__month=month).order_by('-year', 'score', 'artist', 'album')
    except Album.DoesNotExist as e:
      ctx["albums_by_month"][month_name] = []

  return render(request, 'mjuziqmgr/index.html', ctx)

def todo(request):
  tags = [ "jazz", "metal", "misc", "electronic", "prog", "rap" ]
  ctx = {
    "albums_by_tag": {},
    "active_view": "todo",
  }

  for tag in tags:
    try:
      ctx["albums_by_tag"][tag] = Album.objects.filter(listened=False, tags__name__in=[tag]).order_by('-year', 'artist', 'album')
    except Album.DoesNotExist as e:
      ctx["albums_by_tag"][tag] = []

  return render(request, 'mjuziqmgr/todo.html', ctx)