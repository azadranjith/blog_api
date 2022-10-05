from django.shortcuts import render

from django.views import View
# Create your views here.



class TestView(View):
    
    def get(self,request):
        return render(request,'blog_app/greet.html')
