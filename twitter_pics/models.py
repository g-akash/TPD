# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Query(models.Model):
	name = models.CharField(max_length=200)
	query = models.CharField(max_length=200)

	def __str__(self):
		return str(self.query)