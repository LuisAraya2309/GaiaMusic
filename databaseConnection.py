import pyodbc  #Driver for Python and SQL Server
def connectToDatabase():
    serverDirection = '127.0.0.1'
    databaseName = 'GaiaMusic'
    userName = 'sa'
    password = 'admin'
    try:
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                serverDirection+';DATABASE='+databaseName+';UID='+userName+';PWD=' + password)
        return connection
    except Exception as e:
        # Atrapar error
        print("Error 666: Database connection failed.")