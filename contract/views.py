from django.shortcuts import render, redirect,render_to_response
from contract import models
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def unit_views(request):
    unit_list= models.unit.objects.all()

    return render_to_response('admin/contract_info.html',locals())
