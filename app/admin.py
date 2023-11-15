from django.contrib import admin
from .models import Answer, Tag, Question, Profile
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Profile)
