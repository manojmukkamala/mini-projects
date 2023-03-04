-- Part 9 - UNIQUE Key constraint

USE myDatabase
GO

ALTER TABLE tblPerson
ADD CONSTRAINT UQ_tblPerson_Email UNIQUE (Email);

SELECT * FROM tblPerson

INSERT  INTO tblPerson 
VALUES (11, 'ABC', 'a@a.com', 1, 20);

SELECT * FROM tblPerson;

INSERT  INTO tblPerson 
VALUES (13, 'XYZ', 'a@a.com', 1, 20);

ALTER TABLE tblPerson
DROP CONSTRAINT UQ_tblperson_Email