from django.db import models

# Create your models here.

class UserLogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()

class Interest(models.Model):
    topic = models.CharField(max_length=30)
    #def __str__(self):
    #    return str(self.topic)



class UserInterest(models.Model):
    user_id = models.ForeignKey(UserLogin,on_delete=models.CASCADE)
    interest_id = models.ForeignKey(Interest,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.interest_id_id)


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    created_by = models.ForeignKey(UserLogin,on_delete = models.CASCADE)
    topic_id = models.ForeignKey(Interest,on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    

    

class Answer(models.Model):
    que_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=2000)
    answerd_by = models.ForeignKey(UserLogin,on_delete=models.CASCADE)

class Upvote(models.Model):
    answer_id = models.ForeignKey(Answer,on_delete=models.CASCADE)
    upvoted_by = models.ForeignKey(UserLogin,on_delete=models.CASCADE)

