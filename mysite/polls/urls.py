from django.conf.urls import url
from polls import views

urlpatterns = [
    #example pattern : /polls/
    url(r'^$', views.index, name='index'),
    #example pattern : /polls/3/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #example pattern : /polls/3/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #example pattern : /polls/3/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]