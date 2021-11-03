#Libraries
from flask import Flask,render_template,request #Flask framework
from databaseConnection import *
#App creation
app = Flask(__name__)


#Global variables
username =""
instrumentName = ""






#Function that creates the HTML for visualizing all the products
def viewProducts():
    queryResult =[]
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_ViewProducts ?'
            cursor.execute(query,(0))
            queryResult = cursor.fetchall()
            
    except Exception as e:
        return  "Error: "+ str(e) 
    
    finally:
        dbConnection.close()


    
    docHTML = '''  <!doctype html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                        <link href="./static/css/products.css" rel="stylesheet" />
                        <title>Products</title>
                    </head>
                    <body>
                        <div class="v903_105">
                        <div class="v903_107"></div>
                        <span class="v903_109">0</span>
                        <div class="v903_110"></div>
                        <span class="v903_111">Gaia 
                        Music </span>
                        <span class="v914_82">Nuestros
                        Productos</span>

                        <a class="solicitarGarantia" href="/startGuarantee">Solicitar garantía</a>

                        <div class="v903_112"></div>
                        <div class="v914_84"></div>
                        <div class="v914_86"></div></div></div>
                    

                        <div class= "container">   
                        
                        '''
    
    columns = 3
    closeRow = 3
    for instrument in queryResult:
        newRow = columns==closeRow
        if newRow:
            docHTML+= '''<div class = "row ">'''
            closeRow+=3

        instrumentName = str(instrument[0])
        detail = str(instrument[1])
        price = str(instrument[2])
        
        docHTML+= ''' <div class="col-12 col-md6 col-lg-4 p-3">
                    <div class="card border-dark text-dark">
                    <div class="card-header">'''
        docHTML+=instrumentName
        docHTML+='''</div>
                    <div class="card-body">
                        <p class="card-text">
                            <dl class="row">
                                <dt class="col-sm-4">Nombre:</dt>
                                <dd class="col-sm-8">'''

        docHTML+=instrumentName
        docHTML+='''</dd><dt class="col-sm-4">Descripción:</dt><dd class="col-sm-8">'''
        docHTML+=detail
        docHTML+='''</dd><dt class="col-sm-4">Precio:</dt> <dd class="col-sm-8">'''
        docHTML+=price
        docHTML+='''</dd></dl> </p>
        <form action = '/buyProduct' method = 'post'>
        <input type ="hidden" id = "instrumentName" name = "instrumentName" value = "'''
        docHTML+=(instrumentName)
        docHTML+='''" >'''
        docHTML+='''<input type = "submit" value = "Comprar producto" class = "btn btn-primary">
        </form>
        </div> </div></div>'''
        


        columns+=1
        if columns==closeRow:
            docHTML+=''' </div>'''


    docHTML+='''</body>
                </html>
             '''
    return docHTML






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
            
            userPages = {2:'ModifInventario.html',3:'supplier.html'}
            if validUser != 1:
                global username
                username = user
                if userType == 1:
                    return render_template(viewProducts())
                else:
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
        return str(e) + 'Exception error aquiiiiiiii. <a href="/">Intente de nuevo.</a>'
    
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

@app.route('/startGuarantee',methods=['GET','POST'])
def startGuarantee():
    return render_template('guarantee.html')


@app.route('/guarantee',methods=['GET','POST'])
def guarantee():
    productName = request.form['productName']
    saleDate = request.form['saleDate']
    detail = request.form['detail']
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_RequestWarranty ?,?,?,?,?'
            cursor.execute(query,(username,productName,saleDate,detail,0))
            queryResult = cursor.fetchall()
            resultCode = queryResult[0][0]
            if resultCode != 1:
                return render_template('guarantee.html') + '''<div class="window-notice" id="window-notice" >
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
                                            window.location.href="/startGuarantee";
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
                                            
                                        });
                            </script>
                            '''

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()


#Buy product
@app.route('/buyProduct',methods=['GET','POST'])
def buyProduct():
    global instrumentName
    try:
        instrumentName = request.form['instrumentName']
    except:
        pass
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_SelectProduct ?,? '
            cursor.execute(query,(instrumentName,0))
            queryResult = cursor.fetchall()

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()
    
    instrument = queryResult[0]
    

    instrumentName = str(instrument[0])
    detail = str(instrument[1])
    price = str(instrument[2])
    stockAmount = str(instrument[3])

    docHTML = ''' <!DOCTYPE html>
                    <html>
                        <head>
                            <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                            <link href="./static/css/buy.css" rel="stylesheet" />

                            <title>Comprar Productos</title>
                            '''
    docHTML+='''<style type = "text/css">
                        div.v814_165{
                            width: 243px;
                            height: 270px;
                            background: url("./static/images/'''
    docHTML+=instrumentName
    docHTML+='''.jpg");
                            background-repeat: no-repeat;
                            background-position: center center;
                            background-size: cover;
                            opacity: 1;
                            position: absolute;
                            top: 147px;
                            left: 74px;
                            border-top-left-radius: 112px;
                            border-top-right-radius: 112px;
                            border-bottom-left-radius: 112px;
                            border-bottom-right-radius: 112px;
                            overflow: hidden;
                            }
                        </style>
                        </head>
                        <body>
                            <div class="v814_139">
                                <div class="v814_140">
                                    <div class="v814_141"></div>
                                    <div class="v814_142"></div>
                                    <div class="v814_143"></div>
                                    <span class="v814_144">Buscar...</span>
                                    <span class="v814_145">0</span>
                                    <span class="v814_146">Cantidad en  inventario: </span>
                                    <textarea class = "productDetail" readonly="readonly" style="overflow:hidden">'''
    docHTML+=detail
    docHTML+='''</textarea >
                <span class="v814_147">Duración de la garantía:</span>
                <span class="v814_150">Precio total: </span>
                <div class="v912_82"></div>
                <div class="v912_85"></div>
                <form action = '/buyingProduct' method='post'>
                    <input type= "submit" class="v912_85" value="Comprar Producto"> </input>
                </form>
                <span class="v912_83">Agregar a carrito</span>
                <div class="v814_158"></div>
                <span class="v814_159">Gaia Music </span>
                <div class="v814_160"></div>
                <span class="v815_140">Información de compra</span>
                <div class="v912_86"></div>
                <div class="v912_87"></div>
                <div class="v912_88"></div>
                <span class="itemsInStock">'''
    docHTML+=stockAmount
    docHTML+='''</span>
                <span class="warranty">1 año</span>
                <span class="totalPrice">'''
    docHTML+=price
    docHTML+='''</span>
                        </div>
                        <div class="v814_161"></div>
                        <div class = "v814_165">
                        </div>
                    </div>
                </body>
            </html>'''
    return docHTML
    
@app.route('/buyingProduct',methods=['GET','POST'])
def finishBuy():
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_BuyProduct ?,?,?,? '
            cursor.execute(query,(instrumentName,username,1,0))
            queryResult = cursor.fetchall()
            resultCode = queryResult[0][0]

            if resultCode==0:
                return '''<html>
                                <head>
                                    <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                                    <link href="./static/css/buy.css" rel="stylesheet" />
                                </head>
                                <body> 
                                    <div class="window-notice" id="window-notice" >
                                        <div class="content">
                                            <div class="content-text">Se ha realizado su compra con éxito.
                                            </div>
                                            <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                        </div>
                                    </div>
                                    <script>
                                                let close_button = document.getElementById('close-button');
                                                    close_button.addEventListener("click", function(e) {
                                                    e.preventDefault();
                                                    document.getElementById("window-notice").style.display = "none";
                                                    window.location.href="/buyProduct";
                                                });
                                    </script>
                                </body>

                                </html>
                                ''' 
            else:
                return '''<div class="window-notice" id="window-notice" >
                                    <div class="content">
                                        <div class="content-text">Se ha realizado su compra con éxito.
                                        </div>
                                        <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                    </div>
                                </div>
                                <script>
                                            let close_button = document.getElementById('close-button');
                                                close_button.addEventListener("click", function(e) {
                                                e.preventDefault();
                                                document.getElementById("window-notice").style.display = "none";
                                                window.location.href="/buyProduct";
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