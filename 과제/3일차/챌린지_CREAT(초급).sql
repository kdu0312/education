-- use report;

-- CREATE TABLE employees (
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100),
--     position VARCHAR(100),
--     salary DECIMAL(10,2)
-- );

-- INSERT INTO employees (name, position, salary) VALUES
--     ('혜린', 'PM', 90000),
--     ('은우', 'Frontend', 80000),
--     ('가을', 'Backend', 92000),
--     ('지수', 'Frontend', 78000),
--     ('민혁', 'Frontend', 96000),
--     ('하온', 'Backend', 130000);

-- SELECT name, salary FROM employees;

-- SELECT name, salary 
-- FROM employees 
-- WHERE position = 'Frontend' AND salary <= 90000;

-- set SQL_SAFE_UPDATES = 0; --> 설정이 안먹어서 명령어로 해

-- UPDATE employees
-- SET salary = salary * 1.10
-- WHERE position = 'PM';

-- DELETE FROM employees
-- WHERE name = '민혁';

-- SELECT position, AVG(salary) AS avg_salary
-- FROM employees
-- GROUP BY position;

-- DROP TABLE employees;
