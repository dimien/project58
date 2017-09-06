# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Band(models.Model):
	name = models.CharField(max_length=100)
	genere = models.CharField(max_length=100)
	created = models.DateTimeField()
	rip = models.DateTimeField()

	def __str__(self):
		return self.name