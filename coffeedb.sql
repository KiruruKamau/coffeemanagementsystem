
CREATE DATABASE coffeefactory;
USE coffeefactorydb;

CREATE TABLE cooperative_society (
    id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE factory (
    id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100),
    cooperative_society_id VARCHAR(100),
    FOREIGN KEY (cooperative_society_id) REFERENCES cooperative_society(id)
);

CREATE TABLE farmer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    sex VARCHAR(15) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    contact_number VARCHAR(15),
    factory_id VARCHAR(100) NOT NULL,
    FOREIGN KEY (factory_id) REFERENCES factory(id)
);

CREATE TABLE farmer_bank (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bank_name VARCHAR(30) NOT NULL,
    account_number VARCHAR(100),
    amount_to_be_paid INT NOT NULL,
    farmer_id INT NOT NULL,
    FOREIGN KEY (farmer_id) REFERENCES farmer(id)
);

CREATE TABLE coffee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    grade VARCHAR(15) NOT NULL,
    amount INT NOT NULL,
    price_bought INT NOT NULL
);

CREATE TABLE farmer_inputs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    farmer_id INT NOT NULL,
    input_description VARCHAR(100) NOT NULL,
    amount_charged INT NOT NULL
);

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    salary INT NOT NULL
);
