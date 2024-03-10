from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by("-release_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """_summary_

    Args:
        request (_type_): _description_
        question_id (_type_): _description_
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """_summary_

    Args:
        request (_type_): _description_
        question_id (_type_): _description_
    """
    response = f"You're looking at the result of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
