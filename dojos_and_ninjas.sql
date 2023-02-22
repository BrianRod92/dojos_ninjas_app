INSERT INTO dojos (name) VALUES ("Rumble");
INSERT INTO dojos (name) VALUES ("Persistence");
INSERT INTO dojos (name) VALUES ("Resolution");

SELECT * FROM dojos;

DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;

SELECT * FROM dojos;

INSERT INTO dojos (name) VALUES ("Matrix");
INSERT INTO dojos (name) VALUES ("Spartan");
INSERT INTO dojos (name) VALUES ("Gulag");

SELECT * FROM dojos;

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Martin", "Garfield", 33, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Garry", "Martinfield", 24, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Kool", "Gang", 51, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Jim", "Timberland", 37, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Luigi", "Greensworth", 22, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Bill", "Billington", 48, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Benny", "Butch", 21, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Crimson", "Chinsworth", 34, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Sideshow", "Bubafet", 68, 6);

SELECT * FROM ninjas WHERE dojo_id = 4;

SELECT * FROM ninjas WHERE dojo_id = 6;

SELECT * FROM ninjas ORDER BY id DESC;

SELECT name as "Dojo Name" FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE ninjas.id = 9;

SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojos.id = 5;

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Lui", "Green", 26, 4);
