from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from celery.result import AsyncResult
from mathapp.tasks import add_task, mul_task, fac_task


def add_delay(request, a, b):
    t = add_task.delay(int(a), int(b))
    return HttpResponseRedirect(reverse('m:task_result', args=[t.task_id]))


def mul_delay(request, a, b):
    t = mul_task.delay(int(a), int(b))
    return HttpResponseRedirect(reverse('m:task_result', args=[t.task_id]))


def fac_delay(request, n):
    t = fac_task.delay(int(n))
    return HttpResponseRedirect(reverse('m:task_result', args=[t.task_id]))


# view queued task
def task_result(request, task_id):
    res = AsyncResult(task_id)
    ctx = {
        'status': res.status,
        'result': res.result
    }
    return render(request, 'mathapp/task_result.html', ctx)
