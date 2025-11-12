# CÔNG THỨC & TÍNH TOÁN

## 1. INDICATORS (Chỉ báo kỹ thuật)

### 1.1 Moving Averages

**Simple Moving Average (SMA):**
```python
def SMA(prices, period):
    """
    prices: List giá đóng cửa
    period: Số phiên (20, 50, 200...)
    """
    return sum(prices[-period:]) / period

# Ví dụ
prices = [95, 96, 94, 97, 95, 96, 98, ...]
MA20 = SMA(prices, 20)
```

**Exponential Moving Average (EMA):**
```python
def EMA(prices, period):
    """
    EMA nhạy hơn SMA, ưu tiên giá gần đây
    """
    multiplier = 2 / (period + 1)
    ema = prices[0]  # Khởi tạo = giá đầu
    
    for price in prices[1:]:
        ema = (price - ema) * multiplier + ema
    
    return ema

# Hoặc công thức ngắn gọn
EMA_today = (Price_today - EMA_yesterday) * multiplier + EMA_yesterday
```

**Weighted Moving Average (WMA):**
```python
def WMA(prices, period):
    """
    Gắn trọng số cao hơn cho giá gần đây
    """
    weights = list(range(1, period + 1))
    weighted_sum = sum(p * w for p, w in zip(prices[-period:], weights))
    return weighted_sum / sum(weights)
```

---

### 1.2 RSI (Relative Strength Index)

```python
def calculate_RSI(prices, period=14):
    """
    RSI = 100 - (100 / (1 + RS))
    RS = Average Gain / Average Loss
    """
    # Bước 1: Tính changes
    changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    
    # Bước 2: Tách gains và losses
    gains = [max(c, 0) for c in changes]
    losses = [abs(min(c, 0)) for c in changes]
    
    # Bước 3: Tính average (dùng EMA)
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    
    # Smoothing cho các giá trị tiếp theo
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    
    # Bước 4: Tính RS và RSI
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

# Phân loại
def RSI_zone(rsi):
    if rsi < 30:
        return "Oversold (Quá bán)"
    elif rsi > 70:
        return "Overbought (Quá mua)"
    elif rsi > 50:
        return "Bullish Neutral"
    else:
        return "Bearish Neutral"
```

---

### 1.3 MACD

```python
def calculate_MACD(prices, fast=12, slow=26, signal=9):
    """
    MACD Line = EMA(12) - EMA(26)
    Signal Line = EMA(9) of MACD Line
    Histogram = MACD Line - Signal Line
    """
    # Tính EMA
    ema_fast = EMA(prices, fast)
    ema_slow = EMA(prices, slow)
    
    # MACD Line
    macd_line = ema_fast - ema_slow
    
    # Signal Line (EMA của MACD)
    signal_line = EMA([macd_line], signal)
    
    # Histogram
    histogram = macd_line - signal_line
    
    return {
        'macd': macd_line,
        'signal': signal_line,
        'histogram': histogram
    }

# Tín hiệu
def MACD_signal(macd, signal, histogram):
    if macd > signal and histogram > 0:
        return "🟢 Bullish (MACD > Signal)"
    elif macd < signal and histogram < 0:
        return "🔴 Bearish (MACD < Signal)"
    else:
        return "🟡 Neutral"
```

---

### 1.4 Bollinger Bands

```python
def calculate_bollinger_bands(prices, period=20, std_dev=2):
    """
    Middle Band = SMA(20)
    Upper Band = SMA(20) + 2 * Standard Deviation
    Lower Band = SMA(20) - 2 * Standard Deviation
    """
    # Middle Band
    middle = SMA(prices, period)
    
    # Standard Deviation
    variance = sum([(p - middle)**2 for p in prices[-period:]]) / period
    std = variance ** 0.5
    
    # Upper và Lower Bands
    upper = middle + (std_dev * std)
    lower = middle - (std_dev * std)
    
    return {
        'upper': upper,
        'middle': middle,
        'lower': lower,
        'bandwidth': (upper - lower) / middle * 100  # % Bandwidth
    }

# Tín hiệu
def BB_signal(price, upper, lower):
    if price > upper:
        return "⚠️ Giá trên BB Upper - Overbought"
    elif price < lower:
        return "✅ Giá dưới BB Lower - Oversold"
    else:
        return "🟡 Trong bands - Neutral"
```

---

### 1.5 Stochastic Oscillator

```python
def calculate_stochastic(high, low, close, k_period=14, d_period=3):
    """
    %K = ((Current Close - Lowest Low) / (Highest High - Lowest Low)) * 100
    %D = SMA của %K (3 periods)
    """
    # %K calculation
    lowest_low = min(low[-k_period:])
    highest_high = max(high[-k_period:])
    
    k = ((close[-1] - lowest_low) / (highest_high - lowest_low)) * 100
    
    # %D calculation (SMA of %K)
    d = SMA([k], d_period)  # Giả sử có list %K values
    
    return {
        '%K': k,
        '%D': d
    }

# Tín hiệu
def stochastic_signal(k, d):
    if k < 20:
        return "Oversold"
    elif k > 80:
        return "Overbought"
    elif k > d and k > 50:
        return "🟢 Bullish (Golden Cross)"
    elif k < d and k < 50:
        return "🔴 Bearish (Death Cross)"
    else:
        return "🟡 Neutral"
```

---

### 1.6 ATR (Average True Range)

```python
def calculate_ATR(high, low, close, period=14):
    """
    TR = max(High - Low, |High - Close_prev|, |Low - Close_prev|)
    ATR = SMA of TR
    """
    true_ranges = []
    
    for i in range(1, len(high)):
        tr = max(
            high[i] - low[i],
            abs(high[i] - close[i-1]),
            abs(low[i] - close[i-1])
        )
        true_ranges.append(tr)
    
    atr = SMA(true_ranges, period)
    return atr

# Sử dụng: Đặt Stop Loss
def ATR_stop_loss(price, atr, multiplier=2):
    """
    SL = Price - (ATR * multiplier)
    Multiplier thường 1.5 - 3
    """
    return price - (atr * multiplier)
```

---

## 2. FIBONACCI LEVELS

```python
def calculate_fibonacci(swing_high, swing_low, direction='retracement'):
    """
    swing_high: Đỉnh gần nhất
    swing_low: Đáy gần nhất
    direction: 'retracement' hoặc 'extension'
    """
    diff = swing_high - swing_low
    
    if direction == 'retracement':
        # Fibonacci Retracement (từ đáy lên)
        levels = {
            '0%': swing_low,
            '23.6%': swing_low + diff * 0.236,
            '38.2%': swing_low + diff * 0.382,
            '50%': swing_low + diff * 0.5,
            '61.8%': swing_low + diff * 0.618,
            '78.6%': swing_low + diff * 0.786,
            '100%': swing_high
        }
    else:  # extension
        # Fibonacci Extension (mục tiêu sau breakout)
        levels = {
            '0%': swing_high,
            '61.8%': swing_high + diff * 0.618,
            '100%': swing_high + diff * 1.0,
            '161.8%': swing_high + diff * 1.618,
            '261.8%': swing_high + diff * 2.618
        }
    
    return levels

# Ví dụ
swing_high = 99500
swing_low = 88500
fib = calculate_fibonacci(swing_high, swing_low)
# {
#   '0%': 88500,
#   '23.6%': 91096,
#   '38.2%': 92702,
#   '50%': 94000,
#   '61.8%': 95298,
#   '78.6%': 97146,
#   '100%': 99500
# }
```

---

## 3. POSITION SIZING

### 3.1 Risk-Based Position Sizing

```python
def calculate_position_size(capital, risk_percent, entry_price, stop_loss):
    """
    Position Size = (Capital * Risk%) / (Entry - Stop Loss)
    
    capital: Tổng vốn (VNĐ)
    risk_percent: % rủi ro mỗi lệnh (thường 1-2%)
    entry_price: Giá vào lệnh
    stop_loss: Giá cắt lỗ
    """
    risk_amount = capital * (risk_percent / 100)
    risk_per_share = abs(entry_price - stop_loss)
    
    shares = risk_amount / risk_per_share
    shares = int(shares / 100) * 100  # Làm tròn xuống 100 CP
    
    position_value = shares * entry_price
    
    return {
        'shares': shares,
        'position_value': position_value,
        'risk_amount': risk_amount,
        'percentage_of_capital': (position_value / capital) * 100
    }

# Ví dụ
capital = 100_000_000  # 100 triệu
risk = 2  # 2%
entry = 96_500
sl = 94_000

result = calculate_position_size(capital, risk, entry, sl)
# {
#   'shares': 800 CP,
#   'position_value': 77,200,000 VNĐ,
#   'risk_amount': 2,000,000 VNĐ,
#   'percentage_of_capital': 77.2%
# }
```

### 3.2 Fixed Percentage Position Sizing

```python
def fixed_percentage_sizing(capital, allocation_percent, price):
    """
    Đơn giản: Dùng X% vốn cho mã này
    
    allocation_percent: 10%, 20%, 30%...
    """
    amount = capital * (allocation_percent / 100)
    shares = amount / price
    shares = int(shares / 100) * 100  # Làm tròn
    
    actual_amount = shares * price
    
    return {
        'shares': shares,
        'amount': actual_amount,
        'percentage': (actual_amount / capital) * 100
    }
```

### 3.3 Kelly Criterion (Advanced)

```python
def kelly_criterion(win_rate, avg_win, avg_loss):
    """
    Kelly % = W - ((1 - W) / R)
    W = Win rate (0.6 = 60%)
    R = Reward/Risk ratio (avg_win / avg_loss)
    
    Lưu ý: Kelly thường quá aggressive, nên dùng 1/2 Kelly hoặc 1/4 Kelly
    """
    r = avg_win / avg_loss
    kelly = win_rate - ((1 - win_rate) / r)
    
    # Half Kelly (conservative)
    half_kelly = kelly / 2
    
    return {
        'full_kelly': max(0, kelly * 100),  # %
        'half_kelly': max(0, half_kelly * 100),
        'quarter_kelly': max(0, kelly / 4 * 100)
    }

# Ví dụ
win_rate = 0.65  # 65%
avg_win = 3  # Thắng TB +3%
avg_loss = 2  # Thua TB -2%

kelly = kelly_criterion(win_rate, avg_win, avg_loss)
# {
#   'full_kelly': 41.67%,  # Quá cao!
#   'half_kelly': 20.83%,  # Hợp lý
#   'quarter_kelly': 10.42%
# }
```

---

## 4. RISK/REWARD CALCULATION

```python
def calculate_risk_reward(entry, stop_loss, take_profit):
    """
    Risk = Entry - Stop Loss
    Reward = Take Profit - Entry
    R/R Ratio = Reward / Risk
    """
    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)
    rr_ratio = reward / risk if risk > 0 else 0
    
    # Đánh giá
    if rr_ratio >= 3:
        assessment = "✅ Rất tốt (≥3:1)"
    elif rr_ratio >= 2:
        assessment = "✅ Tốt (2-3:1)"
    elif rr_ratio >= 1.5:
        assessment = "🟡 Chấp nhận được (1.5-2:1)"
    elif rr_ratio >= 1:
        assessment = "⚠️ Tối thiểu (1-1.5:1)"
    else:
        assessment = "❌ Không nên vào (<1:1)"
    
    return {
        'risk': risk,
        'reward': reward,
        'ratio': round(rr_ratio, 2),
        'assessment': assessment,
        'risk_percent': (risk / entry) * 100,
        'reward_percent': (reward / entry) * 100
    }

# Ví dụ
entry = 96_500
sl = 94_000
tp1 = 98_500
tp2 = 101_000

rr1 = calculate_risk_reward(entry, sl, tp1)
# {risk: 2500, reward: 2000, ratio: 0.8, assessment: "❌ Không nên"}

rr2 = calculate_risk_reward(entry, sl, tp2)
# {risk: 2500, reward: 4500, ratio: 1.8, assessment: "🟡 Chấp nhận"}
```

---

## 5. EXPECTED VALUE

```python
def expected_value(win_rate, avg_win_percent, avg_loss_percent):
    """
    EV = (Win Rate * Avg Win) - (Loss Rate * Avg Loss)
    
    Nếu EV > 0 → Chiến lược có lợi về dài hạn
    Nếu EV < 0 → Chiến lược thua lỗ về dài hạn
    """
    loss_rate = 1 - win_rate
    ev = (win_rate * avg_win_percent) - (loss_rate * avg_loss_percent)
    
    # Tính expectancy per trade
    if ev > 0:
        status = "✅ Chiến lược khả thi"
        color = "🟢"
    elif ev > -0.5:
        status = "⚠️ Gần hòa vốn, cần cải thiện"
        color = "🟡"
    else:
        status = "❌ Chiến lược thua lỗ"
        color = "🔴"
    
    return {
        'expected_value': round(ev, 2),
        'status': status,
        'color': color,
        'per_100_trades': round(ev * 100, 2)
    }

# Ví dụ
win_rate = 0.60  # 60% thắng
avg_win = 4  # Thắng TB +4%
avg_loss = 2.5  # Thua TB -2.5%

ev = expected_value(win_rate, avg_win, avg_loss)
# {
#   'expected_value': +1.4%,
#   'status': "✅ Chiến lược khả thi",
#   'per_100_trades': +140%  # (Sau 100 lệnh)
# }
```

---

## 6. BREAKEVEN & PROFIT CALCULATION

```python
def calculate_breakeven_profit(entry, shares, commission_rate=0.0015):
    """
    Tính điểm hòa vốn và lợi nhuận
    
    Commission VN: ~0.15% mua + 0.15% bán = 0.3% tổng
    """
    # Chi phí
    buy_commission = entry * shares * commission_rate
    total_cost = (entry * shares) + buy_commission
    
    # Breakeven
    breakeven_price = total_cost / (shares * (1 - commission_rate))
    breakeven_diff = breakeven_price - entry
    
    return {
        'entry_price': entry,
        'shares': shares,
        'total_cost': total_cost,
        'buy_commission': buy_commission,
        'breakeven_price': round(breakeven_price, -2),  # Làm tròn 100đ
        'breakeven_diff': round(breakeven_diff, -2),
        'breakeven_percent': (breakeven_diff / entry) * 100
    }

def calculate_profit_loss(entry, exit, shares, commission_rate=0.0015):
    """
    Tính P/L thực tế sau phí
    """
    # Chi phí mua
    buy_cost = entry * shares
    buy_commission = buy_cost * commission_rate
    total_cost = buy_cost + buy_commission
    
    # Thu về khi bán
    sell_revenue = exit * shares
    sell_commission = sell_revenue * commission_rate
    net_revenue = sell_revenue - sell_commission
    
    # P/L
    pl_amount = net_revenue - total_cost
    pl_percent = (pl_amount / total_cost) * 100
    
    return {
        'entry': entry,
        'exit': exit,
        'shares': shares,
        'total_cost': total_cost,
        'net_revenue': net_revenue,
        'profit_loss': pl_amount,
        'pl_percent': round(pl_percent, 2),
        'total_commission': buy_commission + sell_commission
    }

# Ví dụ Breakeven
entry = 96_500
shares = 800
be = calculate_breakeven(entry, shares)
# {breakeven_price: 96,800, breakeven_diff: 300 (+0.31%)}

# Ví dụ P/L
pl = calculate_profit_loss(96_500, 98_500, 800)
# {profit_loss: +1,551,600, pl_percent: +2.00%}
```

---

## 7. COMPOUND INTEREST

```python
def compound_returns(initial_capital, monthly_return_percent, months):
    """
    Tính lợi nhuận kép
    
    Final = Initial * (1 + R)^N
    """
    r = monthly_return_percent / 100
    final_capital = initial_capital * ((1 + r) ** months)
    total_return = final_capital - initial_capital
    total_return_percent = (total_return / initial_capital) * 100
    
    return {
        'initial': initial_capital,
        'months': months,
        'monthly_return': monthly_return_percent,
        'final_capital': final_capital,
        'total_return': total_return,
        'total_return_percent': round(total_return_percent, 2)
    }

# Ví dụ
initial = 100_000_000  # 100 triệu
monthly = 3  # +3%/tháng
months = 12  # 1 năm

result = compound_returns(initial, monthly, months)
# {
#   'final_capital': 142,576,089,
#   'total_return': 42,576,089,
#   'total_return_percent': +42.58%
# }

# So sánh: Không lãi kép = 3% * 12 = +36%
```

---

## 8. DRAWDOWN CALCULATION

```python
def calculate_drawdown(peak, trough):
    """
    Drawdown = (Trough - Peak) / Peak * 100
    
    Đo lường mức độ giảm từ đỉnh đến đáy
    """
    dd = ((trough - peak) / peak) * 100
    
    if dd > -5:
        severity = "🟢 Nhẹ"
    elif dd > -10:
        severity = "🟡 Trung bình"
    elif dd > -20:
        severity = "🟠 Nặng"
    else:
        severity = "🔴 Rất nặng"
    
    return {
        'peak': peak,
        'trough': trough,
        'drawdown_percent': round(dd, 2),
        'severity': severity,
        'recovery_needed': round(abs(peak / trough - 1) * 100, 2)  # % cần để hồi phục
    }

# Ví dụ
peak = 150_000_000
trough = 120_000_000

dd = calculate_drawdown(peak, trough)
# {
#   'drawdown_percent': -20%,
#   'severity': "🟠 Nặng",
#   'recovery_needed': +25%  # Cần tăng 25% từ 120M để về 150M
# }
```

---

## 9. QUICK REFERENCE

### Công thức nhanh cần nhớ:

```python
# MA
SMA(n) = sum(prices[-n:]) / n

# RSI
RSI = 100 - (100 / (1 + RS))
RS = avg_gain / avg_loss

# MACD
MACD = EMA(12) - EMA(26)
Signal = EMA(9 of MACD)
Histogram = MACD - Signal

# Bollinger Bands
Upper = MA(20) + 2*StdDev
Lower = MA(20) - 2*StdDev

# Fibonacci
38.2%, 50%, 61.8% (Retracement)
161.8%, 261.8% (Extension)

# Position Size
shares = (capital * risk%) / (entry - SL)

# Risk/Reward
R/R = (TP - Entry) / (Entry - SL)
Minimum: 1:1.5

# Expected Value
EV = (Win% * AvgWin) - (Loss% * AvgLoss)

# Breakeven
BE = Entry * (1 + commission_rate)

# Compound
Final = Initial * (1 + R)^N
```

---

**End of kb_formulas.md**