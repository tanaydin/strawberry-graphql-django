import strawberry_django
from strawberry_django import auto
from typing import List
from . import models


# filters

@strawberry_django.filters.filter(models.Fruit, lookups=True)
class FruitFilter:
    id: auto
    name: auto
    color: 'ColorFilter'

@strawberry_django.filters.filter(models.Color, lookups=True)
class ColorFilter:
    id: auto
    name: auto
    fruits: FruitFilter


# order

@strawberry_django.ordering.order(models.Fruit)
class FruitOrder:
    name: auto
    color: 'ColorOrder'

@strawberry_django.ordering.order(models.Color)
class ColorOrder:
    name: auto
    fruit: FruitOrder


# types

@strawberry_django.type(models.Fruit, filters=FruitFilter, order=FruitOrder, pagination=True)
class Fruit:
    id: auto
    name: auto
    color: 'Color'

@strawberry_django.type(models.Color, filters=ColorFilter, order=ColorOrder, pagination=True)
class Color:
    id: auto
    name: auto
    fruits: List[Fruit]


# input types

@strawberry_django.input(models.Fruit)
class FruitInput:
    id: auto
    name: auto
    color: auto

@strawberry_django.input(models.Color)
class ColorInput:
    id: auto
    name: auto
    fruits: auto


# partial input types

@strawberry_django.input(models.Fruit, partial=True)
class FruitPartialInput(FruitInput):
    pass


@strawberry_django.input(models.Color, partial=True)
class ColorPartialInput(ColorInput):
    pass
