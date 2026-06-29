-- 1. Top 5 Fund Houses by AUM
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV by Month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Funds with Expense Ratio < 1%
SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Top 5 Funds by 5-Year Return
SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 6. Average 3-Year Return by Category
SELECT
    category,
    AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

-- 7. Risk Grade Distribution
SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;

-- 8. Transaction Type Distribution
SELECT
    transaction_type,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Average Investment Amount by City Tier
SELECT
    city_tier,
    AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY city_tier;

-- 10. Total Investors by Gender
SELECT
    gender,
    COUNT(DISTINCT investor_id) AS investors
FROM fact_transactions
GROUP BY gender;