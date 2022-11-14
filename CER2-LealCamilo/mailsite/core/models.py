from django.db import models

# Create your models here.

class Residencia(models.Model):
    numero_residencia = models.IntegerField(primary_key=True)
    nombre_dueno = models.CharField(max_length=50)
    fono = models.IntegerField()
    correo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 'Residencia ' + str(self.numero_residencia)

class Mail(models.Model):
    fecha_recepcion = models.DateField()
    conserje = models.CharField(max_length=50)
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    estados = (('Elige una opción','Elige una opción'),
               ('Entregado','Entregado'),
               ('No entregado','No entregado') )
    estado = models.CharField(max_length=20, choices=estados, default='Elige una opción')
    numero_residencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'Correspondencia con fecha ' + str(self.fecha_recepcion) + ' para la residencia ' + str(self.numero_residencia) 