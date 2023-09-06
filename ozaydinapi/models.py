from django.db import models

# Create your models here.


class Cars(models.Model):
    Cartitle = models.CharField(max_length=150,blank=True,null=True)
    Cartype = models.CharField(max_length=100,blank=True,null=True)
    Carfiyat = models.CharField(max_length=100,blank=True,null=True)
    Carkm = models.IntegerField(blank=True,null=True)


class NeredenNereye(models.Model):
    car = models.ForeignKey(Cars,on_delete=models.SET_NULL,null=True)
    Nereden = models.CharField(max_length=100,blank=True,null=True)
    Nereye = models.CharField(max_length=50,blank=True,null=True)
    Yolcu = models.IntegerField(blank=True,null=True)





class Ekstra(models.Model):
    Kopru = models.IntegerField(blank=True,null=True)
    Bebekkoltuk = models.IntegerField(blank=True,null=True)
    Yuksekkoltuk = models.IntegerField(blank=True,null=True)
    saatekstra = models.IntegerField(blank=True,null=True)


class YolcuBilgi(models.Model):
    ekstra = models.ForeignKey(Ekstra,on_delete=models.SET_NULL,null=True)
    isim = models.CharField(max_length=150,blank=True,null=True)
    soyisim = models.CharField(max_length=150,blank=True,null=True)
    yas = models.IntegerField(blank=True,null=True)
    uyruk = models.CharField(max_length=100,blank=True,null=True)
    ekbilgi = models.CharField(max_length=150,blank=True,null=True)

class YolcuLast(models.Model):
    neredennereye= models.ForeignKey(NeredenNereye,on_delete=models.SET_NULL,null=True)
    yolcubilgi= models.ForeignKey(YolcuBilgi,on_delete=models.SET_NULL,null=True)







