import fdb

try:
    con = fdb.connect(
        host='26.2.70.125',
        port=3050,
        database='C:/Controle/banco/BANCO.FDB',
        user='SYSDBA',
        password='masterkey',
        charset='UTF8'
    )
    cur = con.cursor()
    cur.execute('SELECT * FROM pessoas')  # Tabela sem aspas e com nome maiúsculo 
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Ocorreu um erro durante a conexão ou consulta:")
    print(e)
