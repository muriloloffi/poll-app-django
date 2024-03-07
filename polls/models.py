import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(
        "date published"
    )  # The opitional argument given here is an human-readable name.

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(
        max_length=200
    )  # attribute name "choice_text" is used as column name.
    # CharField has max_length as a required argument. It's used for the
    # database schema and validation.
    votes = models.IntegerField(default=0)  # default is an optional field.

    def __str__(self):
        return self.choice_text
