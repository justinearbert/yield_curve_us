# US Yield Curve Spread Analysis 

## Overview
Script to analyze the US Treasury yield curve by comparing 2-year and 10-year Treasury rates.  
It retrieves historical interest rates from FED, calculates the 10Y-2Y spread, and visualizes both the rates and the spread.

## Objective
Understand the shape of the yield curve and its implications for the economy.  
The 10Y-2Y spread is used as a simple indicator of economic growth expectations or potential recession signals:

- **Spread > 0** → Normal curve, indicating economic growth  
- **Spread < 0** → Inverted curve, potential recession   
- **Spread ≈ 0** → Flat curve, economic uncertainty  

## Materials Used
- Python
- Pandas  
- Matplotlib  
- pandas_datareader

Install dependencies with:

```bash
pip install pandas matplotlib pandas_datareader
