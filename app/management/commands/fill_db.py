import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Question, Answer, Tag, QuestionLike, AnswerLike


class Command(BaseCommand):
    help = 'Fill the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Coefficient for data generation')

    def handle(self, *args, **kwargs):
        fake = Faker()
        ratio = kwargs['ratio']

        # Create Users
        users = [
            User(username=f'newUser{i}', email=fake.email(), password=fake.password())
            for i in range(ratio)
        ]
        User.objects.bulk_create(users)

        # Create Tags
        tags = [
            Tag(title=f'newTag{i}', description=fake.text())
            for i in range(ratio)
        ]
        Tag.objects.bulk_create(tags)

        questions = []
        for i in range(ratio * 10):
            author = random.choice(users)
            question = Question(
                author=author,
                title=fake.sentence(),
                description=fake.text(),
                likes=random.randint(0, ratio * 5),
                dislikes=random.randint(0, ratio * 5),
            )
            questions.append(question)
        print(*questions)
        Question.objects.bulk_create(questions)
        for _ in range(ratio*100):
            question = random.choice(questions)
            rated_user = random.choice(users)
            question_like, created = QuestionLike.objects.get_or_create(user=rated_user, question=question)

        for question in questions:
            question_tags = random.sample(tags, random.randint(1, ratio))
            question.tags.set(question_tags)

        answers = []
        for j in range(ratio * 100):
            answer_author = random.choice(users)
            question = random.choice(questions)
            answer = Answer(
                question=question,
                author=answer_author,
                description=fake.text(),
                likes=random.randint(0, ratio * 5),
                dislikes=random.randint(0, ratio * 5),
            )
            answers.append(answer)
        Answer.objects.bulk_create(answers)
        for _ in range(ratio*100):
            rated_user = random.choice(users)
            answer = random.choice(answers)
            answer_like, created = AnswerLike.objects.get_or_create(user=rated_user, answer=answer)

        self.stdout.write(self.style.SUCCESS(f'Successfully filled the database with test data (ratio: {ratio}).'))
