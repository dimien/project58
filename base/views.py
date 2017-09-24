# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Band

# Create your views here.

def index(request):
    name = get_object_or_404(Band.objects.values_list("name", flat=True))
    genere = get_object_or_404(Band.objects.values_list("genere", flat=True))
    created = get_object_or_404(Band.objects.values_list("created", flat=True))
    rip = get_object_or_404(Band.objects.values_list("rip", flat=True))
    context = {
        "band_name": name,
        "band_genere": genere,
        "band_created": created,
        "band_rip": rip
    }
    return render(request, 'base/index.html', context)

