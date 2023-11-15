from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

TAGS = ['Surfinging', 'Killepaking', 'Subheading']

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'Ambitioni dedisse scripsisse iudicaretur. Cras mattis iudicium purus sit amet fermentum. Donec '
                   f'sed odio operae, eu vulputate felis rhoncus. Praeterea iter est quasdam res quas ex communi. At '
                   f'certam indicere. Cras mattis iudicium purus sit amet fermentum. {i} ',
        'tag': TAGS[i % 3]
    } for i in range(20)
]

HOT_QUESTIONS = [
    {
        'id': i,
        'title': f'HotQuestion {i}',
        'content': f'Hot Ambitioni dedisse scripsisse iudicaretur. Cras mattis iudicium purus sit amet fermentum. Donec '
                   f'sed odio operae, eu vulputate felis rhoncus. Praeterea iter est quasdam res quas ex communi. At '
                   f'certam indicere. Cras mattis iudicium purus sit amet fermentum. {i} '
    } for i in range(20)
]


def paginate(objects, request, per_page=15):
    page = int(request.GET.get('page', 1))
    if page > len(objects)//per_page+1:
        page = len(objects)//per_page
    paginator = Paginator(objects, per_page)
    return paginator.page(page)


def index(request):
    context = {
        'questions': paginate(QUESTIONS, request),
        'tags': TAGS
    }
    return render(request, 'index.html', context)


def question(request, question_id):
    item = QUESTIONS[question_id]
    context = {
        'question': item,
        'tags': TAGS
    }
    return render(request, 'oneQuestion.html', context)


def authorization(request):
    context = {
        'tags': TAGS
    }
    return render(request, 'authorization.html', context)


def new_question(request):
    context = {
        'tags': TAGS
    }
    return render(request, 'newquestion.html', context)


def my_profile(request):
    context = {
        'tags': TAGS
    }
    return render(request, 'profile.html', context)


def registration(request):
    context = {
        'tags': TAGS
    }
    return render(request, 'registration.html', context)


def hot_questions(request):
    context = {
        'questions': paginate(HOT_QUESTIONS, request),
        'tags': TAGS
    }
    return render(request, 'index.html', context)


def tag_questions(request, tag_name):
    tag = tag_name
    if tag != '':
        objects = [item for item in QUESTIONS if item['tag'] == tag]
    else:
        objects = QUESTIONS
    context = {
        'questions': paginate(HOT_QUESTIONS, request),
        'tags': TAGS
    }
    return render(request, 'tagQuestions.html', context)
