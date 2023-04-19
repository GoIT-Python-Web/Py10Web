import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import PictureForm
from .models import Picture


# Create your views here.
def home(request):
    return render(request, "app_instagram/index.html", context={"title": "Project Instagram"})


@login_required
def pictures(request):
    pictures = Picture.objects.filter(user=request.user).all()
    return render(request, "app_instagram/pictures.html", context={"title": "Project Instagram", "pictures": pictures})


@login_required
def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to="app_instagram:pictures")
    return render(request, "app_instagram/upload.html", context={"title": "Project Instagram", "form": form})


@login_required
def remove(request, pic_id):
    picture = Picture.objects.filter(pk=pic_id, user=request.user)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.first().path)))
    except OSError as e:
        print(e)
    picture.delete()
    return redirect(to="app_instagram:pictures")


@login_required
def edit(request, pic_id):
    if request.method == "POST":
        description = request.POST.get('description')
        Picture.objects.filter(pk=pic_id, user=request.user).update(description=description)
        return redirect(to="app_instagram:pictures")

    pic = Picture.objects.filter(pk=pic_id, user=request.user).first()
    return render(request, "app_instagram/edit.html", context={"title": "Project Instagram", "pic": pic})
