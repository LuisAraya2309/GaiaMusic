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
            query = 'EXEC sp_SignIn ? , ? , ?'
            cursor.execute(query,(user,password,0))
            queryResult = cursor.fetchall()
            validUser = queryResult[0][0]
            userType = queryResult[0][1]
            
            userPages = {1:'customer.html',2:'admin.html',3:'supplier.html'}
            if validUser != 1:
                return render_template(userPages[userType])
            else:
                return "<script>alert('Usuario y/o Contraseña inválidos');window.location.href = '/';</script>" 

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()

@app.route('/beginSignUp',methods=['GET','POST'])
def beginSignUp():
    return render_template('signUp.html')


@app.route('/signUp',methods=['GET','POST'])
def signUp():
    name = request.form['name']
    lastnames = request.form['lastname']
    user = request.form['user']
    password = request.form['password']
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_SignUp ? , ? , ? , ? , ? , ?'
            cursor.execute(query,(name,lastnames,user,password,'Customer',0))
            queryResult = cursor.fetchall()
            validUser = queryResult[0][0]
            if validUser != 1:
                return render_template('login.html')
            else:
                return "<script>window.location = '/'; alert('Usuario y/o contraseña inválidos.'); </script> " 

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()


#Run application
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)