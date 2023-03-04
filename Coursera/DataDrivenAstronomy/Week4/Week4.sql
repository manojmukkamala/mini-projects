/* 4b – Week 4: Setting up your own database */

/* Modifying tables 1 */

/* Modifying data in existing tables 

The previous activity covered a broad range of standard SQL syntax for querying data in existing tables. Now we're going to have a look at how we can set these tables up from scratch and how we can manipulate them in more advanced ways.

As a starting point, let's have a look at how we can modify data in an existing table.

There are three basic commands to manipulate a table's content:

INSERT: inserts a new row into a table;
DELETE: deletes a specified row;
UPDATE: changes attributes within a row.

We're going to look at each of them in turn using a small version of our Star table from the previous activity.
*/

/* The INSERT statement */

/* The INSERT statement adds a row to an existing table using the following syntax:

INSERT INTO <tablename> (<attributes>) VALUES (...);
You can optionally pass a list of attributes that define the order. The data goes into the VALUES (...) clause. For example, let's add a new star to our Star table:

  
INSERT INTO Star (kepler_id, t_eff, radius)  
VALUES (2713050, 5000, 0.956);
Have a look at the table before and after the INSERT command using SELECT * FROM Star.

You can insert multiple rows at once using multiple tuples of values:

  
INSERT INTO Star (kepler_id, t_eff, radius) VALUES
  (2713050, 5000, 0.956),
  (2713051, 3100, 1.321);
It is not always necessary to include a list of the attributes, it is still good practice. If the order of the columns in the table change, you don't have to change the INSERT command if you've set the order of attributes in there. For example, the following command works just as well as the one above:

  
INSERT INTO Star (kepler_id, radius, t_eff)
VALUES (2713050, 0.956, 5000);
*/
