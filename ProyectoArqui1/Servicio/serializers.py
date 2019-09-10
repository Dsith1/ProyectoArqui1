from rest_framework import serializers
from Servicio import models

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imagen
        fields = "__all__"
