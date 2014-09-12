from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("You've made it to the polls homepage!")

def detail(request, question_id):
    return HttpResponse("This is question : %s" % question_id)

def results(request, question_id):
    return HttpResponse("Poll results for question : %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question : %s" % question_id)

