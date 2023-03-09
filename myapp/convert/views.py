from django.shortcuts import render

def index(request):
    # global converted_t
    # global temp
    converted_t = None
    temp = None
    if request.method == "POST":
        temp = int(request.POST.get('t',''))
        converted_t = (temp-32)*0.5556
    
    return render(request, 'convert/index.html', {'temp': temp, 'con': converted_t})
           
   
    


# Create your views here.
