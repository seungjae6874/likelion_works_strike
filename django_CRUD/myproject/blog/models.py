from django.db import models

#붕어빵 틀이 될 곳
class Blog(models.Model):

    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    images = models.ImageField(blank = True, upload_to = "images",null = True)
    #
    if images.width_field == 0:
        pass
    def __str__(self):
        return self.title

    #100글자 제한해서 게시글 요약 보기
    def summary(self):
        return self.body[:50]

class Intro(models.Model):

    nick = models.CharField(max_length = 100)
    grade = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    image = models.ImageField(blank = True, upload_to = "image",null = True)

    def __str__(self):
        return self.nick
# Create your models here.
