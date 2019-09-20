from django.shortcuts import render,HttpResponseRedirect, render


def Repair(request):

    return render(request, 'maintenance/repair_form.html')

def Repair_list(request):

    return render(request, 'maintenance/repair_list.html')