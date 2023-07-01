from django.shortcuts import render

from .models import *

def report_card(request):
    object_ss = TakeCourses.objects.filter(studentNo=4002040)

    print(object_ss)

    return

