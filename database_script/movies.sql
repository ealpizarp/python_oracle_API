CREATE TABLE movie (id_movie NUMBER, description_movie VARCHAR2 (255), name_movie VARCHAR2 (50), 
url_photo_movie VARCHAR (255),
CONSTRAINT PK_MOVIE PRIMARY KEY (id_movie)
);

INSERT INTO movie VALUES (1, 'Caballero de la noche', 'Batman', 
'https://www.cinemascomics.com/wp-content/uploads/2020/07/batman-vs-deadshot-perro-dc-comics.jpg.webp');

INSERT INTO movie VALUES(2, 'Hombre de Acero', 'Superman',
'https://upload.wikimedia.org/wikipedia/en/3/35/Supermanflying.png');

INSERT INTO movie VALUES(3, 'Spidy', 'Spiderman',
'https://dam.smashmexico.com.mx/wp-content/uploads/2018/09/07142333/spidermanbio_portada.jpg');

INSERT INTO movie VALUES(4, 'Doctor Strange: hechicero supremo', 'Doctor Strange',
'https://i.annihil.us/u/prod/marvel/i/mg/c/40/5d9620fe44acb/clean.jpg');