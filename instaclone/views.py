from django.shortcuts import render,redirect
from instaclone.models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,ProfileForm
from django.http  import Http404




# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  photo = Image.objects.all().order_by('-id')

  return render(request, 'all-photos/index.html',{'photo':photo})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    image = Image.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ProfileForm()

    return render(request, 'all-photos/profile.html', {"image": image, "profile": profile,"form":form})

#search results functions
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})

