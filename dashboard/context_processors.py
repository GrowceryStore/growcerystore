from dashboard.models import Employeprofile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def getemploye(request):
    edetail=None
    if request.user.is_authenticated and request.user.is_superuser!=1:
        userid=request.user.id
        print(userid)
        try:
            edetail=Employeprofile.objects.get(Employe_Id_id=userid)
        except ObjectDoesNotExist:
            edetail=User.objects.get(id=userid)
    return {'edetail':edetail}    