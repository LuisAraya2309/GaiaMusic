#Libraries
from flask import Flask,render_template,request #Flask framework
from databaseConnection import *
import json
#App creation
app = Flask(__name__)


#Global variables
username =""
instrumentName = ""

#Function that creates the HTML for record products
def starGuarantee():
    recordProductsInformation = []
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_ViewRecordProducts ?,?'
            cursor.execute(query,(username,0))
            recordProductsInformation = cursor.fetchall()
            
    except Exception as e:
        return  "Error: "+ str(e) 
    
    finally:
        dbConnection.close()

    recordProductsDicc = {}
    productId = 1
    for product in recordProductsInformation:
        productTitle = product[0]
        transactionDate = product[1]
        price = product[2]
        warranty = product[3]
        recordProductsDicc[productId] = {'productTitle':productTitle,'transactionDate':transactionDate,'price':price,'warranty':warranty}
        productId+=1
    
        
    docHTML = '''<!DOCTYPE html>
                    <html>
                        <head>
                            <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                            <link href="./static/css/warrantyStyle.css" rel="stylesheet" />
                            <title>Document</title>
                        </head>
                        <body>
                            <div class="v802_82">
                                <div class="v802_83">
                                    <div class="v812_107"></div>
                                    <div class="v812_109"></div>
                                    <div class="v802_104"></div>
                                    <span class="v802_84">Gaia Music </span>
                                    <span class="v812_108">Buscar...</span>
                                    <span class="v812_110">0</span>
                                    <span class="v802_92">Historial de compras</span>

                                    <form method = "post" action = "/guarantee" class = "v802_87">
                                        <textarea id = "detail" name = "detail" class="v956_91" ></textarea>
                                        <span class="v802_103">Solicitar garantía</span>
                                        <span class="v957_82">Productos Comprados</span>
                                        <span class="v956_92">Motivo de la solicitud:</span>
                                        <input id = "requestWarranty" name = "requestWarranty"  type = "submit" class="v802_98" value = "Solicitar garantia" ></input>
                                        <select id = "selectProduct" name = "selectProduct" class = "selectProduct" aria-label="Default select example">
                                        <option selected>Productos disponibles</option>
                                        '''
    #Id for list options
    idOption = 1
    #Append 
    
    for productId in recordProductsDicc:
        product = recordProductsDicc[productId]
        if product['warranty'] == 1:
            docHTML+= '''<option id="'''
            docHTML+=str(idOption)
            docHTML+='''" value ="'''
            docHTML+=str(product['productTitle'])
            docHTML+='''  - '''
            docHTML+=str(product['transactionDate'])
            docHTML+='''" >'''
            docHTML+=str(product['productTitle'])
            docHTML+=''' - Precio final: '''
            docHTML+=str(product['price'])
            docHTML+=''' - Fecha de compra: '''
            docHTML+=str(product['transactionDate'])
            docHTML+='''</option>'''
            idOption+=1
    
    docHTML+= '''
                                </select>
                                </form>
                                    
                                    <div class="v812_137"></div>
                                </div>
                                <div class="v812_138"></div>
                            </div>
                        </body>
                    </html>
            '''
    return docHTML



#Function that creates the HTML for modifying the products

@app.route('/returnModifyingProducts',methods=['GET']) 
def modifyingProducts():
    productsInformation = []
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_ViewProducts ?'
            cursor.execute(query,(0))
            productsInformation = cursor.fetchall()
            
    except Exception as e:
        return  "Error: "+ str(e) 
    
    finally:
        dbConnection.close()
        
    productsDicc = {}
    productId = 1
    for product in productsInformation:
        productTitle = product[0]
        productsDicc[productId] = {'productTitle':productTitle}
        productId+=1
    
    
        
    docHTML = '''<!DOCTYPE html>
                <html>
                    <head>
                        <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                        <link href="./static/css/InventarioStyle.css" rel="stylesheet" />
                        <title>Modificar Inventario</title>
                    </head>
                    <body>
                        <div class="v812_111">
                            <div class="v812_112">
                                <div class="v812_113"></div>
                                <div class="v812_114"></div>

                                <form action = "/modifyProducts" method = "post" class="Form1">
                                    <div class = "RectanguloGrande"> </div>
                                    <span class="v812_119">Nuevo nombre </span>
                                    <span class="v812_120">Modificar Inventario</span>
                                    <span class="v812_121">Información</span>
                                    <span class="v850_96">Categoría</span>
                                    <span class="v850_88">Cantidad en Inventario</span>
                                    <span class="v849_84">Nombre del producto a cambiar</span>
                                    <span class="v812_134">Precio</span>
                                    <input class = "RealizarCambio" type = "submit" value = "Realizar cambio"></input>
                                    <input class="v848_83" id = "newName" name = "newName" required =""></input>
                                    <input class="v849_85" id = "oldName" name = "oldName"></input>
                                    <input pattern ="[0-9]*" title="Recuerde que debe ser un valor monetario." class="v812_125" id = "price" name = "price" required =""></input>
                                    <input type= "text" pattern ="[0-9]*" title="Recuerde que debe ser un valor entero." class="v850_89" id = "inStock" name = "inStock" required =""></input>
                                    <input class="v850_95" id = "category" name = "category" required =""></input>
                                    <input class="v812_126" id = "productInformation" name = "productInformation" required =""></input>

                                </form>

                                <span class="v812_118">0</span>
                                <span class="v812_117">Buscar...</span>

                                <form action="/deleteProducts" method="post" class = "Form2">
                                    <div class="RectanguloPequeño"></div>
                                    <span class="v850_91">Nombre del producto a eliminar</span>
                    
                                    
                                    <span class="v850_94">Eliminar producto</span>
                                    <input class = "EliminarProducto" type = "submit" value = "Eliminar producto"></input>
                                    <select id = "productName" name = "productName" class="v850_92" aria-label="Default select example">
                                    <option selected>Productos disponibles</option>
                                    '''
    #Id for list options
    idOption = 1
    #Append 
    
    for productId in productsDicc:
        product = productsDicc[productId]
        docHTML+= '''<option id="'''
        docHTML+=str(idOption)
        docHTML+='''" value ="'''
        docHTML+=str(product['productTitle'])
        docHTML+='''" >'''
        docHTML+=str(product['productTitle'])
        docHTML+='''</option>'''
        idOption+=1
    
    docHTML+= '''
                </select>
                </form>

                <div class="v812_123"></div>
                <div class="v850_93"></div>
                
                <div class="v812_129"></div>
                <span class="v812_130">Gaia Music </span>
                <div class="v813_85"></div>
            
        
            </div>
            <div class="v812_136"></div>
            
        </div>
    </body>
    </html>
    '''
    return docHTML
    

#Function that creates the HTML for managing the orders

def manageOrders():
    ordersInformation =[]
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_ViewOrders ?,?'
            cursor.execute(query,(username,0))
            ordersInformation = cursor.fetchall()
            
    except Exception as e:
        return  "Error: "+ str(e) 
    
    finally:
        dbConnection.close()
    
    ordersDicc = {}
    orderId = 1
    for order in ordersInformation:
        idOrder = order[1]
        detail = order[2]
        date = order[3]
        status = order[4]
        ordersDicc[orderId] = {'idOrder':idOrder,'detail':detail,'date':date,'status':status}
        orderId+=1
    
    docHTML = '''<!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8">
                    <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                    <link href="./static/css/kanban.css" rel="stylesheet" />
                    <title>Administrar encargos</title>

                </head>
                <body>

                    <div class="v922_91">
                        <div class="v922_92">
                            <div class="v922_93"></div>
                            <div class="v922_94"></div>
                            <span class="v922_96">Buscar...</span>
                            <span class="v922_97">0</span>
                            <div class="v922_107"></div>
                            <span class="v922_108">Gaia Music </span>
                            <div class="v922_109"></div>
                            <span class = "Titulo">Gestionar encargos</span>
                            <div class="imagen1"></div>
                            <div class="imagen2"></div>
                            <div class="imagen3"></div>
                            <div class="imagen4"></div>
                        </div>
                        <div class="v922_110"></div>

                    </div>

                    <script >
                        function updateOrderStatus(){
                            var todoCards = document.getElementById('todo').getElementsByClassName('card');
                            var doingCards = document.getElementById('doing').getElementsByClassName('card');
                            var doneCards = document.getElementById('done').getElementsByClassName('card');

                            var todo = [];
                            var doing = [];
                            var done = [];

                            for(var i =0;i<todoCards.length;i++){
                                todo.push(todoCards[i].innerHTML)
                            }

                            
                            for(var i =0;i<doingCards.length;i++){
                                doing.push(doingCards[i].innerHTML)
                            }

                            
                            for(var i =0;i<doneCards.length;i++){
                                done.push(doneCards[i].innerHTML)
                            }

                            var sendJSON = {'ToDo':todo,'Doing':doing,'Done':done};
                            sendJSON = JSON.stringify(sendJSON);
                            document.getElementById('json').value = sendJSON;
                        }
                        
                    </script>


                    <form action = "/orderStatus" class = "form1" method="post">
                        <div id="board">
                            <div id="todo" class="section">
                                <h1>Por hacer</h1>'''
    #Id for cards
    idC = 1
    #Append the todo orders
    for orderId in ordersDicc:
        order = ordersDicc[orderId]
        if order['status'] == 'ToDo':
            docHTML+= '''<div id="'''
            docHTML+=str(idC)
            docHTML+='''" class="card">'''
            docHTML+='''Orden #'''
            docHTML+=str(order['idOrder'])
            docHTML+=''':<br>'''
            docHTML+=str(order['detail'])
            docHTML+="<br> Fecha: "
            docHTML+=str(order['date'])
            docHTML+='''</div>'''
            idC+=1
    
    docHTML+='''</div>
            <div id="doing" class="section">
                <h1>En proceso</h1>'''
    
    #Append the doing orders
    for orderId in ordersDicc:
        order = ordersDicc[orderId]
        if order['status'] == 'Doing':
            docHTML+= '''<div id="'''
            docHTML+=str(idC)
            docHTML+='''" class="card">'''
            docHTML+='''Orden #'''
            docHTML+=str(order['idOrder'])
            docHTML+=''':<br>'''
            docHTML+=str(order['detail'])
            docHTML+="<br> Fecha: "
            docHTML+=str(order['date'])
            docHTML+='''</div>'''
            idC+=1

    docHTML+='''</div>
                        <div id="done" class="section">
                            <h1>Finalizado</h1>
                        </div>
                    </div>

                    <input type="hidden" id="json" name="json" value="blabla">
                    <input class = "updateButton" type = "submit" onclick = "updateOrderStatus()" value="Aplicar Cambios"> </input>

                    </form>
                    <script>
                        var cards = document.querySelectorAll('.card');

        for (var i = 0, n = cards.length; i < n; i++) {
            var card = cards[i];
            card.draggable = true;
        };

        var board = document.getElementById('board');

        var hideMe;

        board.onselectstart = function(e) {
            e.preventDefault();
        }

        board.ondragstart = function(e) {
            console.log('dragstart');
            hideMe = e.target;
            e.dataTransfer.setData('card', e.target.id);
            e.dataTransfer.effectAllowed = 'move';
        };

        board.ondragend = function(e) {
            e.target.style.visibility = 'visible';
        };

        var lastEneterd;

        board.ondragenter = function(e) {
            console.log('dragenter');
            if (hideMe) {
                hideMe.style.visibility = 'hidden';
                hideMe = null;
            }
            // Save this to check in dragleave.
            lastEntered = e.target;
            var section = closestWithClass(e.target, 'section');
            // TODO: Check that it's not the original section.
            if (section) {
                section.classList.add('droppable');
                e.preventDefault(); // Not sure if these needs to be here. Maybe for IE?
                return false;
            }
        };

        board.ondragover = function(e) {
            // TODO: Check data type.
            // TODO: Check that it's not the original section.
            if (closestWithClass(e.target, 'section')) {
                e.preventDefault();
            }
        };

        board.ondragleave = function(e) {
            // FF is raising this event on text nodes so only check elements.
            if (e.target.nodeType === 1) {
                // dragleave for outer elements can trigger after dragenter for inner elements
                // so make sure we're really leaving by checking what we just entered.
                // relatedTarget is missing in WebKit: https://bugs.webkit.org/show_bug.cgi?id=66547
                var section = closestWithClass(e.target, 'section');
                if (section && !section.contains(lastEntered)) {
                    section.classList.remove('droppable');
                }
            }
            lastEntered = null; // No need to keep this around.
        };

        board.ondrop = function(e) {
            var section = closestWithClass(e.target, 'section');
            var id = e.dataTransfer.getData('card');
            if (id) {
                var card = document.getElementById(id);
                // Might be a card from another window.
                if (card) {
                    if (section !== card.parentNode) {
                        section.appendChild(card);
                    }
                } else {
                    alert('could not find card #' + id);
                }
            }
            section.classList.remove('droppable');
            e.preventDefault();
        };

        function closestWithClass(target, className) {
            while (target) {
                if (target.nodeType === 1 &&
                    target.classList.contains(className)) {
                    return target;
                }
                target = target.parentNode;
            }
            return null;
        }
                    </script>
                </body>
                </html>
                '''
    return docHTML

    
    
    
    




#Function that creates the HTML for visualizing all the products

@app.route('/returnViewProducts',methods=['GET']) 
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

            if validUser != 1:
                global username
                username = user
                if userType == 1:
                    return viewProducts()
                elif userType == 3:
                    return manageOrders()
                else:
                    return modifyingProducts()
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
            cursor.execute(query,(name,address,user,password,'Cliente',0))
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
                return  '''
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                                <link href="./static/css/InventarioStyle.css" rel="stylesheet" />
                                <title>Modificar Inventario</title>
                            </head>
                            <div class="window-notice" id="window-notice" >
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
                                            window.location.href="/returnModifyingProducts";
                                        });
                            </script>
                            '''
            else:
                return  '''
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                                <link href="./static/css/InventarioStyle.css" rel="stylesheet" />
                                <title>Modificar Inventario</title>
                            </head>
                            <div class="window-notice" id="window-notice" >
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
                                            window.location.href="/returnModifyingProducts";
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
    productName = request.form["productName"]
    dbConnection = connectToDatabase()
    
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_DeleteInstrument ? , ? , ?'
            cursor.execute(query,(productName,username,0))
            queryResult = cursor.fetchall()
            resultCode = queryResult[0][0]

            if resultCode != 1:
                return '''
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                                <link href="./static/css/InventarioStyle.css" rel="stylesheet" />
                                <title>Modificar Inventario</title>
                            </head>
                            
                            <div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">El instrumento se ha eliminado con éxito.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            window.location.href="/returnModifyingProducts";
                                        });
                            </script>
                            '''
            else:
                return '''
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                                <link href="./static/css/InventarioStyle.css" rel="stylesheet" />
                                <title>Modificar Inventario</title>
                            </head>
                            
                            <div class="window-notice" id="window-notice" >
                                <div class="content">
                                    <div class="content-text">El instrumento no se ha podido eliminar.
                                    </div>
                                    <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                </div>
                            </div>
                            <script>
                                        let close_button = document.getElementById('close-button');
                                            close_button.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            document.getElementById("window-notice").style.display = "none";
                                            window.location.href="/returnModifyingProducts";
                                            
                                        });
                            </script>
                            '''

    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()

@app.route('/startGuarantee',methods=['GET','POST'])
def startGuarantee():

    return starGuarantee()

@app.route('/guarantee',methods=['GET','POST'])
def guarantee():
    completeInformation = request.form['selectProduct']
    detail = request.form['detail']
    productName = completeInformation[0:completeInformation.find("-")-1]
    saleDate = completeInformation[completeInformation.find("-")+1:]
    dbConnection = connectToDatabase()
    try:
        with dbConnection.cursor() as cursor:
            query = 'EXEC sp_RequestWarranty ?,?,?,?,?'
            cursor.execute(query,(username,productName,saleDate,detail,0))
            queryResult = cursor.fetchall()
            resultCode = queryResult[0][0]
            if resultCode != 1:
                return  '''
                            <head>
                                <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                                <link href="./static/css/warrantyStyle.css" rel="stylesheet" />
                            </head>
                            <body> 
                                <div class="window-notice" id="window-notice" >
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
                                                window.location.href="/returnViewProducts";
                                            });
                                </script>
                            </body>
                            ''' 
            else:
                return '''
                            <head>
                                <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                                <link href="./static/css/warrantyStyle.css" rel="stylesheet" />
                            </head>
                            <body> 
                                <div class="window-notice" id="window-notice" >
                                    <div class="content">
                                        <div class="content-text">La garantía del producto seleccionado está obsoleta.
                                        </div>
                                        <div class="content-buttons"><a href="#" id="close-button">Aceptar</a></div>
                                    </div>
                                </div>
                                <script>
                                            let close_button = document.getElementById('close-button');
                                                close_button.addEventListener("click", function(e) {
                                                e.preventDefault();
                                                document.getElementById("window-notice").style.display = "none";
                                                window.location.href="/returnViewProducts";
                                            });
                                </script>
                            </body>
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
                                                    window.location.href="/returnViewProducts";
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
                                                window.location.href="/returnViewProducts";
                                            });
                                </script>
                                ''' 


    except Exception as e:
        print(e)
        return str(e) + 'Exception error. <a href="/">Intente de nuevo.</a>'
    
    finally:
        dbConnection.close()

@app.route('/orderStatus',methods=['GET','POST'])
def updateOrderStatus():
    ordersStatus = request.form['json']
    ordersStatus = json.loads(ordersStatus)
    
    for status in ordersStatus:
        if ordersStatus[status]!=[]:
            for order in ordersStatus[status]:
                begin = order.find('#')
                end = order.find(':')
                orderId = order[begin+1:end]
                try:
                    dbConnection = connectToDatabase()
                    with dbConnection.cursor() as cursor:
                        query = 'EXEC sp_UpdateOrderStatus ?,?,?'
                        cursor.execute(query,(status,orderId,0))
                        queryResult = cursor.fetchall()
                        resultCode = queryResult[0][0]
                        
                except Exception as e:
                    return str(e)
                finally:
                     dbConnection.close()

    return manageOrders() + '''<html>
                    <head>
                        <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" rel="stylesheet" />
                        <link href="./static/css/buy.css" rel="stylesheet" />
                    </head>
                    <body> 
                        <div class="window-notice" id="window-notice" >
                            <div class="content">
                                <div class="content-text">Se han aplicado los cambios con éxito.
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
                    </body>

                    </html> 
                    ''' 






#Run application
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)