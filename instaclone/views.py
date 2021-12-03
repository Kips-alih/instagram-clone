from django.shortcuts import render
from instaclone.models import Image


# Create your views here.
def index(request):
  photo = Image.objects.all().order_by('-id')

  return render(request, 'all-photos/index.html',{'photo':photo})

