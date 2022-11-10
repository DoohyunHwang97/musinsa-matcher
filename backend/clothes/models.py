from django.db import models
from django.contrib.auth.models import AbstractUser


class Pants_size(models.Model):
    waist_size = models.IntegerField()
    hip_size = models.IntegerField()
    thigh_size = models.IntegerField()
    calf_size = models.IntegerField()
    rise = models.IntegerField()
    inseam = models.IntegerField()

class Clothes(models.Model):
    style = models.CharField(max_length=30)
    brand = models.CharField(max_length=50)
    #color
    price = models.IntegerField()
    URL = models.CharField(max_length=200)
    #analytics
    photo = models.CharField(max_length=200) #사진의 저장 경로
    size = models.ForeignKey(
        Pants_size, #style 추가시 수정
        on_delete=models.PROTECT #pants_size가 삭제되는 일은 없을 것
    )

    def __str__(self):
        return self.name

#class color

class Myuser(AbstractUser):
    nickname = models.CharField(max_length=50)
    chest_size = models.IntegerField(default=0)
    waist_size = models.IntegerField(default=0)
    thigh_size = models.IntegerField(default=0)
    calf_size = models.IntegerField(default=0)

    purchased = models.ManyToManyField(
        Clothes,
        related_name = "user_purchased",
    )

    scrapped = models.ManyToManyField(
        Clothes,
        related_name = "user_scrapped",
    )

    def __str__(self):
        return self.username



class Review(models.Model):
    upload_time = models.TimeField()
    content = models.TextField()
    photo = models.CharField(max_length=200) #사진의 저장 경로
    reviewing_clothes = models.ForeignKey(
        Clothes,
        on_delete=models.CASCADE,
        related_name = "clothes_review",
    )
    uploaded_user = models.ForeignKey(
        Myuser,
        on_delete=models.CASCADE, #User가 삭제되는 경우
        related_name = "uploaded_review",
    )

class Comment(models.Model):
    upload_time = models.TimeField()
    content = models.TextField()
    uploaded_user = models.ForeignKey(
        Myuser,
        on_delete=models.CASCADE, #User가 삭제되는 경우
        related_name = "uploaded_comments",
    )
    original_review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comment_uploaded',
    )