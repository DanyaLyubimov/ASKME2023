from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class QuestionManager(models.Manager):

    def get_all(self):
        return self.all()

    def get_best_questions(self):
        return self.all().order_by('-likes')

    def get_tag_questions(self, tag):
        return self.filter(tags__title__contains=tag)

    def get_newest_questions(self):
        return self.all().order_by('-date')

    def get_question_by_id(self, question_id):
        try:
            return self.get(id=question_id)
        except Question.DoesNotExist:
            return None


class TagsManager(models.Manager):
    def get_top_tags(self, count=5):
        return self.annotate(num_questions=Count('questions')).order_by('-num_questions')[:count]


class AnswersManager(models.Manager):
    def get_answers_by_question_id(self, question_id):
        return self.filter(question_id=question_id)


class Tag(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=60)

    objects = TagsManager()

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    date = models.DateField(default='2023-01-01')
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    tags = models.ManyToManyField('Tag', related_name='questions')
    description = models.CharField(max_length=256)

    objects = QuestionManager()

    def __str__(self):
        return f'{self.title} {self.author}'


class Answer(models.Model):
    date = models.DateField(default='2023-01-01')
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    description = models.CharField(max_length=256)

    objects = AnswersManager()

    def __str__(self):
        return f'{self.question} {self.author}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.ImageField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.user}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.answer}'
