from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) #짧은문자열로 되어있는 데이터를 title로 처리하고 최대길이는 200이다.
    pub_date = models.DateTimeField('date published') #PublishDate를 시간으로 처리
    body = models.TextField() #긴문자열 body로 처리

    def __str__(self):
        return self.title