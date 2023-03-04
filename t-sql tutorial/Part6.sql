-- Part 6 - Adding a Check Constraint

USE myDatabase
GO

ALTER TABLE tblPerson
ADD Age INT NULL;

SELECT * FROM tblPerson;

INSERT INTO tblPerson  VALUES (11, 'Sara', 's@s.com', 2, -970);

DELETE FROM tblPerson WHERE ID = 11

ALTER TABLE tblPerson
ADD CONSTRAINT CK_tblPerson_Age
CHECK (Age > 0 AND Age < 150);

INSERT INTO tblPerson  VALUES (11, 'Sara', 's@s.com', 2, -970);

INSERT INTO tblPerson  VALUES (11, 'Sara', 's@s.com', 2, 10);

SELECT * FROM tblPerson;