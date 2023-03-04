-- Part 3 - Creating and Working with Tables

USE [myDatabase]
GO

CREATE TABLE tblPerson
(
ID INT NOT NULL PRIMARY KEY,
Name NVARCHAR(50) NOT NULL,
Email NVARCHAR(50) NOT NULL,
GenderID INT 
);

CREATE TABLE tblGender
(
ID INT NOT NULL PRIMARY KEY,
Gender NVARCHAR(50) NOT NULL
);

ALTER TABLE tblPerson
ADD CONSTRAINT tblPerson_GenderID_FK
FOREIGN KEY (GenderID)
REFERENCES tblGender (ID);