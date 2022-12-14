#loggingをimportする
import logging

from flask_debugtoolbar import DebugToolbarExtension

from email_validator import validate_email, EmailNotValidError

#Flaskクラスをimportする

from flask import (Flask, current_app, g, render_template, url_for, redirect, request, flash)
#Flaskクラスをインスタンス化する

app=Flask(__name__)

#SECRET_KEYを追加する
app.config["SECRET_KEY"]="2AZSMss3p5QPbcY2hBsJ"

app.logger.setLevel(logging.DEBUG)

#リダイレクトを中断しない様にする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
#DebugToolbarExtensionにアプリケーションをセットする
toolbar = DebugToolbarExtension(app)

#URLと実行する関数をマッピングする

@app.route("/")
def index():
    return"Hello,Flaskbook!"

@app.route("/hello/<name>",
            methods=["GET","POST"],
            endpoint="hello-endpoint")
def hello(name):
    return f"Hello,{name}!"

#show_nameエンドポイント作成
@app.route("/name/<name>")

def show_name(name):
    return render_template("index.html",name=name)

#contactエンドポイント作成
@app.route("/contact")

def contact():
    return render_template("contact.html")

#contact_completeエンドポイント作成
@app.route("/contact/complete",
                      methods=["GET","POST"])

def contact_complete():
    if request.method == "POST":
        #form属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]     
        description = request.form["description"]
        #入力チェック
        is_valid = True

        if not username:
            flash("ユーザー名は必須です")
            is_valid = False
        
        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))


        #メールを送る

        #contactエンドポイントへリダイレクトする
        flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


with app.test_request_context():
    # /
    print(url_for("index"))
    #/hello/world
    print(url_for("hello-endpoint",name="world"))

    #/name/ichiro?page=1
    print(url_for("show_name",name="ichiro",page="1"))

