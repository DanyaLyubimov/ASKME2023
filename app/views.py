from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from app.models import Question, Tag, Answer

TAGS = ['Surfing', 'Killepaking', 'Subheading']

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
    questions = Question.objects.get_newest_questions()
    tags = Tag.objects.get_top_tags()
    context = {
        'questions': questions,
        'tags': tags
    }
    return render(request, 'index.html', context)


def question(request, question_id):
    answers = Answer.objects.get_answers_by_question_id(question_id)
    tags = Tag.objects.get_top_tags()
    item = Question.objects.get_question_by_id(question_id)
    context = {
        'question': item,
        'tags': tags,
        'answers': answers
    }
    return render(request, 'oneQuestion.html', context)


def authorization(request):
    tags = Tag.objects.get_top_tags()
    context = {
        'tags': tags
    }
    return render(request, 'authorization.html', context)


def new_question(request):
    tags = Tag.objects.get_top_tags()
    context = {
        'tags': tags
    }
    return render(request, 'newquestion.html', context)


def my_profile(request):
    tags = Tag.objects.get_top_tags()
    context = {
        'tags': tags
    }
    return render(request, 'profile.html', context)


def registration(request):
    tags = Tag.objects.get_top_tags()
    context = {
        'tags': tags
    }
    return render(request, 'registration.html', context)


def hot_questions(request):
    questions = Question.objects.get_best_questions()
    tags = Tag.objects.get_top_tags()
    context = {
        'questions': questions,
        'tags': tags
    }
    return render(request, 'index.html', context)


def tag_questions(request, tag_name):
    tag = tag_name
    if tag != '':
        objects = [item for item in QUESTIONS if item['tag'] == tag]
    else:
        objects = HOT_QUESTIONS
    tags = Tag.objects.get_top_tags()
    questions = Question.objects.get_tag_questions(tag_name)
    context = {
        'questions': questions,
        'tags': tags
    }
    return render(request, 'tagQuestions.html', context)
