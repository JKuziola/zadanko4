from django.contrib import admin

from .models import Question, Choice


class QuestionChoiceInline(admin.TabularInline):
    fieldsets = (
        ('Advanced options', {
            'classes': ('collapse'),
            'fields': ('choice_text', 'votes')
        }),
    )
    model = Choice
    extra = 1
    show_change_link = True


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionChoiceInline]
# Register your models here.
