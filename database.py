import pyrebase
#banco de dados

config= {
    "apiKey": "AIzaSyDpRH3tU_e1KABihAF-CteYjCbtW4yqCAs",
    "authDomain": "gamificacao-3b8d0.firebaseapp.com",
    "projectId": "gamificacao-3b8d0",
    "storageBucket": "gamificacao-3b8d0.appspot.com",
    "messagingSenderId": "574966019275",
    "appId": "1:574966019275:web:74ad6374f89c2ddbf4574e",
    "measurementId": "G-KEZNWR2YZG"
}

firebase = pyrebase.initialize_app(config)
dados = firebase.database()
dados.child().update({})