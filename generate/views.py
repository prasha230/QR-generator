from django.shortcuts import render
from .forms import textinput
import qrcode
from PIL import Image
# Create your views here.
def home(request):
    if request.method == 'POST':
        form=textinput(request.POST)
        if form.is_valid():
            inp=form.cleaned_data['inp']
            qrcode.make(inp).save('generate/static/qr.png')
            return render(request,'generate/result.html',{'inp':inp})
    form=textinput()
    return render(request,'generate/home.html',{'form':form})