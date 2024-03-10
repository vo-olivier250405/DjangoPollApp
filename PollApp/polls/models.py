from django.db import models

# Create your models here.


class Question(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    question_text = models.CharField(max_length=200)
    release_date = models.DateTimeField("date published")


class Choice(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
