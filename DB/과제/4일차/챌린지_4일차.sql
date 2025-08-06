-- use report;

-- DROP TABLE IF EXISTS customer;
-- DROP TABLE IF EXISTS customer_pet;
-- DROP TABLE IF EXISTS room;
-- DROP TABLE IF EXISTS reservation;
-- DROP TABLE IF EXISTS service; 

-- CREATE TABLE customer (
-- 	customer_id INT AUTO_INCREMENT,
-- 	name varchar(50) NOT NULL,
-- 	phone_number varchar(50) NOT NULL,
-- 	address varchar(100) NOT NULL,
-- PRIMARY KEY (customer_id)
-- )

-- CREATE TABLE pet (
-- 	pet_id INT AUTO_INCREMENT,
--  customer_id INT NOT NULL,
--  pet_name varchar(50) NOT NULL,
--  species varchar(50) NOT NULL,
--  breed varchar(50) NOT NULL,
-- PRIMARY KEY (pet_id),
-- FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
-- )

-- CREATE TABLE room (
-- 	room_id INT AUTO_INCREMENT,
--  room_num varchar(50) NOT NULL,
--  room_type varchar(50) NOT NULL,
--  price DECIMAL(10,2) NOT NULL,
-- PRIMARY KEY (room_id)
-- )

-- CREATE TABLE reservation (
--     reservation_id INT AUTO_INCREMENT,
--     pet_id INT NOT NULL,
--     room_id INT NOT NULL,
--     start_date DATE NOT NULL,
--     end_date DATE NOT NULL,
-- PRIMARY KEY (reservation_id),
-- FOREIGN KEY (pet_id) REFERENCES pet(pet_id),
-- FOREIGN KEY (room_id) REFERENCES room(room_id)
-- )

CREATE TABLE service (
    service_id INT AUTO_INCREMENT,
    reservation_id INT NOT NULL,
    service_name VARCHAR(50),
    service_price DECIMAL(10,2),
PRIMARY KEY (service_id),
FOREIGN KEY (reservation_id) REFERENCES reservation(reservation_id)
)
