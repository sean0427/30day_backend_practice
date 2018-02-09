BEGIN;
    CREATE TABLE Language(
        id SERIAL PRIMARY KEY,
        code CHAR(6) NOT NULL UNIQUE,
        name VARCHAR
    );

    CREATE TABLE Locale(
        id SERIAL PRIMARY KEY,
        name VARCHAR UNIQUE
    );

    CREATE TABLE Company(
        id SERIAL PRIMARY KEY,
        name VARCHAR NOT NULL UNIQUE,
        address VARCHAR,
        telephone CHAR(10),
        contant_person_name CHAR(30)
    );

    CREATE TABLE User_Classification(
        id SERIAL PRIMARY KEY,
        name CHAR(10) UNIQUE
    );

    CREATE TABLE Product_Type(
        id SERIAL PRIMARY KEY,
        name CHAR(30) UNIQUE
    );

    CREATE TABLE Number(
        id SERIAL PRIMARY KEY,
        password TEXT NOT NULL,
        user_classification_id INTEGER REFERENCES User_Classification NOT NULL,
        e_mail CHAR(100) NOT NULL UNIQUE
    );

    CREATE TABLE User_Shopping_Inforation(
        id SERIAL PRIMARY KEY,
        number_id INTEGER REFERENCES Number NOT NULL,
        address VARCHAR NOT NULL,
        telephone CHAR(10)
    );

    CREATE TABLE Coupon_Type(
        id SERIAL PRIMARY KEY,
        type INTEGER REFERENCES Product_Type NOT NULL,
        discount INTEGER NOT NULL,
        duration_days INTEGER NOT NULL
    );

    CREATE TABLE Coupon(
        id SERIAL PRIMARY KEY,
        type_id INTEGER REFERENCES Coupon_Type NOT NULL,
        start_datetime TIMESTAMP NOT NULL,
        owner_id INTEGER REFERENCES Number DEFAULT 0
    );

    CREATE TABLE Product(
        id SERIAL PRIMARY KEY,
        type_id INTEGER REFERENCES Product_Type NOT NULL,
        manufacturing INTEGER REFERENCES Company
    );

    CREATE TABLE Language_Product(
        id SERIAL PRIMARY KEY,
        product_id INTEGER REFERENCES Product NOT NULL,
        language_id INTEGER REFERENCES Language NOT NULL,
        name CHAR(100) NOT NULL,
        describe TEXT,
        image CHAR(100)
    );

    CREATE TABLE Locale_Product(
        id SERIAL PRIMARY KEY,
        product_id INTEGER REFERENCES Product NOT NULL,
        locale_id INTEGER REFERENCES Locale NOT NULL,
        price MONEY NOT NULL,
        publisher INTEGER REFERENCES Company NOT NULL
    );

    CREATE TABLE Discounted_Locate_Product(
        id SERIAL PRIMARY KEY,
        locale_product_id INTEGER REFERENCES Language_Product NOT NULL,
        user_classification_id INTEGER REFERENCES User_Classification,
        discount INTEGER NOT NULL,
        start_datetime TIMESTAMP NOT NULL,
        end_datetime TIMESTAMP NOT NULL
    );

    CREATE TABLE Bill(
        id SERIAL PRIMARY KEY,
        user_shopping_inforation_id INTEGER REFERENCES User_Classification NOT NULL,
        date TIMESTAMP NOT NULL,
        status INTEGER NOT NULL default 0,
        total MONEY NOT NULL
    );

    CREATE TABLE Order_Discounted_Locale_Product(
        id SERIAL PRIMARY KEY,
        product_id INTEGER REFERENCES Discounted_Locate_Product NOT NULL,
        bill_id INTEGER REFERENCES Bill NOT NULL,
        coupon_id INTEGER REFERENCES Coupon,
        quantity INTEGER NOT NULL
    );
END;
