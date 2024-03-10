from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Question(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    question_text = models.CharField(max_length=200)
    release_date = models.DateTimeField("date published")

    def __str__(self):
        """_summary_
        """
        return self.question_text

    def was_published_recently(self):
        return self.release_date >= timezone.now() - timedelta(days=1)


class Choice(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """_summary_
        """
        return self.choice_text
