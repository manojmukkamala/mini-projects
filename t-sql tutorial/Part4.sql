-- Part 4 - Adding a Default Constraint

USE myDatabase 
GO

SELECT * FROM tblGender;
SELECT * FROM tblPerson;

-- Adding a New Record
INSERT INTO tblPerson (ID, Name, Email)
VALUES
(7, 'Rich', 'r@r.com');

-- Adding DEFAULT Constraint to tblPerson (GenderID)
ALTER TABLE tblPerson
ADD CONSTRAINT DF_tblPerson_GenderID
DEFAULT 3 FOR GenderID;

-- Adding a New Record
INSERT INTO tblPerson (ID, Name, Email)
VALUES
(8, 'Mike', 'mike@r.com');

SELECT * FROM tblPerson;


-- Adding a New Record
INSERT INTO tblPerson (ID, Name, Email, GenderID)
VALUES
(9, 'Sara', 's@r.com', 1);

SELECT * FROM tblPerson;


-- Adding a New Record
INSERT INTO tblPerson (ID, Name, Email, GenderID)
VALUES
(10, 'Johny', 'j@r.com', NULL);

SELECT * FROM tblPerson;