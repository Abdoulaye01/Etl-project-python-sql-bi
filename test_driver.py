import pyodbc

try:

    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};'
                          'SERVER=ip_address,1433;'   # Use the actual IP and port of your SQL Server
                          'DATABASE=master;'
                          'UID=admin;'                # SQL Server username
                          'PWD=password;'             # SQL Server password
                          'Encrypt=yes;'              # Enable encryption
                          'TrustServerCertificate=yes;')  # Bypass certificate validation
    print("Connection successful")
except pyodbc.Error as e:
    print("Connection failed: ", e)



# import pyodbc
# print(pyodbc.drivers())
