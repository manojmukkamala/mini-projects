/* 3b – Week 3: Writing your own SQL queries */


/* Write an SQL query to find the radius and temperature of the stars in the Star table that are larger than our sun. */
SELECT radius, t_eff
FROM Star
WHERE radius > 1;


/* Write a range query which returns the kepler_id and the t_eff attributes of all those stars in the Star table whose temperature lies between 5000 and 6000 Kelvin (inclusive). */
SELECT kepler_id, t_eff
FROM Star 
WHERE t_eff BETWEEN 5000 AND 6000;


/* Write a query to find the kepler_name and radius of each planet in the Planet table which is a confirmed exoplanet, meaning that their kepler_name is not NULL, or, equivalently, whose status is 'CONFIRMED'.
 Restrict your results to those planets whose radius lies between one and three earth radii, and remember that the radius of the planets is relative to the earth radius. */
SELECT kepler_name, radius
FROM Planet
WHERE (kepler_name IS NOT NULL OR status = 'CONFIRMED') AND radius BETWEEN 1 AND 3;


/* Write a query that calculates the:
-minimum radius;
-maximum radius;
-average radius; and
-standard deviation of the radii
of unconfirmed planets (with a NULL value in kepler_name) in the Planet table. */
SELECT MIN(radius), MAX(radius), AVG(radius), STDDEV(radius)
FROM Planet
WHERE kepler_name IS NULL;


/* How many planets in the Planet database are in a multi-planet system. Planets sharing the same star will have the same kepler_id, but different koi_name values.
Your query should return a table in which each row contains the kepler_id of the star and the number of planets orbiting that star (i.e. that share this kepler_id).
Limit your results to counts above one and order the rows in descending order based on the number of planets. */
SELECT kepler_id, COUNT(*)
FROM Planet
GROUP BY 1 
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;


/* 4a – Week 3: Joining tables with SQL */

/* Write a query that returns the radius of each star and planet pair whose radii have a ratio greater than the Sun-to-Earth radius ratio. Order the results in descending order based on the stellar radii. Use sun_radius and planet_radius as attribute aliases for the star and planet radii.
For this problem you will have to join the two tables to find all planets belonging to a given star and use a condition to select those results which fulfill the size requirement above. */
SELECT s.radius AS sun_radius, p.radius AS planet_radius
FROM Star s INNER JOIN Planet p ON s.kepler_id = p.kepler_id
WHERE (s.radius/p.radius) > 1
ORDER BY sun_radius DESC;


/* Write a query which counts the number of planets in each solar system where the corresponding stars are larger than our sun (i.e. their radius is larger than 1).
Your query should return the star's radius and its number of planets, showing only rows where the number of planets is more than one. Sort the rows in descending order based on the star radii. */
SELECT s.radius, COUNT(*)
FROM Star s INNER JOIN Planet p ON s.kepler_id = p.kepler_id
WHERE s.radius > 1
GROUP BY s.kepler_id
HAVING COUNT(*) > 1
ORDER BY s.radius DESC;


/* Write a query which returns the kepler_id, t_eff and radius for all stars in the Star table which haven't got a planet as join partner. Order the resulting table based on the t_eff attribute in descending order. */
SELECT s.kepler_id, s.t_eff, s.radius
FROM Star s LEFT OUTER JOIN Planet p ON s.kepler_id = p.kepler_id
WHERE p.koi_name IS NULL
ORDER BY t_eff DESC;


/* Write a query which queries both the Star and the Planet table and calculates the following quantities:
-the average value of the planets' equilibrium temperature t_eq, rounded to one decimal place;
-the minimum effective temperature t_eff of the stars;
-the maximum value of t_eff;
Your query should only use those star-planet pairs whose stars have a higher temperature (t_eff) than the average star temperature in the table. Try to use a subquery to solve this problem! */
SELECT ROUND(AVG(p.t_eq), 1), MIN(s.t_eff), MAX(s.t_eff)
FROM Star s JOIN Planet p USING(kepler_id)
WHERE s.t_eff > (SELECT AVG(t_eff) AS t_eff FROM Star);


/* Write a query which finds the radii of those planets in the Planet table which orbit the five largest stars in the Star table. Your query should return the planet's koi_name and radius as well as the corresponding star radius. */
SELECT koi_name, p.radius, s.radius
FROM Planet p JOIN Star s USING (kepler_id)
WHERE s.radius IN (SELECT radius FROM Star ORDER BY radius DESC LIMIT 5);

