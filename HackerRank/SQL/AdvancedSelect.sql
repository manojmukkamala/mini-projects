# Type of Triangle
SELECT CASE WHEN A + B > C AND A + C > B AND B + C > A THEN 
       CASE WHEN A = B AND B = C THEN 'Equilateral' 
            WHEN A = B OR B = C OR A = C THEN 'Isosceles' 
            ELSE 'Scalene' 
            END ELSE 'Not A Triangle' END 
FROM TRIANGLES;


# The PADS
SELECT CONCAT(Name, '(', SUBSTRING(Occupation, 1, 1), ')') as Name
FROM OCCUPATIONS
ORDER BY Name
SELECT CONCAT('There are a total of ',COUNT(*),' ',LOWER(Occupation),'s.') AS Total
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY Total


# Binary Tree Nodes
SELECT N,
CASE 
WHEN P IS NULL THEN "Root"
WHEN N IN (SELECT P FROM BST) THEN "Inner"
ELSE "Leaf"
END AS NodeType
FROM BST
ORDER BY N;


# New Companies
SELECT t1.company_code, founder, COUNT(DISTINCT t2.lead_manager_code), COUNT(DISTINCT t3.senior_manager_code), COUNT(DISTINCT t4.manager_code), COUNT(DISTINCT t5.employee_code)
FROM Company t1
LEFT JOIN Lead_Manager t2 ON t1.company_code = t2.company_code
LEFT JOIN Senior_Manager t3 ON t1.company_code = t3.company_code
LEFT JOIN Manager t4 ON t1.company_code = t4.company_code 
LEFT JOIN Employee t5 ON t1.company_code = t5.company_code
GROUP BY t1.company_code, founder
ORDER BY company_code
