from django.db import models

# Create your models here.
#class Women(models.Model):
class Smartphones(models.Model):
    title=models.CharField(max_length=255) #-  посилання на екземпляр ЧАРФіелд(максимальна довжина текстового поля =255)

    content=models.TextField(blank=True) #- розширена інформація, поле може бути пустим, але це навряд

    photo=models.ImageField(upload_to="photos/%Y/%m/%d")# - посилання на фото нашого посту, в які підкаталоги ми будемо загружати наші фото

    time_create=models.DateTimeField(auto_now_add=True)#не буде мінятись - час створення статті і час її використання(міняється автоматично)

    time_update=models.DateTimeField(auto_now=True)#буде змінюваись кожен раз як ми будемо щось змінювати

    is_published=models.BooleanField(default=True)# - буде тру по дефолту в момент коли ми щось будемо додавати

    def __str__(self):
        return self.title

class Laptops(models.Model):
    title = models.CharField(
        max_length=255)  # -  посилання на екземпляр ЧАРФіелд(максимальна довжина текстового поля =255)

    content = models.TextField(blank=True)  # - розширена інформація, поле може бути пустим, але це навряд

    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d")  # - посилання на фото нашого посту, в які підкаталоги ми будемо загружати наші фото

    time_create = models.DateTimeField(
        auto_now_add=True)  # не буде мінятись - час створення статті і час її використання(міняється автоматично)

    time_update = models.DateTimeField(auto_now=True)  # буде змінюваись кожен раз як ми будемо щось змінювати

    is_published = models.BooleanField(default=True)  # - буде тру по дефолту в момент коли ми щось будемо додавати

class about_me(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


