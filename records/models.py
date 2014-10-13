import datetime

from django.db import models

class Album(models.Model):
	album_text = models.CharField(max_length=200)
	company_text = models.CharField(max_length=200)
	release_date = models.DateTimeField('date released')
	def __unicode__(self):
		return self.album_text

class Artist(models.Model):
	album = models.ForeignKey(Album)
	artist_text = models.CharField(max_length=200)
	def __unicode__(self):
		return self.artist_text


