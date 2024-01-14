from django.db import models

# Create your models here.
class Artist (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True,default=0)
    profile_pic = models.ImageField(blank=True,upload_to='artists')
    def __str__(self):
        return self.name;

class Song(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_cover = models.ImageField(blank=True,upload_to='songs')

    def __str__(self):
        return self.title