from django.conf.urls import url, include

from . import views

app_name = "tm"
urlpatterns = [
    url(r'^$', views.GoalsView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.PlanView.as_view(), name = "plan"),
    url(r'^(?P<goal_id>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
]

