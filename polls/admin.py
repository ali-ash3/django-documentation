from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text", "pub_date",)
admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "choice_text","votes")
admin.site.register(Choice, ChoiceAdmin)
