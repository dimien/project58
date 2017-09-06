# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from models import Band

# Create your views here.

def index(request):
	bands = Band.objects.all()
	print bands
	# context = get_object_or_404(Band, pk=1)
	context = {'bands': bands}
	return render(request, 'base/index.html', context)