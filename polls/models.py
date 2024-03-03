from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(
        "date published"
    )  # The opitional argument given here is an human-readable name.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(
        max_length=200
    )  # attribute name "choice_text" is used as column name.
    # CharField has max_length as a required argument. It's used for the
    # database schema and validation.
    votes = models.IntegerField(default=0)  # default is an optional field.
