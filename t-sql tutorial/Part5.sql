-- Part 5 - Cascading Referential Integrity Constraint

USE myDatabase 
GO

SELECT * FROM tblGender;
SELECT * FROM tblPerson;

DELETE FROM tblGender WHERE ID = 2;