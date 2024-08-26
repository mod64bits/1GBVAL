from apps.home.models import Empresa

def empresa_context(request):
    empresa = Empresa.objects.first()
    return {'empresacontext': empresa}