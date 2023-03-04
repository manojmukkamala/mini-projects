# Revising Aggregations - The Count Function
SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000;


# Revising Aggregations - The Sum Function
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';


# Revising Aggregations - Averages
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';


# Average Population
SELECT AVG(POPULATION)
FROM CITY;


# Japan Population
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN';


# Population Density Difference
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;


# The Blunder
SELECT CAST(CEILING(AVG(CAST(SALARY as FLOAT))-AVG(CAST(REPLACE(STR(SALARY), '0', '') AS FLOAT))) AS INT) 
FROM EMPLOYEES;


# Top Earners
SELECT TOP 1 (MONTHS*SALARY) AS EARNINGS, COUNT(*)
FROM EMPLOYEE
GROUP BY MONTHS*SALARY
ORDER BY COUNT(*) DESC;
                                                   
                                                   
# Weather Observation Station 2                                                   
SELECT CONCAT(LEFT(ROUND(SUM(LAT_N), 2), 8),' ', LEFT(ROUND(SUM(LONG_W), 2), 8))
FROM STATION;

                                                      
# Weather Observation Station 13
SELECT CAST(SUM(LAT_N) AS NUMERIC(10, 4))
FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;

                                  
# Weather Observation Station 14                                                 
SELECT CAST(MAX(LAT_N) AS NUMERIC(10, 4))
FROM STATION
WHERE LAT_N < 137.2345;
                                  

# Weather Observation Station 15
SELECT CAST(LONG_W AS NUMERIC(10, 4))
FROM STATION
WHERE LAT_N IN
(SELECT MAX(LAT_N) 
FROM STATION
WHERE LAT_N < 137.2345);
                              

# Weather Observation Station 16                                                   
SELECT CAST(MIN(LAT_N) AS NUMERIC(10, 4))
FROM STATION
WHERE LAT_N > 38.7780;
                                  

# Weather Observation Station 17
SELECT CAST(LONG_W AS NUMERIC(10, 4))
FROM STATION
WHERE LAT_N IN
(SELECT MIN(LAT_N)
FROM STATION
WHERE LAT_N > 38.7780);
                              

# Weather Observation Station 18                                                  
SELECT CAST(ABS(MIN(LAT_N)-MAX(LAT_N)) + ABS(MIN(LONG_W) - MAX(LONG_W)) AS NUMERIC(10, 4))
FROM STATION;
                                                                                   

# Weather Observation Station 19 
SELECT CAST(SQRT(SQUARE(MIN(LAT_N) - MAX(LAT_N)) + SQUARE(MIN(LONG_W) - MAX(LONG_W))) AS NUMERIC(10, 4))
FROM STATION;
                                                                                                 

# Weather Observation Station 20                                                  
SELECT CAST(S.LAT_N AS NUMERIC(10, 4)) MEDIAN 
FROM STATION S 
WHERE (SELECT COUNT(Lat_N) FROM STATION WHERE Lat_N < S.LAT_N) = (SELECT COUNT(Lat_N) FROM STATION WHERE Lat_N > S.LAT_N);

