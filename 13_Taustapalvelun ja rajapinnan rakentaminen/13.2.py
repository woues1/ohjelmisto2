from flask import Flask, request
import mysql.connector


def get_db_connection() -> mysql.connector.connect:
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'flight_game',
        'autocommit': True
    }

    # Establish a connection
    return mysql.connector.connect(**db_config)


def sql_Execute_Query(sql):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result


app = Flask(__name__)

@app.route("/kenttä/<icao>")
def kenttä(icao):
    res = sql_Execute_Query(f"SELECT ident, name, municipality FROM airport where ident='{icao}'")
    icao, name, municipality = res[0]

    vastaus = {
        "ICAO": icao,
        "Name": name,
        "Municipality": municipality
    }
    return vastaus

if __name__=="__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)