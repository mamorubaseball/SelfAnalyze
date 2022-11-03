# SelfAnalyze
自己分析ツールの開発

#　言語の選定
今回は小規模開発になるので、Vueを使うのが得策。

## 機能
- ライフ計算機能
    - 現在の年齢入力と3個程度のアンケートから平均寿命算出
    - 残りのライフを可視化(時間だけではなく、図にする) 
- user登録機能
    - firebaseにメールアドレスとユーザー名を登録
    - ログイン機能
- 各単位ごとに何に時間を使ったのか可視化する
    - googleカレンダーの情報取
    - 年、月、週のセレクト機能
    - 可視化ツール(vue-charts.js)

# 開発手順
- バックエンドからGoogleカレンダーAPIを呼び出す。
- フロントエンドから GoogleカレンダーAPI

# ブランチ
- main⇨本番環境(https://selfanalyze.herokuapp.com/)
- develop⇨ローカル環境

## Vueバージョンの設定
```
vue create selfanalyze
```
- babel
- router
- vuex
- linter
- vue3
