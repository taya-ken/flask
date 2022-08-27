#Flaskクラスをimportする

from flask import Flask, render_template, url_for, redirect, request
#Flaskクラスをインスタンス化する

app=Flask(__name__)

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
        #メールを送る

        #contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


with app.test_request_context():
    # /
    print(url_for("index"))
    #/hello/world
    print(url_for("hello-endpoint",name="world"))

    #/name/ichiro?page=1
    print(url_for("show_name",name="ichiro",page="1"))

if __name__ == "__main__":
    app.run(debug=True)
