from django import forms
from django.contrib.auth.models import User
from .models import Accounts

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応 forms.PasswordInput()
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

# 新規登録フォーム
class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Accounts
        fields = ('old','sex','account_image')
        labels = {'old':"年齢",'sex':"性別",'account_image':"プロフィール画像"}