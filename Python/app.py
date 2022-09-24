from divar.app import app 

#divar


import divar.models as models
models.db.create_all()
models.db.create_all()
#//////////////////////////////////////

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8080)
