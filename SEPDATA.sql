CREATE DATABASE sep;

USE sep;

CREATE TABLE login_user_data(
L_S_No INT AUTO_INCREMENT PRIMARY KEY,
L_Name VARCHAR(20),
L_Phone_Number VARCHAR(20),
L_E_Mail VARCHAR(30),
L_Pass VARCHAR(20),
L_Con_Pass VARCHAR(20)
);

DROP TABLE login_user_data;
SELECT * FROM login_user_data;

SET SQL_SAFE_UPDATES=0;
update login_user_data
set Address="Addres"
where L_Name="Vaishali";

update login_user_data
set Address="16/46 West Gangaghat Shuklaganj Unnao"
where L_Name="Prateek Yadav";

INSERT INTO login_user_data
VALUES 
(1,"Prateek","9956049122","prateekya23@gamil.com","Prateek12@","Prateek12@");
DELETE FROM login_user_data
WHERE L_S_No=3;

ALTER TABLE login_user_data
ADD COLUMN Address varchar(50);

CREATE TABLE book_table_data(
Name VARCHAR(20),
E_Mail VARCHAR(30),
Date_Time VARCHAR(20),
People INT,
Request VARCHAR(100)
);
DROP TABLE book_table_data;
SELECT * FROM book_table_data;


CREATE TABLE be_our_guest(
L_S_No INT AUTO_INCREMENT PRIMARY KEY,
G_Name VARCHAR(20),
G_EMail VARCHAR(30),
G_Date VARCHAR(20),
G_People INT,
G_Type varchar(20),
G_Special VARCHAR(100)
);
SELECT * FROM be_our_guest;
INSERT INTO be_our_guest
VALUES 
(1,"Prateek","prateekya23@gmail.com","20-Jan-24",2,"Breakfast","Nothing");


CREATE TABLE membership_table(
 M_S_No INT AUTO_INCREMENT PRIMARY KEY,
 M_Name varchar(20),
 M_E_Mail varchar(20), 
 M_Start_Date varchar(20), 
 M_No_Months varchar(20),
 M_Address varchar(50),
 M_CIty varchar(20), 
 M_State varchar(20), 
 M_Pin_Code int, 
 M_Menu_Type varchar(20), 
 M_Phone int
 );
 
ALTER TABLE membership_table
MODIFY M_Phone VARCHAR(10);

ALTER TABLE membership_table
MODIFY M_E_Mail VARCHAR(30);
 
INSERT INTO membership_table
VALUES 
(2,"Prateek","prateekya23@gmail.com","20-Jan-24","Six","Shuklaganj","unnao","Uttar Pradesh",209861,"Nothing","9956049122");

select * from membership_table;