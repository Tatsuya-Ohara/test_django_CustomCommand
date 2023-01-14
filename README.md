# test_django_CustomCommand
Djangoカスタムコマンド練習用
基本デフォルト
newapp/management/commands内だけを編集して動作を確認

## 概要

- appフォルダ内にmanagement/commandsディレクトリを作成
- __init__.pyとコマンドを入れるpythonファイルを作成
- コマンドを入れる用のpyファイルにコマンドの詳細を書き込む
- 引数の設定にはadd_argumentsメソッドを使用
- コマンドを使った場合の具体的な動作はhandleメソッドに記述

## 参考URL

### 1. Zenn: [Django]カスタムコマンドを作る

https://zenn.dev/wtkn25/articles/django-custom-command

ごく基本的な使い方の解説
- nargsの値は正規表現のような感じで渡せばOK

### 2. Qiita: Djangoのカスタムコマンドを作成してコマンドラインから実行する

https://qiita.com/checkpoint/items/b6947501774b4008e077

Modelから必要なデータを取得し、コマンドラインに結果を表示する方法
