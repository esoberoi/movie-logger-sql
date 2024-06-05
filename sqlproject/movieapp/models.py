from django.db import models

# Create your models here.

# These two models utilize Django ORM to interact with SQLite databases-- particuarly, 
# the Movie table and the MovieLog table

class Movie(models.Model): # movie table model
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField(db_index=True) #INDEX 1
    length = models.IntegerField()

    def __str__(self):
        return self.title

class MovieLog(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, db_index=True) #INDEX 2
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) #movie LOG model, note foreign key to Movie class
    date_watched = models.DateField(db_index=True) #INDEX 3
    rating = models.IntegerField()

    #class Meta:
     #   indexes = [
      #      models.Index(fields=['user_id']),
       #     models.Index(fields=['date_watched'])
        #]

    def __str__(self):
        return f"{self.user_id}: {self.movie.title} - {self.date_watched}"