# 📈 Binance Futures Trading Bot – Python Developer Assignment  
A modular CLI-based trading bot for Binance Futures markets with support for:

- Market Orders  
- Limit Orders  
- Stop-Limit Orders  
- OCO Orders  
- TWAP Execution  
- Grid Trading Strategy  
- Input Validation  
- Centralized Client Wrapper  
- Logging & Error Handling  

This project was built as part of a **Python Developer Assignment**, demonstrating knowledge of Python, modular coding, CLI tools, error handling, and algorithmic strategy design.

---

# 🚀 Features Overview

## ✅ 1. Market Orders
BTCUSDT BUY 0.01


---

## ✅ 2. Limit Orders
BTCUSDT BUY 0.01 95000


## 🔥 Advanced Trading Features

### ✔ Stop-Limit Orders

advanced.stop_limit BTCUSDT BUY 0.01 98000 99000

### ✔ OCO (Take-Profit + Stop-Loss)

advanced.oco BTCUSDT BUY 0.01 96000 98000 99000

### ✔ TWAP (Time Weighted Average Price)
Executes a large order split into smaller time-based slices.

advanced.twap BTCUSDT BUY 0.1 --chunks 5 --interval 1


### ✔ Grid Trading Strategy
Creates a grid of limit orders across a price range.

advanced.grid_strategy BTCUSDT BUY 0.01 45000 55000 5


---

# 🧱 Project Structure

![image alt]

---

# 🧩 Technical Highlights

### ⭐ Centralized Binance Client
- Reads API keys from environment variables  
- Falls back to a **MockClient** for safe local testing  
- Ensures no real orders are executed accidentally  

### ⭐ Input Validation
Using `validators.py`:

- Valid symbol (e.g., BTCUSDT)  
- Positive numeric quantity  
- Positive numeric price  

### ⭐ Error Handling
- All scripts validate inputs  
- Try/except blocks around API calls  
- Human-readable error messages  

### ⭐ Logging
Every action is logged into `bot.log`:

- Order details  
- Errors  
- Strategy execution logs  

---

# 🛠️ Requirements

### 📌 Python Version  
Python **3.10+** recommended.




## 📈 Results & Impact


python market_orders.py BTCUSDT BUY 0.01

![image alt](https://github.com/Kaif2596/Mohd-Kaif-Ansari-Binance-bot/blob/main/screenshots/Screenshot%20(66).png)

python limit_orders.py BTCUSDT BUY 0.01 95000

![image alt](https://github.com/Kaif2596/Mohd-Kaif-Ansari-Binance-bot/blob/main/screenshots/Screenshot%20(67.png)

python -m advanced.stop_limit BTCUSDT BUY 0.01 98000 99000

![image alt](https://github.com/Kaif2596/Mohd-Kaif-Ansari-Binance-bot/blob/main/screenshots/Screenshot%20(68.png)

python -m advanced.oco BTCUSDT BUY 0.01 96000 98000 99000

![image alt](https://github.com/Kaif2596/Mohd-Kaif-Ansari-Binance-bot/blob/main/screenshots/Screenshot%20(69.png)

python -m advanced.twap BTCUSDT BUY 0.1 --chunks 5 --interval 1

![image alt](https://github.com/Kaif2596/Mohd-Kaif-Ansari-Binance-bot/blob/main/screenshots/Screenshot%20(69.png)

python -m advanced.grid_strategy BTCUSDT BUY 0.01 45000 55000 5

![image alt](https://github.com/Kaif2596/Mohd-Kaif-Ansari-Binance-bot/blob/main/screenshots/Screenshot%2071.png)


## 👨‍💻 Author

- Name: Mohd Kaif Ansari

- Contact : 9354578826

- Email : kaifansari1808@gmail.com

- LinkedIn : https://www.linkedin.com/in/mohd-kaif-ansari-4a93aa31b/


---
