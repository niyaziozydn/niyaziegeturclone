from rest_framework import serializers
from ozaydinapi.models import NeredenNereye, Cars, Ekstra, YolcuBilgi, YolcuLast

class NeredenNereyeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NeredenNereye
        fields = '__all__'

class CarsSerializer(serializers.ModelSerializer):
    YolculukFiyati = serializers.SerializerMethodField()
    class Meta:
        model = Cars
        fields = ['Cartitle','Cartype','Carfiyat','Carkm','YolculukFiyati']

    def get_YolculukFiyati(self, obj):

        YolculukFiyati = float(obj.Carfiyat * obj.Carkm)
        return round(YolculukFiyati) 

class EkstraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ekstra
        fields = '__all__'

class YolcubilgiSerializer(serializers.ModelSerializer):
    class Meta:
        model = YolcuBilgi
        fields = '__all__'
        
class YolcuLastSerializer(serializers.ModelSerializer):
    class Meta:
        model = YolcuLast
        fields = '__all__'