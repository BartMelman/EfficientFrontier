# Efficient Frontier

In modern portfolio theory, the objective is to maximise the return for a given level of risk. Harry Markowitz first introduced the concept of an efficient frontier of assets in 1952. The efficient frontier is a set of portfolio's for which no higher expected return can be created for a level of risk. 

In this project, I investigate several methods of reducing risk of a portfolio. The following methods are investigated:
- Global Minimum Variance (GMV) Portfolio
- Efficient Frontier (in and out-of-sample)
- Efficient Frontier based on stocks
- Efficient Frontier based on sector and industry returns



## Download data
- Download ticker names from the [nasdaq website](https://www.nasdaq.com/market-activity/stocks/screener) and put the csv file in the folder 'data'.

## Install packages

Install the python packages with the following command in the terminal.
```
pip3 install -r requirements.txt
```

## Usage

Run the following notebook with the data analytics. 
```
run main.ipynb
```

## References
- [valid ticker yfinance](https://codereview.stackexchange.com/questions/93609/python-functions-to-determine-if-a-given-ticker-symbol-is-an-etf)
