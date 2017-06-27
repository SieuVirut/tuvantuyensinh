from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    template = loader.get_template('tuvantuyensinh/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request ,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'tuvantuyensinh/detail.html', {'question': question})
def results(requets ,question_id):
    response = "Ban dang xem cau tra loi cua cau hoi %s"
    return HttpResponse(response %question_id)
def vote(request ,question_id):
    return HttpResponse("Binh chon cho cau hoi %s" %question_id)