# Data Dictionary

## fund_master.csv
- amfi_code : Unique AMFI scheme code
- scheme_name : Name of the mutual fund scheme
- fund_house : Mutual fund company
- category : Fund category
- sub_category : Fund sub-category
- plan : Direct/Regular plan
- risk_category : Risk classification

## nav_history.csv
- amfi_code : Scheme code
- date : NAV date
- nav : Net Asset Value

## investor_transactions.csv
- investor_id : Unique investor ID
- transaction_date : Date of transaction
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction amount
- state : Investor state
- city : Investor city
- city_tier : T30/B30 classification
- gender : Investor gender
- kyc_status : KYC verification status

## scheme_performance.csv
- return_1yr_pct : 1-year return
- return_3yr_pct : 3-year return
- return_5yr_pct : 5-year return
- expense_ratio_pct : Expense ratio
- sharpe_ratio : Sharpe ratio
- risk_grade : Risk level

## aum_by_fund_house.csv
- fund_house : Fund house name
- year : Financial year
- aum_crore : Assets Under Management (₹ Crore)