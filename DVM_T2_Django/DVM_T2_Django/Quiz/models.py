from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.TextField(null=True)
    op1 = models.TextField(null=True)
    op2 = models.TextField(null=True)
    op3 = models.TextField(null=True)
    op4 = models.TextField(null=True)
    ans = models.TextField(null=True)
    
    def __str__(self):
        return self.question