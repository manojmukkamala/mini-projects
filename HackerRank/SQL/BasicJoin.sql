# Asian Population
SELECT SUM(C.POPULATION)
FROM COUNTRY CO, CITY C 
WHERE CONTINENT = 'Asia' AND C.COUNTRYCODE = CO.CODE


# African Cities
SELECT CITY.NAME
FROM CITY, COUNTRY
WHERE COUNTRY.CONTINENT = 'Africa' AND CITY.CountryCode = COUNTRY.Code;


# Average Population of Each Continent
SELECT CONTINENT, CEILING(AVG(CITY.POPULATION))
FROM COUNTRY, CITY
WHERE CITY.COUNTRYCODE= COUNTRY.CODE
GROUP BY CONTINENT;


# The Report
SELECT CASE WHEN GRADE < 8 THEN NULL ELSE NAME END, GRADE, MARKS 
FROM STUDENTS S, GRADES G
WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK
ORDER BY GRADE DESC, NAME;


# Top Competitors
SELECT H.HACKER_ID, H.NAME
FROM HACKERS H, SUBMISSIONS S, CHALLENGES C, DIFFICULTY D
WHERE S.HACKER_ID = H.HACKER_ID AND S.CHALLENGE_ID = C.CHALLENGE_ID AND C.DIFFICULTY_LEVEL = D.DIFFICULTY_LEVEL AND S.SCORE = D.SCORE
GROUP BY H.HACKER_ID, H.NAME
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, H.HACKER_ID ASC


#Challenges
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS challenges_created
FROM Hackers h JOIN Challenges c ON c.hacker_id = h.hacker_id
GROUP BY h.hacker_id, h.name
HAVING COUNT(c.challenge_id) = 
    (SELECT TOP 1 COUNT(c2.challenge_id) AS c_max
     FROM challenges as c2 
     GROUP BY c2.hacker_id 
     ORDER BY c_max DESC)
OR COUNT(c.challenge_id) IN 
    (SELECT DISTINCT c_compare AS c_unique
     FROM (SELECT h2.hacker_id, 
                  h2.name, 
                  COUNT(challenge_id) AS c_compare
           FROM Hackers h2
           JOIN Challenges c ON c.hacker_id = h2.hacker_id
           GROUP BY h2.hacker_id, h2.name) counts
     GROUP BY c_compare
     HAVING COUNT(c_compare) = 1)
ORDER BY challenges_created DESC, h.hacker_id;


#Contest Leaderboard
SELECT H.Hacker_id, name, SUM(MaxScore) as Tot
FROM(
    SELECT Hacker_id, challenge_id, MAX(score) as MaxScore
    FROM SUBMISSIONS
    GROUP BY HACKER_id, challenge_id
    HAVING MAX(score) > 0
 ) S, HACKERS H
WHERE H.Hacker_id = S.Hacker_id
GROUP BY H.Hacker_id, name
ORDER BY Tot DESC, H.Hacker_id;
