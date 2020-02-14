from django.shortcuts import render, reverse, HttpResponseRedirect
from django.db.models import F
# from django.views.decorators.csrf import csrf_exempt

from ghostpost.models import GhostPost
from ghostpost.forms import GhostPostAddForm

def index(request):
    items = GhostPost.objects.order_by('-created_date')
    return render(request, "index.html", {"data": items})

def sort_likes(request):
    items = GhostPost.objects.order_by('-likes')
    return render(request, "index.html", {"data": items})

def sort_dislikes(request):
    items = GhostPost.objects.order_by('-dislikes')
    return render(request, "index.html", {"data": items})

def like(request, pk):
                ghostpost = GhostPost.objects.get(pk=pk)
                ghostpost.likes += 1
                ghostpost.save()
                return HttpResponseRedirect(reverse('homepage'))

def dislike(request, pk):
                ghostpost = GhostPost.objects.get(pk=pk)
                ghostpost.dislikes += 1
                ghostpost.save()
                return HttpResponseRedirect(reverse('homepage'))

def ghostpost_add_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = GhostPostAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                body=data['body'],
                boast=data['boast']
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = GhostPostAddForm()

    return render(request, html, {'form': form})