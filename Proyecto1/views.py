from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from Personas.models import Persona

def ver_personas(request, nombre, apellido, edad):
    persona = Persona(nombre = nombre, apellido = apellido, edad = edad, fecha_de_creacion = datetime.now())
    persona = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'persona': persona})
    
    return HttpResponse(template_renderizado)