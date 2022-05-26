
CREATE TABLE ALBUM
( 
	album_id             integer  NOT NULL ,
	artista_id           integer  NOT NULL ,
	nombre_al            varchar(50)  NOT NULL ,
	no_canciones         integer  NOT NULL ,
	genero               varchar(20)  NULL ,
	año_al               integer  NOT NULL ,
	duracion_al          integer  NOT NULL 
);

ALTER TABLE ALBUM
DROP COLUMN DURACION_AL;

ALTER TABLE ALBUM
ADD DURACION_AL VARCHAR(5) NOT NULL;

ALTER TABLE ALBUM
	ADD CONSTRAINT XPKAlbum PRIMARY KEY (album_id);
    
CREATE TABLE ARTISTA
( 
	artista_id           integer  NOT NULL ,
	disquera_id          integer  NOT NULL ,
	nombre               varchar(50)  NOT NULL ,
	no_albumes           integer  NULL ,
	descripcion_a        varchar(100)  NULL ,
	no_reprod_a          integer  NULL ,
	seguidores_a         integer  NULL ,
	verificado           varchar(20)  NOT NULL 
);

ALTER TABLE ARTISTA
	ADD CONSTRAINT XPKArtista PRIMARY KEY (artista_id);

CREATE TABLE CANCION
( 
	cancion_id           integer  NOT NULL ,
	album_id             integer  NOT NULL ,
	titulo               varchar(50)  NOT NULL ,
	duracion_c           varchar(5)  NOT NULL ,
	genero               varchar(20)  NULL ,
	no_reprod_c          integer  NULL ,
	año_c                integer  NOT NULL 
);

ALTER TABLE CANCION
DROP COLUMN DURACION_C;

ALTER TABLE CANCION
ADD DURACION_C VARCHAR(5);

ALTER TABLE CANCION
	ADD CONSTRAINT XPKCanciones PRIMARY KEY (cancion_id);

CREATE TABLE DISQUERA
( 
	disquera_id          integer  NOT NULL ,
	nombre_disq          varchar(50)  NOT NULL ,
	ceo                  varchar(50)  NULL 
);

ALTER TABLE DISQUERA
	ADD CONSTRAINT XPKDisquera PRIMARY KEY (disquera_id);

CREATE TABLE PLAYLIST
( 
	playlist_id          integer  NOT NULL ,
	usuario_id           integer  NOT NULL ,
	nombre_p             varchar(20)  NOT NULL ,
	descripcion_p        varchar(50)  NULL ,
	no_canciones         integer  NOT NULL ,
	seguidores_p         integer  NULL ,
	duracion_p           integer  NOT NULL 
)

ALTER TABLE PLAYLIST
DROP COLUMN CANCION_ID;

ALTER TABLE PLAYLIST
	ADD CONSTRAINT XPKPlaylist PRIMARY KEY (playlist_id);

CREATE TABLE USUARIO
( 
	usuario_id           integer  NOT NULL ,
	artista_id           integer  NOT NULL ,
	nombre_u             varchar(20)  NOT NULL ,
	no_seguidores_u      integer  NULL ,
	no_siguiendo         integer  NOT NULL 
);

ALTER TABLE USUARIO
	ADD CONSTRAINT XPKUsuario PRIMARY KEY (usuario_id);
    
ALTER TABLE ALBUM
	ADD CONSTRAINT R_2 FOREIGN KEY (artista_id) REFERENCES Artista(artista_id);

ALTER TABLE ARTISTA
	ADD CONSTRAINT R_3 FOREIGN KEY (disquera_id) REFERENCES Disquera(disquera_id);

ALTER TABLE CANCION
	ADD CONSTRAINT R_1 FOREIGN KEY (album_id) REFERENCES Album(album_id);

ALTER TABLE PLAYLIST
	ADD CONSTRAINT R_6 FOREIGN KEY (cancion_id) REFERENCES Cancion(cancion_id);

ALTER TABLE PLAYLIST
	ADD CONSTRAINT R_7 FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id);

ALTER TABLE USUARIO
	ADD CONSTRAINT R_5 FOREIGN KEY (artista_id) REFERENCES Artista(artista_id);
    
INSERT INTO DISQUERA
VALUES(1, 'Universal Music Group', 'Lucian Grainge');
INSERT INTO DISQUERA
VALUES(2, 'Sony Music Entertainment', 'Rob Stringer');
INSERT INTO DISQUERA
VALUES(3, 'Warner Music Group', 'Stephen Cooper');
INSERT INTO DISQUERA
VALUES(4, 'Island Records', 'Darcus Beese, OBE and MD Jon Turner');
INSERT INTO DISQUERA
VALUES(5, 'BMG Rights', 'Hartwig Masuch)');
INSERT INTO DISQUERA
VALUES(6, 'ABC-Paramount', 'Edward J. Noble');
INSERT INTO DISQUERA 
VALUES(7, 'Virgin Records', 'Richard Branson');
INSERT INTO DISQUERA
VALUES(8, 'Red Hill Records', 'Bobby Holliday');
INSERT INTO DISQUERA
VALUES(9, 'JYP Entertainment', 'Jung Wook');
INSERT INTO DISQUERA
VALUES(10, 'SM Entertainment', 'Lee Sung Soo');

INSERT INTO ARTISTA
VALUES (1, 10, 'ITZY', 5, 'Itzy is a South Korean girl group consisting of members Yeji, Lia, Ryujin, Chaeryeong, and Yuna.', 1000000, 100000, 'True');
INSERT INTO ARTISTA
VALUES (2, 9, 'NCT 127', 15, 'NCT 127 is the first fixed sub-unit of the South Korean boy band NCT', 1132324, 123123, 'True');
INSERT INTO ARTISTA
VALUES(3, 2, 'Little Mix', 6, 'British girl group consisting of Jade Thirlwall, Perrie Edwards, and Leigh-Anne Pinnock', 654321, 78987, 'True');
INSERT INTO ARTISTA
VALUES(4, 1, 'BTS', 12, 'BTS, also known as the Bangtan Boys, is a South Korean boy band that debuted in 2013', 7896546, 98745, 'True');
INSERT INTO ARTISTA
VALUES(5, 3, 'Coldplay', 9, 'Edward Christopher Sheeran MBE is an English singer-songwriter', 982647, 1234, 'True');
INSERT INTO ARTISTA
VALUES(6, 5, 'Louis Tomlinson', 2, 'Louis William Tomlinson is an English singer and songwriter', 609713, 13492, 'True');
INSERT INTO ARTISTA
VALUES(7, 4, 'Keshi', 3, ' Keshi is an American singer, songwriter, record producer, and multi-instrumentalist.', 794568, 7689, 'True');
INSERT INTO ARTISTA
VALUES(8, 6, 'B.B King', 8, ' B.B. King was an American blues singer-songwriter, guitarist, and record producer', 182948, 827433, 'True');
INSERT INTO ARTISTA
VALUES(9, 7, 'Daft Punk', 6, 'Daft Punk were a French electronic music duo formed by Thomas Bangalter & Guy-Manuel de Homem-Christo', 728374, 82983, 'True');
INSERT INTO ARTISTA
VALUES(10, 8, 'Katy Perry', 3, 'Katy Perry, is an American singer, songwriter, actress and television personality', 7826354, 981632, 'True'); 

INSERT INTO ALBUM
VALUES(1, 1, 'Crazy in Love', 16, 'K-Pop', 2021, '51:09');
INSERT INTO ALBUM
VALUES(2, 2, 'We Are Superhuman', 6, 'K-Pop', 2019, '18:26');
INSERT INTO ALBUM
VALUES(3, 3, 'Salute', 12, 'Pop', 2013, '43:06');
INSERT INTO ALBUM
VALUES(4, 4, 'Map Of The Soul: 7', 20, 'K-Pop', 2020, '74:52');
INSERT INTO ALBUM
VALUES (5, 5, 'A Rush of Blood to the Head', 11, 'Pop', 2002, '54:08');
INSERT INTO ALBUM
VALUES(6, 6, 'Walls', 12, 'Pop', 2020, '39:33');
INSERT INTO ALBUM
VALUES(7, 7, 'Gabriel', 12, 'R&B', 2022, '32:39');
INSERT INTO ALBUM
VALUES(8, 8, 'The Blues', 12, 'Blues', 1957, '33:38');
INSERT INTO ALBUM
VALUES(9, 9, 'Discovery', 14, 'French house' , 2001, '60:50');
INSERT INTO ALBUM
VALUES(10, 10, 'Teenage Dream', 12, 'Pop', 2010, '46:44');

INSERT INTO CANCION
VALUES(1, 1, 'LOCO', 'K-Pop', 3567892, 2020, '3:32');
INSERT INTO CANCION
VALUES(2, 2, 'Superhuman', 'K-Pop', 4019284, 2019, '3:59');
INSERT INTO CANCION
VALUES(3, 3, 'Salute', 'Pop', 1627384, 2013, '3:21');
INSERT INTO CANCION
VALUES(4, 4, 'Moon', 'K-Pop', 5901821, 2020, '3:12');
INSERT INTO CANCION
VALUES(5, 5, 'Clocks', 'Pop', 105679182, 2002, '3:49');
INSERT INTO CANCION
VALUES(6, 6, 'Two Of Us', 'Pop', 6781918, 2020, '3:38');
INSERT INTO CANCION
VALUES(7, 7, 'UNDERSTAND', 'R&B', 3876908, 2022, '3:10');
INSERT INTO CANCION
VALUES(8, 8, 'Why Do Things Happen to Me', 'Blues', 129897, 1958, '3:50');
INSERT INTO CANCION
VALUES(9, 9, 'One More Time', 'French house', 6778291, 2001, '3:19');
INSERT INTO CANCION
VALUES(10, 10, 'Teenage Dream', 'Pop', 1289387, 2010, '3:51');

INSERT INTO USUARIO
VALUES(1, 2, 'La Tocino', 13, 190);

INSERT INTO PLAYLIST
VALUES(1, 1, 'Música para barrer', 'Música para motivarse', 19, 20, '35:40');
INSERT INTO PLAYLIST
VALUES(2, 1, 'Chill Lo-Fi Music', 'Music for studying/relaxing', 50, 10020, '59:09');
INSERT INTO PLAYLIST
VALUES(3, 1, 'Anime Openings', 'Best openings', 32, 18290, '34:21');
INSERT INTO PLAYLIST
VALUES(4, 1, 'Concentration Music', 'For late study nights', 49, 78, '58:12');
INSERT INTO PLAYLIST
VALUES(5, 1, 'Classic Rock', 'Best classic rock songs', 19293, 78, '34:23');
