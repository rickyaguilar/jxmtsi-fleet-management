from django.shortcuts import render,HttpResponseRedirect, render
#from .models import (
#    Driver,
#)
from django.views.generic import (
    CreateView
)
#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import user_passes_test



#def in_group(user):
#    if user.groups.filter(name="Driver").exists():
#        return True
#    else:
#        raise PermissionDenied()


#@user_passes_test(in_group)
def Drivers(request):
#    context = {
#       'Drivers': Driver.objects.all(),
#        'title': 'Reg-Drivers'
#    }
    return render(request, 'Reg_Driver/driver_list.html')

class DriverCreateView(CreateView):
#    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    template_name = 'Reg_Driver/drive_form.html'