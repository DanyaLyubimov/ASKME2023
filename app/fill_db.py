import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Question, Answer, Tag


class Command(BaseCommand):
    help = 'Fill the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Coefficient for data generation')

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']

        # Create Users
        users = []
        for i in range(ratio):
            user = User(username=f'user{i}')
            user.save()
            users.append(user)

        # Create Tags
        tags = []
        for i in range(ratio):
            tag = Tag(title=f'tag{i}', description=f'Tag {i}')
            tag.save()
            tags.append(tag)

        # Create Questions, Answers, and Ratings
        for i in range(ratio * 10):
            author = random.choice(users)
            question = Question(author=author, title=f'Question about {i}?', description=f'A detailed description of the question that is written above to make it easier to answer {i}')
            question.save()

            question.tags.set(random.sample(tags, random.randint(1, ratio)))

            for j in range(ratio * 10):
                answer_author = random.choice(users)
                answer = Answer(question=question, author=answer_author, description=f'Answer {j}')
                answer.save()

                # Simulate user ratings
                for _ in range(ratio * 2):
                    rated_user = random.choice(users)
                    answer.likes.create(user=rated_user)

        self.stdout.write(self.style.SUCCESS(f'Successfully filled the database with test data (ratio: {ratio}).'))
