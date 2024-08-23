from django.shortcuts import render
from rest_framework import generics
from . import serializers
from api.models import menu, feedback
from .forms import feedbackform

class MenuList(generics.ListAPIView):
    queryset = menu.objects.all()
    serializer_class = serializers.menu_serializer

def FeedbackCheck(request):
    comments = feedback.objects.all()
    return render(request, "FeedbackCheck.html", {"comments":comments})


def FeedbackPost(request):
    error = ''
    if request.method == "POST":
        form = feedbackform(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Форма заполнена неверно"

    form = feedbackform
    data = {
        'form': form,
        'error': error
    }
    return render(request, "FeedbackPost.html", data)


# def main_page(request):
#     return render(request, "index.html")