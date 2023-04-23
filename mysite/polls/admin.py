from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)



""" class QuestionChoiceInline(admin.TabularInline):
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
    inlines = [QuestionChoiceInline] """
# Register your models here.
