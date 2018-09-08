from django.db import models

# Create your models here.

class QuesModel(models.Model):
    QTYPE = (
        ('MCQ','MCQ'),
        ('ING','ING'),
    )
    stmt  = models.CharField(max_length=50)
    qtype = models.ChoiceField(max_length=5,choices=QTYPE,default='MCQ')

    def __str__(self):
        return self.stmt

class choiceModel(models.Model):
    q = models.ForeignKey(QuesModel,on_delete=models.CASCADE)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    option4 = models.CharField(max_length=20)
    OPTIONS = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
    )
    ans = models.IntegerField('Answer',choices=OPTIONS,default=0)


class YourchoiceModel(models.Model):
    stmt = models.ForeignKey(QuesModel,on_delete=models.CASCADE)
    ans_c= models.ForeignKey(choiceModel, default=0,on_delete=models.CASCADE)
    choice = models.CharField('Your Ans',max_length=20,blank='True',default='1')

    def score(self):
        if self.choice==self.ans_c.ans:
            return 1
        else:
            return 0
