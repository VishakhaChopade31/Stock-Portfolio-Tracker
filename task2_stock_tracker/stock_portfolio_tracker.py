"""
TASK 2: Stock Portfolio Tracker
CodeAlpha Python Programming Internship

A simple stock tracker that calculates total investment based on manually defined stock prices.

Features:
- Input stock names and quantities
- Hardcoded stock price dictionary
- Calculate total portfolio value
- Display portfolio summary
- Save results to CSV file

Author: CodeAlpha Intern
"""

import csv
from datetime import datetime

# Hardcoded stock prices (as of example date)
STOCK_PRICES = {
    "AAPL": 180.50,    # Apple Inc.
    "TSLA": 250.75,    # Tesla Inc.
    "GOOGL": 140.25,   # Alphabet Inc.
    "MSFT": 375.80,    # Microsoft Corp.
    "AMZN": 155.30,    # Amazon.com Inc.
    "META": 485.20,    # Meta Platforms Inc.
    "NVDA": 495.50,    # NVIDIA Corp.
    "NFLX": 480.75,    # Netflix Inc.
}

def display_available_stocks():
    """Display all available stocks and their prices"""
    print("\n" + "=" * 60)
    print("AVAILABLE STOCKS")
    print("=" * 60)
    print(f"{'Stock Symbol':<15} {'Company Name':<25} {'Price ($)':<10}")
    print("-" * 60)
    
    stock_names = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet Inc.",
        "MSFT": "Microsoft Corp.",
        "AMZN": "Amazon.com Inc.",
        "META": "Meta Platforms Inc.",
        "NVDA": "NVIDIA Corp.",
        "NFLX": "Netflix Inc.",
    }
    
    for symbol, price in sorted(STOCK_PRICES.items()):
        print(f"{symbol:<15} {stock_names[symbol]:<25} ${price:<9.2f}")
    print("=" * 60)

def get_portfolio_input():
    """Get user's portfolio input"""
    portfolio = {}
    
    print("\n" + "=" * 60)
    print("BUILD YOUR PORTFOLIO")
    print("=" * 60)
    print("Enter your stock holdings (type 'done' when finished)")
    print("-" * 60)
    
    while True:
        stock_symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock_symbol == 'DONE':
            if portfolio:
                break
            else:
                print("Please add at least one stock to your portfolio!")
                continue
        
        if stock_symbol not in STOCK_PRICES:
            print(f"Error: '{stock_symbol}' is not available. Please choose from the list above.")
            continue
        
        # Get quantity
        while True:
            try:
                quantity = int(input(f"Enter quantity for {stock_symbol}: "))
                if quantity <= 0:
                    print("Please enter a positive number!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        portfolio[stock_symbol] = quantity
        print(f"✓ Added {quantity} shares of {stock_symbol}")
    
    return portfolio

def calculate_portfolio_value(portfolio):
    """Calculate total portfolio value and individual stock values"""
    portfolio_details = []
    total_value = 0
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        stock_value = quantity * price
        total_value += stock_value
        
        portfolio_details.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'value': stock_value
        })
    
    return portfolio_details, total_value

def display_portfolio_summary(portfolio_details, total_value):
    """Display portfolio summary"""
    print("\n" + "=" * 80)
    print("PORTFOLIO SUMMARY")
    print("=" * 80)
    print(f"{'Stock':<10} {'Quantity':<12} {'Price/Share':<15} {'Total Value':<15}")
    print("-" * 80)
    
    for stock in portfolio_details:
        print(f"{stock['symbol']:<10} {stock['quantity']:<12} "
              f"${stock['price']:<14.2f} ${stock['value']:<14.2f}")
    
    print("-" * 80)
    print(f"{'TOTAL PORTFOLIO VALUE:':<52} ${total_value:>14.2f}")
    print("=" * 80)

def save_to_file(portfolio_details, total_value, file_format='csv'):
    """Save portfolio to file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if file_format == 'csv':
        filename = f"portfolio_{timestamp}.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for stock in portfolio_details:
                writer.writerow({
                    'Stock Symbol': stock['symbol'],
                    'Quantity': stock['quantity'],
                    'Price per Share': f"${stock['price']:.2f}",
                    'Total Value': f"${stock['value']:.2f}"
                })
            
            # Add total row
            writer.writerow({
                'Stock Symbol': 'TOTAL',
                'Quantity': '',
                'Price per Share': '',
                'Total Value': f"${total_value:.2f}"
            })
        
        print(f"\n✓ Portfolio saved to: {filename}")
    
    else:  # txt format
        filename = f"portfolio_{timestamp}.txt"
        
        with open(filename, 'w') as txtfile:
            txtfile.write("=" * 80 + "\n")
            txtfile.write("STOCK PORTFOLIO SUMMARY\n")
            txtfile.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            txtfile.write("=" * 80 + "\n\n")
            
            txtfile.write(f"{'Stock':<10} {'Quantity':<12} {'Price/Share':<15} {'Total Value':<15}\n")
            txtfile.write("-" * 80 + "\n")
            
            for stock in portfolio_details:
                txtfile.write(f"{stock['symbol']:<10} {stock['quantity']:<12} "
                            f"${stock['price']:<14.2f} ${stock['value']:<14.2f}\n")
            
            txtfile.write("-" * 80 + "\n")
            txtfile.write(f"{'TOTAL PORTFOLIO VALUE:':<52} ${total_value:>14.2f}\n")
            txtfile.write("=" * 80 + "\n")
        
        print(f"\n✓ Portfolio saved to: {filename}")

def main():
    """Main function"""
    print("\n" + "=" * 60)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 60)
    
    # Display available stocks
    display_available_stocks()
    
    # Get portfolio input
    portfolio = get_portfolio_input()
    
    # Calculate portfolio value
    portfolio_details, total_value = calculate_portfolio_value(portfolio)
    
    # Display summary
    display_portfolio_summary(portfolio_details, total_value)
    
    # Ask to save
    save_choice = input("\nDo you want to save the portfolio? (yes/no): ").lower()
    if save_choice in ['yes', 'y']:
        format_choice = input("Choose format (csv/txt): ").lower()
        if format_choice in ['csv', 'txt']:
            save_to_file(portfolio_details, total_value, format_choice)
        else:
            save_to_file(portfolio_details, total_value, 'csv')
    
    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
