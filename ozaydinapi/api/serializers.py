from rest_framework import serializers
from ozaydinapi.models import Cars, Yolcular,Yolculuk,YolculuknYolcular, Ekstra

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class YolcularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yolcular
        fields = '__all__'


class EkstraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ekstra
        fields = '__all__'

class YolculukSerializer(serializers.ModelSerializer):
    #data = serializers.SerializerMethodField()
    class Meta:
        model = Yolculuk
        fields = ['cars','yolcusayi','kac_km','nereden','nereye','ekstra'] #data
    def get_data(self, obj):
         data = {}
"""         data["fiyat/euro"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi)) / 30
         data["fiyat/dolar"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi)) / 27 
         data["fiyat/sterlin"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi)) / 25 
         data["fiyat/TL"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi)) 
        
         data["fiyat/euro/ekstra"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi) + ((obj.ekstra.uckopru * 50) + (obj.ekstra.bebekkoltuk * 100 ) +(obj.ekstra.yuksekkoltuk * 150) + (obj.ekstra.onesaat * 50  )   )) / 30 
         data["fiyat/dolar/ekstra"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi) + ((obj.ekstra.uckopru * 50) + (obj.ekstra.bebekkoltuk * 100 ) +(obj.ekstra.yuksekkoltuk * 150) + (obj.ekstra.onesaat * 50  )   )) / 27 
         data["fiyat/sterlin/ekstra"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi) + ((obj.ekstra.uckopru * 50) + (obj.ekstra.bebekkoltuk * 100 ) +(obj.ekstra.yuksekkoltuk * 150) + (obj.ekstra.onesaat * 50  )   )) / 25
         data["fiyat/TL/ekstra"] = (obj.cars.carfiyat * (obj.kac_km * obj.yolcusayi) + ((obj.ekstra.uckopru * 50) + (obj.ekstra.bebekkoltuk * 100 ) +(obj.ekstra.yuksekkoltuk * 150) + (obj.ekstra.onesaat * 50  )   ))

         
 


         
         
         return data
    """



class YolculuknYolcularSerializer(serializers.ModelSerializer):
    yolcular = YolcularSerializer()
    yolculuk = YolculukSerializer()
    class Meta:
        model = YolculuknYolcular
        fields = '__all__'
    