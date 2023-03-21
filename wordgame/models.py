from django.db import models

# Create your models here.
class NewWord(models.Model):
    word = models.CharField(max_length=20)
    isValid = models.BooleanField()
    pointsValue = models.IntegerField()
    
    def __str__(self):
        return self.word
    
class Button(models.Model):
    position = models.CharField(max_length=2)
    clickable = models.BooleanField()
    
    class Letter(models.Model):
        is_vowel = models.BooleanField()
        point_value = models.IntegerField()

        def __str__(self):
            return self.point_value

    def __str__(self):
            return self.position


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text