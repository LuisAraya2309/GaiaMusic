#Libraries
from flask import Flask,render_template,request #Flask framework
from databaseConnection import *
#App creation
app = Flask(__name__)

#Database conncection string


#Routes
@app.route('/',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/signIn',methods=['GET','POST'])
def validateUser():
    user = request.form['user']
    password = request.form['password']
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_SignIn ? , ?'
            cursor.execute(query,(user,password))
            queryResult = cursor.fetchall()
            validUser = queryResult[0]
            userType = queryResult[1]
            userPages = {1:'customer.html',2:'admin.html',3:'supplier.html'}
            if validUser != 1:
                return render_template(userPages[userType])
            else:
                return 'Usuario y contraseña inválidos. <a href="/">Intente de nuevo.</a>'        

    except Exception as e:
        return 'Usuario y contraseña inválidos. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()


@app.route('/signUp',methods=['GET','POST'])
def signUp():
    print('Aca va el registro de usuario')




#Run application
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)