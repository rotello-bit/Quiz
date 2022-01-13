from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, db_column='quiz_id', on_delete=models.CASCADE)
    no = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=250, null=True)

    class Meta:
        unique_together = ('quiz_id', 'no',)

    def __str__(self):
        return self.name


class Option(models.Model):
    question = models.ForeignKey(Question, db_column='question_id', on_delete=models.CASCADE)
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, db_column='question_id', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, db_column='option_id', on_delete=models.CASCADE)

    def __str__(self):
        return 'Soru: ' + self.question.name + '  Cevap: ' + self.option.name
