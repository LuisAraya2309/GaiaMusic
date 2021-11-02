#Libraries
from flask import Flask,render_template,request #Flask framework
from databaseConnection import *
#App creation
app = Flask(__name__)


#Global variables
username =""




#Function that creates the HTML for visualizing all the products
def viewProducts():
    
    docHTML = ''''''





#Routes
@app.route('/',methods=['GET'])   #Login page
def login():
    return render_template('login.html')

@app.route('/signIn',methods=['GET','POST'])  #Sign in
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
            
            userPages = {1:'products.html',2:'ModifInventario.html',3:'supplier.html'}
            if validUser != 1:
                global username
                username = user
                return render_template(userPages[userType])
            else:
                return render_template('login.html') + '''<div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">Usuario o contraseña inválido. Vuelva a intentarlo.
                                    <a href="/beginSignUp">Registrarse</a></div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            window.location.href="/";
                                        });
                            </script>
                            '''

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
    address = request.form['address']
    user = request.form['user']
    password = request.form['password']
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_SignUp ? , ? , ? , ? , ? , ?'
            cursor.execute(query,(name,address,user,password,'Customer',0))
            queryResult = cursor.fetchall()
            validUser = queryResult[0][0]
            if validUser != 1:
                return render_template('login.html') + '''<div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">Su cuenta se ha registrado con éxito.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            window.location.href="/";
                                        });
                            </script>
                            '''
            else:
                return render_template('signUp.html') + '''<div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">El nombre de usuario elegido ya existe. Ingrese uno nuevo.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            window.location.href="/beginSignUp";
                                        });
                            </script>
                            '''

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()


@app.route('/modifyProducts',methods=['GET','POST'])
def modifyProducts():
    productName = request.form['oldName']
    newName = request.form['newName']
    stock = request.form['inStock']
    category = request.form['category']
    price = request.form['price']
    information = request.form['productInformation']
    
    dbConnection = connectToDatabase()
    
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_ModifyInstrument ? , ? , ? , ? , ? , ?, ? ,?'
            cursor.execute(query,(category,username,productName,newName,information,price,stock,0))
            queryResult = cursor.fetchall()
            resultCode = queryResult[0][0]
            if resultCode != 1:
                return render_template('ModifInventario.html') + '''<div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">El instrumento se ha modificado con éxito.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            
                                        });
                            </script>
                            '''
            else:
                return render_template('ModifInventario.html') + '''<div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">El instrumento a modificar no existe.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            
                                        });
                            </script>
                            '''

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()

@app.route('/deleteProducts',methods=['GET','POST'])
def deleteProducts():
    productName = request.form["productToEliminate"]
    dbConnection = connectToDatabase()
    
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_DeleteInstrument ? , ? , ?'
            cursor.execute(query,(productName,username,0))
            queryResult = cursor.fetchall()
            resultCode = queryResult[0][0]
            if resultCode != 1:
                return render_template('login.html')
            else:
                return "<script>alert('No existe el articulo a eliminar.'); </script> " 

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()


@app.route('/guarantee',methods=['GET','POST'])
def guarantee():
    productName = request.form['productName']
    saleDate = request.form['saleDate']
    detail = request.form['detail']
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_RequestWarranty ? , ? , ?, ?, ?'
            cursor.execute(query,(username,productName,saleDate,detail,0))
            queryResult = cursor.fetchall()
            resultCode = queryResult[0][0]
            if resultCode != 1:
                return render_template('login.html') + '''<div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">Su solicitud de garantía se ha registrado con éxito.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            window.location.href="/";
                                        });
                            </script>
                            ''' 
            else:
                return render_template('guarantee.html') + '''<div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">Los datos suministrados para la solicitud de la garantía no son válidos.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            window.location.href="/beginSignUp";
                                        });
                            </script>
                            '''

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()


#Run application
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)