from django.shortcuts import render

# Create your views here.
def index(request):
    #FOR CUSTOM FILTERS
    context_dict = {'text':'hello world','number':1000}
    return render(request,'basicapp/index.html',context_dict)#con dict onnly for filters

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/rel_url_temp.html')
