from django.shortcuts import render
from .forms import textinput
import qrcode
from PIL import Image
import re
# Create your views here.
def home(request):
    if request.method == 'POST':
        form=textinput(request.POST)
        if form.is_valid():
            inp=form.cleaned_data['inp']
            url_pattern_1 = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
            url_pattern_2 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
            flag1=re.match(url_pattern_1, inp)!=None
            flag2=re.match(url_pattern_2, inp)!=None
            qrcode.make(inp).save('generate/static/qr.png')
            return render(request,'generate/result.html',{'inp':inp,'flag1':flag1,'flag2':flag2})
    form=textinput()
    return render(request,'generate/home.html',{'form':form})