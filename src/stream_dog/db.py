import pymysql.cursors
import os

def get_conn():
#  conn = pymysql.connect(host=os.getenv("DB_IP", "localhost"),
#                            port=int(os.getenv("MY_PORT", 53306)),
#                            user = 'mnist', password = '1234',
#                            database = 'mnistdb',
#                            cursorclass=pymysql.cursors.DictCursor)
    # 여기 ip나 port나 비번이나 다 바꾸기
  conn = pymysql.connect(host=os.getenv("DB_IP","localhost"),
                            port=int(os.getenv("MY_PORT", 53306)),
                            user = 'mnist', password = '1234',
                            database = 'mnistdb',
                            cursorclass=pymysql.cursors.DictCursor)
  return conn


def select(query: str, size = -1):
  conn = get_conn()
  with conn:
      with conn.cursor() as cursor:
          cursor.execute(query)
          result = cursor.fetchmany(size)

  return result


def dml(sql, *values):
  conn = get_conn()

  with conn:
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
        conn.commit()
        return cursor.rowcount
