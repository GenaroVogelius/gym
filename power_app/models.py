from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver



# Create your models here.
class Usuario(models.Model):

    # el primer argumento es como se va guardar en el model, el segundo argumento es como se va a ver en admin
    SEX_CHOICES = [
        ("Femenino", "Femenino"),
        ("Masculino", "Masculino"),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=SEX_CHOICES)
    DNI = models.IntegerField(unique=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    pago = models.DateField(default=timezone.now, null=False, blank=False)
    vencimiento = models.DateField(
        null=True, blank=True, help_text="Si no es especificado será dentro de 30 dias"
    )
    activo = models.BooleanField(default=True, editable=False)
    id = models.AutoField(primary_key=True)
    # esto de id lo pusiste asi ya que importas los usuarios desde un excel, en asistencia no lo pones porque arranca desde cero.

    # ? @staticmethod: This decorator is used to define a static method within a class. A static method belongs to the class itself rather than an instance of the class. In this case, it means that the method can be called directly on the class itself without needing to create an instance of the class. 
    # ? @receiver(pre_save, sender="power_app.Usuario"): This is a decorator provided by Django's signals framework. It allows you to register the function as a receiver for the pre_save signal emitted by the Usuario model in the power_app app. The pre_save signal is sent just before saving an instance of the model.
    @staticmethod
    @receiver(pre_save, sender="power_app.Usuario")
    def update_activo(sender, instance, **kwargs):
        # ? escribimos un try y excep ya que necesitamos el .date() cuando se sube un archivo excel y cuando no salta un error por eso en el except lo sacamos
        try:
            if instance.vencimiento.date() < timezone.now().date():
                instance.activo = False
            else:
                instance.activo = True
        except:
            if instance.vencimiento < timezone.now().date():
                instance.activo = False
            else:
                instance.activo = True

        

    def save(self, *args, **kwargs):

        #? para cuando se crea un nuevo usuario.
        if self.vencimiento == None:
            self.vencimiento = self.pago + timedelta(days=30)
            if self.vencimiento.day != self.pago.day:
                self.vencimiento = self.vencimiento.replace(day=self.pago.day)
        else:
            # esto significa que solo modifico el dia del pago.
            # ! para testear podes sacar esto
            if self.pago > self.vencimiento:
                self.vencimiento = self.pago + timedelta(days=30)
                if self.vencimiento.day != self.pago.day:
                    self.vencimiento = self.vencimiento.replace(day=self.pago.day)

        self.nombre = self.nombre.title()
        self.apellido = self.apellido.title()

        super().save(*args, **kwargs)
        # ? Al poner super() lo que hace es buscar de las clases padres (en este caso models.Model) el metodo que vos le indicas (.save()). al ponerlo asi agregas las lineas de codigo que escribiste y después el resto será igual a lo que indica la clase padre, sirve para mantener la inheritance de la clase padre y no sobreescribir cosas que no queres.
        # ? if you remove the super().save(*args, **kwargs) call, the custom behavior you have defined in your save method will still be executed, but the model instance will not be saved to the database.

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # ? auto_now=True updates the value of the field to the current date and time every time the model is saved to the database. This is useful when you want to keep track of the last time the model was updated.

    # ? auto_now_add=True sets the value of the field to the current date and time when the model is first created and saved to the database. The value of the field is not updated thereafter, even if the model is subsequently saved. This is useful when you want to track the date a record was created.

    # ? null=True means that the field is allowed to be None or null in the database. This applies to all field types, including CharField, IntegerField, and so on.

    # ? blank=True means that the field is allowed to be blank in forms. This applies only to string-based fields such as CharField, TextField, and so on. It has no effect on other field types like IntegerField or DateField.

    # ? it's a good practice to include the *args and **kwargs in case you need to add additional arguments to the save method in the future, or if you are overriding a method that may be called with different arguments by other parts of your code.
    # ? *args is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of arguments to the function, and the function will receive them as a tuple. For example:
    # def foo(*args):
    # for arg in args:
    # print(arg)

    # resultado:
    # foo(1, 2, 3, "four")

    # ? **kwargs is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of keyword arguments to the function, and the function will receive them as a dictionary. For example:
    #     def bar(**kwargs):
    #     for key, value in kwargs.items():
    #         print(key, "=", value)

    # bar(name="Alice", age=30, city="New York")

    # resultado:
    # name = Alice
    # age = 30
    # city = New York


class Asistencia(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE,
    )
    dia = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    activo = models.BooleanField(default=True, editable=False)
    
    
    def save(self, *args, **kwargs):
        # ?This will set self.activo to True if self.usuario.activo is True, and False 
        self.activo = bool(self.usuario.activo)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario} vino {self.dia} a las {self.hora}"
