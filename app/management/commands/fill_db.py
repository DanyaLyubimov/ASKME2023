import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Question, Answer, Tag, Like


class Command(BaseCommand):
    help = 'Fill the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Coefficient for data generation')

    def handle(self, *args, **kwargs):
        fake = Faker()
        ratio = kwargs['ratio']

        # Create Users
        users = []
        for i in range(ratio):
            user = User(username=f'user{i+10}', email=fake.email(), password=fake.password())
            user.save()
            users.append(user)

        # Create Tags
        tags = []
        for i in range(ratio):
            tag = Tag(title=f'tag{i}', description=fake.text())
            tag.save()
            tags.append(tag)

        # Create Questions, Answers, and Ratings
        for i in range(ratio * 10):
            author = random.choice(users)
            question = Question(
                author=author,
                title=fake.sentence(),
                description=fake.text(),
                likes=random.randint(0, ratio * 5),
                dislikes=random.randint(0, ratio * 5),
            )
            question.save()

            question.tags.set(random.sample(tags, random.randint(1, ratio)))

        for j in range(ratio * 100):
            answer_author = random.choice(users)
            answer = Answer(
                question=question,
                author=answer_author,
                description=fake.text(),
                likes=random.randint(0, ratio * 5),
                dislikes=random.randint(0, ratio * 5),
            )
            answer.save()

                # Simulate user ratings
        for _ in range(ratio * 200):
            rated_user = random.choice(users)
            like = Like(user=rated_user, question=question)
            like.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully filled the database with test data (ratio: {ratio}).'))
