

--TIME SERIES ANALYSIS 

--1.	Stock Price over year (Close price) 

SELECT [Date]
	, [Close] AS stock_price 	
FROM dbo.[Netflix Stock Price Data set 2002-2022]


--2.	Volumn over year

SELECT [Date]
	, Volume 
FROM dbo.[Netflix Stock Price Data set 2002-2022]

--3.	Daily Market Capitalization = Open Price * Volumn

SELECT [Date]
	, CAST([Close] AS float) * Volume AS market_capitalization	
FROM dbo.[Netflix Stock Price Data set 2002-2022]

--4.	Daily Voltality (Return) = (Close Price 1 / Close price 0) -1 

SELECT [Date]
	, [Close] AS stock_price
	, LAG ([Close]) OVER (ORDER BY [Date]) AS previous_price
	, FORMAT(CAST([Close] AS float) / LAG ([Close]) OVER (ORDER BY [Date]) -1, 'p') AS daily_return
FROM dbo.[Netflix Stock Price Data set 2002-2022]


--5.	Cumulative Return using Close Price 

WITH cum_table AS (
	SELECT [Date]
		, [Close] AS stock_price
		, LAG ([Close]) OVER (ORDER BY [Date]) AS previous_price
		, CAST([Close] AS float) / LAG ([Close]) OVER (ORDER BY [Date]) -1 AS daily_return
	FROM dbo.[Netflix Stock Price Data set 2002-2022]
)
SELECT [Date]
	, FORMAT(daily_return, 'p')
	, FORMAT(SUM(daily_return ) OVER (ORDER BY [Date]), 'p') AS cum_return
FROM cum_table


--Cumulative Return using Adjust Close Price

WITH adj_cum_table AS (
	SELECT [Date]
		, [Adj Close] AS adj_stock_price
		, LAG ([Adj Close]) OVER (ORDER BY [Date]) AS adj_previous_price
		, CAST([Adj Close] AS float) / LAG ([Adj Close]) OVER (ORDER BY [Date]) -1 AS adj_daily_return
	FROM dbo.[Netflix Stock Price Data set 2002-2022]
)
SELECT [Date]
	, FORMAT(adj_daily_return, 'p')
	, FORMAT(SUM(adj_daily_return ) OVER (ORDER BY [Date]), 'p') AS adj_cum_return
FROM adj_cum_table


--6.	The Average Monthly Returns 
WITH group_table AS (
	SELECT MONTH([Date]) AS [month]
		, [Close] AS stock_price
		, LAG ([Close]) OVER (ORDER BY [Date]) AS previous_price
		, CAST([Close] AS float) / LAG ([Close]) OVER (ORDER BY [Date]) -1 AS daily_return
	FROM dbo.[Netflix Stock Price Data set 2002-2022]
)
SELECT [month]
	, FORMAT(AVG(daily_return), 'p') AS avg_monthly_return
FROM group_table
GROUP BY [month]
ORDER BY [month]


--7.	The Average Yearly Returns

WITH group_table AS (
	SELECT YEAR([Date]) AS [year]
		, [Close] AS stock_price
		, LAG ([Close]) OVER (ORDER BY [Date]) AS previous_price
		, CAST([Close] AS float) / LAG ([Close]) OVER (ORDER BY [Date]) -1 AS daily_return
	FROM dbo.[Netflix Stock Price Data set 2002-2022]
)
SELECT [year]
	, FORMAT(AVG(daily_return), 'p') AS avg_yearlyly_return
FROM group_table
GROUP BY [year]
ORDER BY [year]

--8.	The Average Day of Week Returns 
WITH group_table AS (
	SELECT FORMAT(CAST([Date] AS date), 'ddd') AS [weekday]
		, [Close] AS stock_price
		, LAG ([Close]) OVER (ORDER BY [Date]) AS previous_price
		, CAST([Close] AS float) / LAG ([Close]) OVER (ORDER BY [Date]) -1 AS daily_return
	FROM dbo.[Netflix Stock Price Data set 2002-2022]
)
SELECT [weekday]
	, FORMAT(AVG(daily_return), 'p') AS avg_weekday_return
FROM group_table
GROUP BY [weekday]
ORDER BY [weekday]

--9.	Moving Average 10 days, 20 days, 50 days, 100 days of Stock Price (using close price)

SELECT [Date]
	, AVG(CAST([Close] AS float)) OVER (ORDER BY [Date] ROWS BETWEEN 9 PRECEDING AND CURRENT ROW )  AS MA_10days	
	, AVG(CAST([Close] AS float)) OVER (ORDER BY [Date] ROWS BETWEEN 19 PRECEDING AND CURRENT ROW) AS MA_20days
	, AVG(CAST([Close] AS float)) OVER (ORDER BY [Date] ROWS BETWEEN 49 PRECEDING AND CURRENT ROW) AS MA_50days
	, AVG(CAST([Close] AS float)) OVER (ORDER BY [Date] ROWS BETWEEN 99 PRECEDING AND CURRENT ROW) AS MA_100days
FROM dbo.[Netflix Stock Price Data set 2002-2022]