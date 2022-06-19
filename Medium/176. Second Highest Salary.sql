-- MySql 8.0
SELECT(SELECT DISTINCT salary
       FROM EMPLOYEE
       ORDER BY SALARY DESC
       LIMIT 1 OFFSET 1)
as SECONDHIGHESTSALARY

-- much faster:
/*
SELECT max(salary) as SecondHighestSalary
FROM Employee
WHERE salary < (SELECT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1)
*/
