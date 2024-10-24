from flask import Flask, jsonify, Blueprint



def runwebsite():
    app = Flask(__name__, template_folder='Template ')
    app.config['SECRET_KEY'] = 'Hans'
    from Homepage import homepage
    from Auth import auth

    app.register_blueprint(homepage,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

