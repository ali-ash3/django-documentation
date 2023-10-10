from django.contrib import admin
from polls.models import Question, choice

# Register your models here.
admin.site.register(Question)
admin.site.register(choice)
