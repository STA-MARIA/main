from django.db import models

class User(models.Model):
    name = models.TextField(default="")
    comment = models.TextField(default="")
    number = models.IntegerField(default="")
    User_ID = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return self.name 
    
class Subscription(models.Model):
    features = models.TextField(default="")
    inclusion = models.TextField(default="")
    Service_ID = models.TextField(default="",primary_key=True)
    usersub = models.OneToOneField(User, on_delete=models.CASCADE)
    # usersubs = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Service_IDS


class Guides(models.Model):
    Walkthrough = models.TextField(default="")
    Tips = models.TextField(default="")
    Guide_ID = models.TextField(default="",primary_key=True)
    serviceguides = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return self.Guide_ID

class Feedback(models.Model):
    forum = models.TextField(default="")
    polls = models.TextField(default="")
    reaction = models.TextField(default="")
    Feedback_ID= models.TextField(default="",primary_key=True)
    # User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    guidefeedback = models.ManyToManyField(Guides)
    
    def __str__(self):
        return self.Feedback_ID

class Feeds(models.Model):
    News_ID = models.TextField(default="",primary_key=True)
    servicefeeds = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    userfeeds = models.ForeignKey(User, on_delete=models.CASCADE)
    feedsfeedback = models.ManyToManyField(Feedback)
    feedguide = models.ManyToManyField(Guides)
    
    def __str__(self):
        return self.News_ID 
    

    
