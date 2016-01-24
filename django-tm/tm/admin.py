from django.contrib import admin

from .models import Goal, Plan, Comments

#class PlanInLine(admin.StackedInline):
#    model = Plan
#    extra = 1

#class GoalAdmin(admin.ModelAdmin):
#   inlines = [PlanInLine]

class GoalAdmin(admin.ModelAdmin):
    search_fields = ['goal_text']

class CommentsAdmin(admin.ModelAdmin):
    fields = ['goal', 'comment_text', 'pub_date']
    list_display = ('comment_text', 'goal')
    list_filter = ['pub_date']
    search_fields = ['comment_text']

admin.site.register(Goal, GoalAdmin)
admin.site.register(Plan)
admin.site.register(Comments, CommentsAdmin)
