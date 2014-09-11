import datetime

from django.db import models
from django.utils import timezone

class Question (models.Model) :
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __unicode__(self):
    return self.question_text

  def was_recently_published(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  was_recently_published.admin_order_field = 'pub_date'
  was_recently_published.boolean = True
  was_recently_published.short_description = "Published Recently?"

class Choice (models.Model) :
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __unicode__(self):
    return self.choice_text
