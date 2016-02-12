from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Goal, Plan, Comments

from django.views import generic

class GoalsView(generic.ListView):
    template_name = 'tm/goals.html'
    
    context_object_name = 'goal_list'    
    def get_queryset(self):
        return Goal.objects.order_by('-priority')[:5]

class PlanView(generic.DetailView):
    template_name = 'tm/plan.html'
    model = Goal

def add_comment(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    try:
        comment_text = request.POST['comment_text']
    except (KeyError, Comment.IsEmpty):
        # Redisplay the question voting form.
        return render(request, 'tm/plan.html', {
            'goal': goal,
            'error_message': "You didn't select a choice.",
        })
    else:
        comment = Comments(comment_text = comment_text, pub_date = timezone.now(), goal_id = goal_id)
        comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('tm:plan', args=(goal.id,)))
