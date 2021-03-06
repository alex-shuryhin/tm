from django.db import models


class Goal(models.Model):
    priority = models.PositiveSmallIntegerField(default=100)
    goal_text = models.CharField(max_length=200)
    goal_t2 = models.CharField(max_length=200)

    def __str__(self):
        return self.goal_text


class Plan(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    plan_child = models.CharField(max_length=200)
    plan_aim = models.CharField(max_length=200)
    plan_tree = models.CharField(max_length=200)
    plan_bottleneck = models.CharField(max_length=200)
    plan_wall = models.CharField(max_length=200)
    plan_plank = models.CharField(max_length=200)


class Comments(models.Model):
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text
