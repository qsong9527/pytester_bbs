# -*- encoding:utf-8 -*-

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome To PyTester Home</h1><hr size='18' color='gray'>")