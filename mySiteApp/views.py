from django.shortcuts import render,HttpResponse
from .forms import ImageForm
from rest_framework import viewsets
from mySiteApp.models import GameLevel
from mySiteApp.serializers import GameLevelSerializer






# Create your views here.
def index(request):
  return render(request,'index.html')



def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


class GameLevelViewSet(viewsets.ModelViewSet):
   queryset = GameLevel.objects.all()
   serializer_class = GameLevelSerializer