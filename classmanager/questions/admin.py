from django.contrib import admin

from .models import User, Question, Course, Topic, Answer


class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ("saved_by",)

class AnswerAdmin(admin.ModelAdmin):
    filter_horizontal = ("upvoted_by", "downvoted_by")
    
# Register your models here.
# admin.site.register(User)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)