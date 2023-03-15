from django.shortcuts import render

# Create your views here.
def Sample(request):
    d={'A':10, 'B':20}
    return render(request, 'temp.html', d)