from django.shortcuts import render

# Create your views here.
def index_generale(request):
    return render(request, "index_generale.html")

#def base(request):
 #  return render(request, "base.html")