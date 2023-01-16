USE homework_10;
DROP TABLE IF EXISTS pc;
CREATE TABLE PC (
code int auto_increment not null primary key,
 model varchar(40),
 speed smallint,
 ram smallint,
 hd real,
 cd varchar(10),
 price float
 );
INSERT INTO pc (model, speed, ram, hd, cd, price)
VALUES
("HP", 1000, 4, 250, 1, 10000),
("lenovo", 1500, 8, 500, 2, 11000),
("Intel", 2000, 16, 1000, 3, 12000),
("Apple", 3000, 16, 1500, 1, 13000),
("Athlon", 4000, 8, 1600, 1, 15000);

SELECT * FROM pc WHERE price < 400;

SELECT model, speed FROM pc WHERE ( ram >= 8 AND ram <=16);

SELECT price FROM pc WHERE hd<1000;

UPDATE  pc
    SET price=price*2
    WHERE price>400;
