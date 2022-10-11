from dataclasses import field
import email
from unicodedata import name
from rest_framework import serializers
from google_app.models import User,LifeExpectancy

#Json形式のフォーマットに変換してくれる。
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        # json で出力するフィールドを指定することも可能
        # fields = ('id','user_name', 'birth_day','age','created_at')

    #パターン1
    # def create(self, validated_data):
        # return User(**validated_data)

    #パターン2
    def create(self, validated_data):
        newVendor = User.objects.create(
        name = validated_data["name"],
        email = validated_data["email"],
        old = validated_data["old"],
        sex = validated_data["sex"],
        data = validated_data["data"],
    )
        newVendor.save()
        return newVendor

    #updateメソッドをオーバーライド
    #PUTリクエストを可能にする
    def update(self, instance, validated_data):
        instance.name = str(validated_data["name"]),
        instance.email = str(validated_data["email"]),
        instance.old =int(validated_data["old"]),
        instance.sex = str(validated_data["sex"]),
        instance.data = validated_data["data"],
        instance.save()
        return instance

class LifeSeializer(serializers.ModelSerializer):
    class Meta:
        model = LifeExpectancy
        fields ='__all__'

    def create(self,validated_data):
        newVendor = LifeExpectancy.objects.create(
        year = validated_data["year"],
        old_list_men = validated_data["old_list_men"],
        old_list_women = validated_data["old_list_women"],
    )
        newVendor.save()
        return newVendor


