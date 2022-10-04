from django.http import HttpResponse
from django.template import loader, Template, Context
from datetime import datetime
import random


# def hola(request):
#     return HttpResponse('<h1>Buenos dias</h1>')


# def mi_template(request):
    
#     cargar_archivo = open(r'C:\Users\magaa\OneDrive\Escritorio\MI_PROYECTO\template\index.html','r')
#     template = Template(cargar_archivo.read())
#     cargar_archivo.close()
#     contexto = Context()
#     template_renderizado = template.render(contexto)
        
#     return HttpResponse(template_renderizado)

def crear_persona(request, nombre, apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona.save()
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'persona': persona})
    
    return HttpResponse(template_renderizado)


def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
        
    return HttpResponse(template_renderizado)