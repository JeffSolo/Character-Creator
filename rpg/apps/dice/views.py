from django.http import JsonResponse
from django.shortcuts import render
from .common import roll_stats


def rolled_stats(request):
    return JsonResponse({'stats': roll_stats()})
