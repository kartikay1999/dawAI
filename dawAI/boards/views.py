from django.shortcuts import render,get_object_or_404
from .models import inp

# Create your views here.
def index(request):
    all_symptoms=inp.objects.all()
    context={
        'all_symptoms':all_symptoms
    }
    return render(request,'boards/index.html',context)

