BEGIN;
    INSERT INTO Locale(name) VALUES ('Taiwan');
    INSERT INTO Locale(name) VALUES ('US');

    INSERT INTO Language(code, name) VALUES ('en', 'English');
    INSERT INTO Language(code, name) VALUES ('zh-TW', '繁體中文（台灣）');

    INSERT INTO User_Classification(name) VALUES ('Normal');
    INSERT INTO User_Classification(name) VALUES ('Gold');
    INSERT INTO User_Classification(name) VALUES ('Silver');

    INSERT INTO Product_Type(name) VALUES ('3c');
    INSERT INTO Product_Type(name) VALUES ('colse');

    INSERT INTO Coupon_Type(type, discount, duration_days) 
        VALUES ((SELECT id FROM Product_Type WHERE name='3c'), 0.20, 30) ;
    INSERT INTO Coupon_Type(type, discount, duration_days) 
        VALUES ((SELECT id FROM Product_Type WHERE name='3c'), 0.50, 20) ;
    INSERT INTO Coupon_Type(type, discount, duration_days) 
        VALUES ((SELECT id FROM Product_Type WHERE name='3c'), 0.80, 10) ;
END;
