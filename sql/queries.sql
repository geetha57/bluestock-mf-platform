-- 1. View all records
SELECT * FROM axis_bluechip;

-- 2. Latest NAV
SELECT *
FROM axis_bluechip
ORDER BY date DESC
LIMIT 1;

-- 3. Oldest NAV
SELECT *
FROM axis_bluechip
ORDER BY date ASC
LIMIT 1;

-- 4. Maximum NAV
SELECT MAX(nav) AS max_nav
FROM axis_bluechip;

-- 5. Minimum NAV
SELECT MIN(nav) AS min_nav
FROM axis_bluechip;

-- 6. Average NAV
SELECT AVG(nav) AS average_nav
FROM axis_bluechip;

-- 7. Count records
SELECT COUNT(*) AS total_records
FROM axis_bluechip;

-- 8. NAV greater than 5000
SELECT *
FROM axis_bluechip
WHERE nav > 5000;

-- 9. Latest 10 records
SELECT *
FROM axis_bluechip
ORDER BY date DESC
LIMIT 10;

-- 10. Date range
SELECT MIN(date) AS start_date,
       MAX(date) AS end_date
FROM axis_bluechip;