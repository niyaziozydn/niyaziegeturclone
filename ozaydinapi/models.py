from django.db import models

# Create your models here.


class Cars(models.Model):
    cartitle = models.CharField(max_length=200,blank=True,null=True)
    cartype = models.CharField(max_length=200,blank=True,null=True)
    carperkm= models.IntegerField(blank=True,null=True)
    carcreated = models.DateTimeField(auto_now_add=True)
    carfiyat = models.IntegerField(blank=True,null=True)
    carimage = models.ImageField(upload_to="media/cars",blank=True,null=True)

    def __str__(self):
        return self.cartitle

class Ekstra(models.Model):
    uckopru = models.IntegerField(blank=True,null=True)
    bebekkoltuk = models.IntegerField(blank=True,null=True)
    yuksekkoltuk = models.IntegerField(blank=True,null=True)
    onesaat = models.IntegerField(blank=True,null=True)

    
class Yolculuk(models.Model):
    cars = models.ForeignKey(Cars,on_delete=models.SET_NULL,null=True)
    ekstra = models.ForeignKey(Ekstra,on_delete=models.SET_NULL,null=True)
    yolcusayi = models.IntegerField(blank=True,null=True)
    kac_km = models.IntegerField(blank=True,null=True)
    nereden = models.CharField(max_length=200,blank=True,null=True)
    nereye = models.CharField(max_length=200,blank=True,null=True)

class Yolcular(models.Model):
    yolculuk = models.ForeignKey(Yolculuk,on_delete=models.SET_NULL,null=True)
    isim = models.CharField(max_length=200,blank=True,null=True)
    soy_isim = models.CharField(max_length=200,blank=True,null=True)
    yas = models.IntegerField(blank=True,null=True)
    tc = models.IntegerField(blank=True,null=True)
    uyruk = models.CharField(max_length=200,blank=True,null=True)
    cinsiyet = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.isim

class YolculuknYolcular(models.Model):
    yolcular = models.ForeignKey(Yolcular,on_delete=models.SET_NULL,null=True)
    yolculuk = models.ForeignKey(Yolculuk,on_delete=models.SET_NULL,null=True)





