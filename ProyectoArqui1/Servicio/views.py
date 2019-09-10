from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wsgiref.util import FileWrapper
from mimetypes import MimeTypes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import base64
import os


from .serializers import ImagenSerializer
from .models import Imagen

def index(request):
    return HttpResponse("Hello, Django!")
# Create your views here.


def VerImg(request,id):
    
    try:
        img = Imagen.objects.get(id=id)
    except Imagen.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        
       
        serializer = ImagenSerializer(img)

        
        handle1=open(serializer.data['nombre']+'.bmp','wb')
        imgdata = base64.b64decode(serializer.data['archivo']+'==')
        handle1.write(imgdata)
        handle1.close()
        
        return JSONResponse(serializer.data)

    
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)    



class Enviar_Img(APIView):
    parser_class =(ImagenSerializer,)
    
    def post(self,request,*args, **kwargs):
    
        file_serializer = ImagenSerializer(data=request.data)
    
        if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
   


  
