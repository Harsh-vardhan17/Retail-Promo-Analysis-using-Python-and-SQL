{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww34000\viewh21380\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 -- 1. Total Weekly Sales\
SELECT Date, SUM(Weekly_Sales) AS Total_Sales\
FROM `project.dataset.walmart_sales`\
GROUP BY Date\
ORDER BY Date;\
\
-- 2. Top Performing Stores\
SELECT Store, SUM(Weekly_Sales) AS Total_Sales\
FROM `project.dataset.walmart_sales`\
GROUP BY Store\
ORDER BY Total_Sales DESC\
LIMIT 10;\
\
-- 3. Promo vs Non-Promo\
SELECT Holiday_Flag, AVG(Weekly_Sales) AS Avg_Sales\
FROM `project.dataset.walmart_sales`\
GROUP BY Holiday_Flag;\
\
-- 4. Store-wise Sales Over Time\
SELECT Date, Store, SUM(Weekly_Sales) AS Weekly_Sales\
FROM `project.dataset.walmart_sales`\
GROUP BY Date, Store\
ORDER BY Date;\
}
