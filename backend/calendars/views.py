from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters import rest_framework as filters

from .models import Event
from .serializer import EventSerializer


class EventFilter(filters.FilterSet):
  year = filters.NumberFilter(field_name='date', lookup_expr='year')
  month = filters.NumberFilter(field_name='date', lookup_expr='month')

  class Meta:
    model = Event
    fields = ['year', 'month']


class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  filter_class = EventFilter
