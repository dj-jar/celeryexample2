from __future__ import absolute_import
from celery import shared_task


@shared_task
def add_task(a, b):
    return a + b


@shared_task
def mul_task(a, b):
    return a * b


@shared_task
def fac_task(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
