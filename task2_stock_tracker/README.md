# Task 2: Stock Portfolio Tracker 📈

## Project Overview
A Python-based stock portfolio management tool that helps users track their stock investments and calculate total portfolio value. Uses hardcoded stock prices for simplicity and includes CSV/TXT export functionality.

## Features ✨
- **8 Major Stocks**: Pre-loaded prices for AAPL, TSLA, GOOGL, MSFT, AMZN, META, NVDA, NFLX
- **Portfolio Builder**: Add multiple stocks with quantities
- **Automatic Calculations**: Computes individual and total values
- **File Export**: Save portfolios to CSV or TXT format
- **Professional Display**: Formatted tables and summaries
- **Input Validation**: Prevents invalid stock symbols and quantities

## How to Run 🚀

### Prerequisites
- Python 3.7 or higher
- Built-in modules only (csv, datetime)

### Installation
1. Download the `stock_portfolio_tracker.py` file
2. Open terminal/command prompt
3. Navigate to the file location

### Running the Program
```bash
python stock_portfolio_tracker.py
```

## Available Stocks 💰

| Symbol | Company Name | Price (USD) |
|--------|-------------|-------------|
| AAPL | Apple Inc. | $180.50 |
| TSLA | Tesla Inc. | $250.75 |
| GOOGL | Alphabet Inc. | $140.25 |
| MSFT | Microsoft Corp. | $375.80 |
| AMZN | Amazon.com Inc. | $155.30 |
| META | Meta Platforms Inc. | $485.20 |
| NVDA | NVIDIA Corp. | $495.50 |
| NFLX | Netflix Inc. | $480.75 |

## Usage Instructions 📋

### Building Your Portfolio

1. **Start the program**: Run `python stock_portfolio_tracker.py`
2. **View available stocks**: Automatically displayed
3. **Enter stock symbol**: Type the symbol (e.g., AAPL)
4. **Enter quantity**: Input number of shares
5. **Add more stocks**: Repeat for each stock
6. **Finish**: Type 'done' when complete
7. **View summary**: Portfolio value displayed
8. **Save** (optional): Export to CSV or TXT

### Sample Session

```
============================================================
STOCK PORTFOLIO TRACKER
============================================================

============================================================
AVAILABLE STOCKS
============================================================
Stock Symbol    Company Name              Price ($) 
------------------------------------------------------------
AAPL            Apple Inc.                $180.50   
MSFT            Microsoft Corp.           $375.80   
TSLA            Tesla Inc.                $250.75   
...

============================================================
BUILD YOUR PORTFOLIO
============================================================
Enter your stock holdings (type 'done' when finished)
------------------------------------------------------------

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity for AAPL: 10
✓ Added 10 shares of AAPL

Enter stock symbol (or 'done' to finish): MSFT
Enter quantity for MSFT: 5
✓ Added 5 shares of MSFT

Enter stock symbol (or 'done' to finish): done

================================================================================
PORTFOLIO SUMMARY
================================================================================
Stock      Quantity     Price/Share     Total Value    
--------------------------------------------------------------------------------
AAPL       10           $180.50         $1,805.00      
MSFT       5            $375.80         $1,879.00      
--------------------------------------------------------------------------------
TOTAL PORTFOLIO VALUE:                                        $3,684.00
================================================================================

Do you want to save the portfolio? (yes/no): yes
Choose format (csv/txt): csv

✓ Portfolio saved to: portfolio_20260201_120530.csv
```

## Output File Formats 📄

### CSV Format
```csv
Stock Symbol,Quantity,Price per Share,Total Value
AAPL,10,$180.50,$1805.00
MSFT,5,$375.80,$1879.00
TOTAL,,,,$3684.00
```

### TXT Format
```txt
================================================================================
STOCK PORTFOLIO SUMMARY
Generated: 2026-02-01 12:05:30
================================================================================

Stock      Quantity     Price/Share     Total Value    
--------------------------------------------------------------------------------
AAPL       10           $180.50         $1,805.00      
MSFT       5            $375.80         $1,879.00      
--------------------------------------------------------------------------------
TOTAL PORTFOLIO VALUE:                                        $3,684.00
================================================================================
```

## Code Structure 📁

```python
stock_portfolio_tracker.py
├── STOCK_PRICES               # Dictionary with stock prices
├── display_available_stocks() # Shows all available stocks
├── get_portfolio_input()      # Collects user's portfolio
├── calculate_portfolio_value()# Computes total value
├── display_portfolio_summary()# Shows formatted summary
├── save_to_file()            # Exports to CSV/TXT
└── main()                     # Main program flow
```

## Key Python Concepts Used 🐍

### 1. Dictionaries
```python
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "GOOGL": 140.25,
}
```

### 2. CSV Module
```python
import csv

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
```

### 3. File Handling
```python
with open(filename, 'w') as txtfile:
    txtfile.write("Portfolio Summary\n")
```

### 4. String Formatting
```python
print(f"{symbol:<10} {quantity:<12} ${price:<14.2f}")
```

### 5. Input Validation
```python
if stock_symbol not in STOCK_PRICES:
    print(f"Error: '{stock_symbol}' is not available")
    continue
```

### 6. Datetime Module
```python
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
```

### 7. Exception Handling
```python
try:
    quantity = int(input(f"Enter quantity: "))
except ValueError:
    print("Please enter a valid number!")
```

## Customization Ideas 💡

### 1. Add More Stocks
```python
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    # Add your own
    "IBM": 145.30,
    "ORCL": 115.80,
}
```

### 2. Add Stock Symbols Dictionary
```python
STOCK_INFO = {
    "AAPL": {"name": "Apple Inc.", "sector": "Technology"},
    "TSLA": {"name": "Tesla Inc.", "sector": "Automotive"}
}
```

### 3. Calculate Profit/Loss
```python
def calculate_profit_loss(purchase_price, current_price, quantity):
    profit = (current_price - purchase_price) * quantity
    percentage = ((current_price - purchase_price) / purchase_price) * 100
    return profit, percentage
```

### 4. Add Portfolio Diversification Analysis
```python
def analyze_diversification(portfolio):
    sectors = {}
    for stock in portfolio:
        sector = STOCK_INFO[stock]['sector']
        sectors[sector] = sectors.get(sector, 0) + portfolio[stock]
    return sectors
```

### 5. Create Portfolio Comparison
```python
def compare_portfolios(portfolio1, portfolio2):
    value1 = calculate_total_value(portfolio1)
    value2 = calculate_total_value(portfolio2)
    difference = value1 - value2
    return difference
```

### 6. Add Real-Time Prices (Advanced)
```python
import yfinance as yf

def get_live_price(symbol):
    stock = yf.Ticker(symbol)
    return stock.info['currentPrice']
```

## Testing Checklist ✅

- [ ] Run the program successfully
- [ ] Add at least 3 different stocks
- [ ] Verify calculations are correct (manual check)
- [ ] Test with maximum quantity (e.g., 10000)
- [ ] Try entering invalid stock symbol
- [ ] Try entering negative quantity
- [ ] Try entering non-numeric quantity
- [ ] Save to CSV and open in Excel/Sheets
- [ ] Save to TXT and verify formatting
- [ ] Test 'done' command works
- [ ] Run program multiple times

## Calculation Verification 🧮

**Manual Test:**
- AAPL: 10 shares × $180.50 = $1,805.00
- MSFT: 5 shares × $375.80 = $1,879.00
- **Total**: $3,684.00 ✓

## Common Issues & Solutions 🔧

**Issue**: Module 'csv' not found
- **Solution**: CSV is built-in, no installation needed. Check Python version.

**Issue**: File not saving
- **Solution**: Check write permissions in the current directory

**Issue**: Wrong calculations
- **Solution**: Verify you're using correct stock symbols (uppercase)

**Issue**: Can't open CSV file
- **Solution**: Use Excel, Google Sheets, or any spreadsheet program

## Real-World Applications 🌍

This project teaches concepts used in:
- 💼 **Financial Applications**: Investment tracking apps
- 📊 **Data Analysis**: Portfolio management tools
- 💰 **Personal Finance**: Wealth tracking systems
- 🏦 **Banking Software**: Investment account dashboards

## Learning Outcomes 📚

After completing this task, you will understand:
- ✅ Dictionary data structures and operations
- ✅ CSV file creation and formatting
- ✅ File I/O operations in Python
- ✅ Basic financial calculations
- ✅ Input validation techniques
- ✅ String formatting for tables
- ✅ Datetime module usage
- ✅ Professional output formatting

## Extension Ideas 🚀

### Beginner Extensions:
1. Add stock purchase date
2. Calculate average purchase price
3. Show top 3 holdings by value
4. Add portfolio name

### Intermediate Extensions:
1. Multiple portfolio support
2. Portfolio comparison feature
3. Historical performance tracking
4. Export to Excel with formatting

### Advanced Extensions:
1. Integrate real-time stock prices (yfinance)
2. Add charts and visualizations (matplotlib)
3. Create GUI version (tkinter)
4. Add database storage (SQLite)

## Sample Output Files 📋

Files are automatically named with timestamps:
- `portfolio_20260201_120530.csv`
- `portfolio_20260201_120530.txt`

This prevents overwriting previous saves!

## Project Timeline ⏱️

- **Understanding**: 20-30 minutes
- **Testing**: 30-45 minutes
- **Customization** (optional): 1-2 hours
- **Documentation**: 30-45 minutes
- **Total**: 2-3.5 hours

## Tips for Success 💯

1. **Test with realistic data**: Use actual quantities you might invest
2. **Verify calculations**: Always double-check math manually
3. **Explore file formats**: Open saved files to see structure
4. **Read the code**: Understand each function's purpose
5. **Add comments**: Document your understanding
6. **Customize**: Make it your own with modifications

## Author 👨‍💻
Created as part of the CodeAlpha Python Programming Internship

## License 📄
Free to use for educational purposes

## Next Steps 🚶

1. **Test thoroughly**: Try different scenarios
2. **Understand calculations**: Verify math manually
3. **Explore file output**: Open saved files
4. **Customize prices**: Update to current market values
5. **Add features**: Implement one customization idea
6. **Document**: Update README with changes
7. **Share**: Upload to GitHub with examples

---

**Ready to track your portfolio? Run `python stock_portfolio_tracker.py` 📈**
