DROP TABLE indirect_flights;


CREATE TABLE indirect_flights(
    airport_name VARCHAR(60) NOT NULL,
    latitude_deg VARCHAR(30) NOT NULL,
    longitude_deg VARCHAR(30) NOT NULL,
    iso_region VARCHAR(30) NOT NULL,
    municipality VARCHAR(30) NOT NULL,
    iata_code VARCHAR(30) NOT NULL,
    Temperature_in_F VARCHAR(30) NOT NULL
    
);



SELECT * FROM indirect_flights;

-------------------------------------

DROP TABLE direct_flights;


CREATE TABLE direct_flights(
    Title VARCHAR(60) NOT NULL,
    Code VARCHAR(30) NOT NULL,
    Temperature_in_F VARCHAR(30) NOT NULL
    
);

SELECT * FROM direct_flights;

----------------------------------

DROP TABLE restaurant;


CREATE TABLE restaurant(
    Index_ VARCHAR(60) NOT NULL,
    Restaurant_Name VARCHAR(60) NOT NULL,
    Price_Level VARCHAR(30) NOT NULL,
    Rating VARCHAR(30) NOT NULL,
    Address VARCHAR(300) NOT NULL,
    City_Code VARCHAR(30) NOT NULL
    
);



SELECT * FROM restaurant;


----------------------------------
