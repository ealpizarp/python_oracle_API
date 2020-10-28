# Autor: Eric Alpizar Prendas
#        Rodrigo Espinach
# Fecha: 10/24/2020

import cx_Oracle

from flask_cors import CORS

# Se importa la biblioteca encargada de realizar la conexion con Oracle

from flask import Flask, jsonify, request

# Se importa Flask, una biblioteca que se encarga de facilitar la construccion del API

import json

#Inicializacion del servidor Flask

app = Flask(__name__)

CORS(app)

#Datos ingresados para la conexion a la base de datos cx_Oracle.connect(<username>, <password>, "localhost/XE")

connection = cx_Oracle.connect("ealpizarp", "root", "localhost/XE")

cursor = connection.cursor()

# Muestra todos los datos sobre una entidad en especifico

@app.route('/movies', methods=['GET'])
def movies():
    cursor.execute("""
    SELECT * FROM movie
    """)
    row = cursor.fetchall()
    dic_array = []
    for index, record in enumerate(row):
        dic_array.append({'description': record[1], 'id': record[0], 'name':record[2], 'urlPhoto': record[3]})

    return jsonify(dic_array)


# Se se utiliza para buscar una entidad con un id en especifico. Ejemplo: localhost:4000/movies/1

@app.route('/movies/<int:movie_id>')
def getMovie(movie_id):

    cursor.execute("""
    SELECT * FROM movie WHERE :id_ext = id_movie
    """, id_ext = movie_id)
    row = cursor.fetchall()
    dic_array = []

    for index, record in enumerate(row):
        dic_array.append({'description': record[1], 'id': record[0], 'name':record[2], 'urlPhoto': record[3]})

    return jsonify(dic_array)




## El siguiente procedimiento interactua con la base de datos para insertar una tabla


@app.route('/movies/insert', methods=['POST'])

def addMovie():
    	
    data = request.get_json(force=True)
    try:
        cursor.execute("""
        INSERT INTO movie VALUES (:id_ext, :descripcion_pel, :nom_pelicula, :url_image)
        """, id_ext = data['id'], descripcion_pel = data['description'],
            nom_pelicula = data['name'], url_image = data['urlPhoto'])

        connection.commit()

    except cx_Oracle.DatabaseError as e:

        print('Error-', e.Code)
        print('Mensaje-Error', e.Message)

    finally:

        return jsonify({'message': 'Procedimiento completado'})




# Actualizacion de datos especificados, para los datos que no se desea actualizar se debe utiliza NULL en el JSON file

@app.route('/movies/update/<int:movie_id>', methods=['PUT'])
def editMovie(movie_id):
    try:

        data = request.get_json(force=True)
        
        statement = """ UPDATE movie SET description_movie = COALESCE(:dec_mov, description_movie), name_movie = COALESCE(:n_mov, name_movie),
        url_photo_movie = COALESCE(:url_ph, url_photo_movie) WHERE id_movie = :id_ext """
        params = {'id_ext': movie_id , 'n_mov': data['name'], 'url_ph': data['urlPhoto'], 'dec_mov': data['description'] }

        cursor.execute(statement, params)

        connection.commit()

    except cx_Oracle.DatabaseError as e:

        print('Error-', e.Code)
        print('Mensaje-Error', e.Message)

    finally:

         return jsonify({'message': 'Procedimiento completado'})



# El siguiente codigo esta hecho para borrar alguna tabla de la base de datos, utilizar el metodo DELETE para esto
# no se puede hacer directamente del URL

@app.route('/movies/delete/<int:movie_id>', methods=['DELETE'])

def deleteMovie(movie_id):
    try:
        cursor.execute(
            "DELETE FROM movie WHERE id_movie = :id_ext ", id_ext = movie_id 
        )
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print('Error', error.code)
    finally:
        connection.commit()
        print('Datos eliminados correctamente')

        cursor.execute("""
        SELECT * FROM movie
        """)

        row = cursor.fetchall()
        dic_array = []

        for index, record in enumerate(row):
            dic_array.append({'description': record[1], 'id': record[0], 'name':record[2], 'urlPhoto:': record[3]})

        return jsonify(dic_array)



# Encender el servidor

if __name__ == '__main__':
    app.run(debug=True, port=4000)