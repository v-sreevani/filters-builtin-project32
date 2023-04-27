from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'HOW aRe YoU','dt':dt,'c':1}
    return render(request,'built_in_filters.html',d)