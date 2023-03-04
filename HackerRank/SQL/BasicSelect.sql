# Revising the Select Query I
SELECT ID, NAME, COUNTRYCODE, DISTRICT, POPULATION 
FROM CITY
WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';


# Revising the Select Query II
SELECT NAME
FROM CITY
WHERE POPULATION > 120000 AND COUNTRYCODE = 'USA';


# Select All
SELECT * FROM CITY;


# Select By ID
SELECT *
FROM CITY 
WHERE ID = 1661;


# Japanese Cities' Attributes
SELECT * 
FROM CITY
WHERE COUNTRYCODE = 'JPN';


# Japanese Cities' Names
SELECT NAME
FROM CITY 
WHERE COUNTRYCODE = 'JPN';


# Weather Observation Station 1
SELECT CITY, STATE FROM STATION;


# Weather Observation Station 3
SELECT DISTINCT CITY FROM STATION WHERE (ID % 2) = 0;


# Weather Observation Station 4
SELECT (COUNT(CITY) - COUNT(DISTINCT(CITY))) FROM STATION;


# Weather Observation Station 5
SELECT TOP 1 CITY, LEN(CITY) 
FROM STATION
ORDER BY LEN(CITY) ASC, CITY ASC;
SELECT TOP 1 CITY, LEN(CITY) 
FROM STATION
ORDER BY LEN(CITY) DESC, CITY DESC;


# Weather Observation Station 6
select CITY from STATION where CITY like '[aeiou]%';


# Weather Observation Station 7
SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE '%[aeiou]';


# Weather Observation Station 8
SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE '%[aeiou]' AND CITY LIKE '[aeiou]%';


# Weather Observation Station 9
select DISTINCT CITY from STATION where CITY  NOT like '[aeiou]%';


# Weather Observation Station 10
select distinct CITY from STATION where CITY not like '%[aeiou]';


# Weather Observation Station 11
select distinct CITY from STATION where CITY not like '[aeiou]%' or CITY not like '%[aeiou]';


# Weather Observation Station 12
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT LIKE '%[aeiou]' AND CITY NOT LIKE '[aeiou]%' 


# Higher Than 75 Marks
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(Name,3), ID; 


# Employee Names
SELECT name FROM EMPLOYEE ORDER BY name;


# Employee Salaries
SELECT name FROM EMPLOYEE WHERE salary > 2000 AND months < 10;
