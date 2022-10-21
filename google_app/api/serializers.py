from dataclasses import field
import email
from unicodedata import name
from rest_framework import serializers
from google_app.models import Accounts,LifeExpectancy

#Json形式のフォーマットに変換してくれる。
class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Accounts
        fields='__all__'
        # json で出力するフィールドを指定することも可能
        # fields = ('user','old','sex','data')

    #パターン1
    # def create(self, validated_data):
        # return User(**validated_data)

    #パターン2
    def create(self, validated_data):
        newVendor = Accounts.objects.create(
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


