-- -------------------
-- Query Investors data
-- -------------------

-- Select everything form Investor
SELECT *
FROM INVESTORS;
-- Select all from Investor with condition
SELECT * 
FROM INVESTORS 
WHERE ID = 4;
-- Select specific columns from Investor with condition and ordering
SELECT NAME, SSN, ADDRESS
FROM INVESTORS
WHERE ID = 3
ORDER BY SSN;

-- -------------------
-- Update Investor Data
-- -------------------

UPDATE INVESTORS
SET ADDRESS = '122 Third St. Algeria, Al'
WHERE INVESTOR_ID = 3;

-- -------------------
-- JOIN DATA
-- -------------------
SELECT PORTFOLIO.INVESTOR_ID, NAME, SSN, ADDRESS, TICKER
FROM PORTFOLIO, INVESTORS
WHERE PORTFOLIO.INVESTOR_ID = INVESTORS.INVESTOR_ID;

