SELECT EMPLOYEES.BRANCH_ID, SUM(PRICE) as 매출액
FROM EMPLOYEES INNER JOIN SELLINGS
ON EMPLOYEES.ID = SELLINGS.EMPLOYEE_ID
GROUP BY EMPLOYEES.BRANCH_ID
ORDER BY SUM(PRICE) DESC