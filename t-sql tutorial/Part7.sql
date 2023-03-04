-- Part 7 - Identity Column in SQL Server

USE myDatabase
GO

SELECT * FROM dbo.tblPerson;

INSERT INTO dbo.tblPerson VALUES (12, 'Todd', 't@t.com', 1, 25);

INSERT INTO dbo.tblPerson1 VALUES ('Tom');

INSERT INTO dbo.tblPerson1 VALUES ('John');

INSERT INTO dbo.tblPerson1 VALUES ('Sara');

SELECT * FROM dbo.tblPerson1;

DELETE FROM dbo.tblPerson1 WHERE PersonID = 1;

INSERT INTO dbo.tblPerson1 VALUES ('Todd');

SELECT * FROM dbo.tblPerson1;

INSERT INTO dbo.tblPerson1 VALUES (1, 'Jane');

SET IDENTITY_INSERT tblPerson1 ON;

INSERT INTO dbo.tblPerson1 (PersonID, Name) VALUES (1, 'Jane');

SELECT * FROM dbo.tblPerson1;

INSERT INTO dbo.tblPerson1 VALUES ('Martin');

SET IDENTITY_INSERT tblPerson1 OFF;

INSERT INTO dbo.tblPerson1 VALUES ('Martin');

SELECT * FROM dbo.tblPerson1;

DELETE FROM tblPerson1;

SELECT * FROM dbo.tblPerson1;

INSERT INTO dbo.tblPerson1 VALUES ('Martin');

SELECT * FROM dbo.tblPerson1;

DELETE FROM tblPerson1;

DBCC CHECKIDENT('tblPerson1', RESEED, 0);

INSERT INTO dbo.tblPerson1 VALUES ('Martin');

SELECT * FROM dbo.tblPerson1;

