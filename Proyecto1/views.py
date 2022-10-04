from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import random
from Personas.models import Persona

def crear_persona(request, nombre, apellido):
    persona = Persona(nombre = nombre, apellido = apellido, edad = random.randrange(1, 99), fecha_nacimiento = datetime.now())
    persona.save()
    persona = Persona.objects.all()
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'persona': persona})
    
    return HttpResponse(template_renderizado)
