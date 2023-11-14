from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorus ipsum {i}'
        } for i in range(20)
    ]


def paginate(objects, page,  per_page=15):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)
def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, page)})


def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'oneQuestion.html', {'question': item})


def authorization(request):
    return render(request, 'authorization.html')


def new_question(request):
    return render(request, 'newquestion.html')


def my_profile(request):
    return render(request, 'profile.html')