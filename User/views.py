from django.shortcuts import render
from django.views import View

class HomePageView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)

class LoginPageView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)