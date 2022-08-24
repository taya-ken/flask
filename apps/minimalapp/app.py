#Flaskクラスをimportする

from flask import Flask, render_template
#Flaskクラスをインスタンス化する

app=Flask(__name__)

#URLと実行する関数をマッピングする

@app.route("/")
def index():
    return"Hello,Flaskbook!"

@app.route("/hello/<name>",
            methods=["GET","POST"],
            endpoint="hello-endpoint")
def heloo(name):
    return f"Hello,{name}!"

#show_nameエンドポイント作成
@app.route("/name/<name>")

def show_name(name):
    return render_template("index.html",name=name)