import pymysql
from config import DB_CONFIG

def get_connection():
    return pymysql.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database'],
        cursorclass=getattr(pymysql.cursors, DB_CONFIG['cursorclass'])
    )

def executar_query(query):
    conn = None
    try:
        conn = get_connection()
        print("Conexão ao MySQL bem-sucedida!")
        with conn.cursor() as cursor:
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
    except pymysql.Error as e:
        print(f"Erro ao conectar ao MySQL ou ao executar a query: {e}")
        return None
    finally:
        if conn:
            conn.close()

def inserir_dados(query):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return True
    except pymysql.Error as e:
        print(f"Erro ao conectar ao MySQL ou ao executar a query de inserção: {e}")
        return False
    finally:
        if conn:
            conn.close()

def atualizar_dados(query):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return True
    except pymysql.Error as e:
        print(f"Erro ao conectar ao MySQL ou ao executar a query de atualização: {e}")
        return False
    finally:
        if conn:
            conn.close()
