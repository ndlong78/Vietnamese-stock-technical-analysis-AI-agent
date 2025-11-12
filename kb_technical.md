# PHƯƠNG PHÁP PHÂN TÍCH KỸ THUẬT

## 1. TREND ANALYSIS (Phân tích Xu hướng)

### Logic xác định
```python
def analyze_trend(price, ma20, ma50, ma200):
    # UPTREND: Price > MA20 > MA50 > MA200
    # DOWNTREND: Price < MA20 < MA50 < MA200
    # SIDEWAYS: MA đan xen
    
    if price > ma20 > ma50 > ma200:
        strength = "Mạnh" if (price - ma20)/ma20 > 0.03 else "Vừa"
        return f"📈 UPTREND {strength}"
    elif price < ma20 < ma50 < ma200:
        strength = "Mạnh" if (ma20 - price)/price > 0.03 else "Vừa"
        return f"📉 DOWNTREND {strength}"
    else:
        return "↔️ SIDEWAYS"
```

### Tín hiệu quan trọng
- **Golden Cross**: MA20 cắt lên trên MA50 → Tín hiệu tăng
- **Death Cross**: MA20 cắt xuống dưới MA50 → Tín hiệu giảm
- **Higher High & Higher Low (HH/HL)**: Xu hướng tăng lành mạnh
- **Lower High & Lower Low (LH/LL)**: Xu hướng giảm

### Format đầu ra
```
📊 XU HƯỚNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Khung D1: 📈 UPTREND Mạnh
Khung W1: 📈 UPTREND Vừa
Khung MN: ↔️ SIDEWAYS

Giá: 96,500 (Trên MA20: +2.4%)
MA20: 94,200⬆️ | MA50: 92,800⬆️ | MA200: 88,500⬆️

✅ Điểm mạnh:
- Chuỗi HH & HL liên tiếp
- MA20 dốc lên rõ (góc 35°)
- Giá trên tất cả MA

⚠️ Lưu ý:
- Khoảng cách giá-MA20 giãn rộng → Pullback có thể xảy ra
- Cần xác nhận bằng volume
```

---

## 2. SUPPORT & RESISTANCE (Hỗ trợ & Kháng cự)

### Cách xác định

**1. Horizontal S/R**: Vùng giá test nhiều lần
- Điểm chạm càng nhiều → S/R càng mạnh
- Ít nhất 2-3 lần test thành công

**2. Dynamic S/R**: Các đường MA
- MA20: S/R ngắn hạn
- MA50: S/R trung hạn
- MA200: S/R dài hạn

**3. Psychological levels**: Mốc tròn
- VD: 100,000 / 50,000 / 25,000

**4. Volume Profile**: Vùng khối lượng tập trung
- High Volume Node = S/R mạnh

**5. Fibonacci Retracement**
```python
swing_high = 99500
swing_low = 88500
diff = swing_high - swing_low

fib_levels = {
    '0%': swing_low,                    # 88,500
    '23.6%': swing_low + diff * 0.236,  # 91,096
    '38.2%': swing_low + diff * 0.382,  # 92,702
    '50%': swing_low + diff * 0.5,      # 94,000
    '61.8%': swing_low + diff * 0.618,  # 95,298
    '78.6%': swing_low + diff * 0.786,  # 97,146
    '100%': swing_high,                  # 99,500
    '161.8%': swing_high + diff * 0.618 # 106,298 (Extension)
}
```

### Độ tin cậy S/R

**Mạnh (90%+)**:
- Test 3+ lần thành công
- Trùng nhiều yếu tố (MA + Fib + Psychological)
- Volume spike tại vùng đó

**Trung bình (60-90%)**:
- Test 2 lần
- Trùng 1-2 yếu tố

**Yếu (< 60%)**:
- Chỉ test 1 lần
- Không có xác nhận từ volume

### Format đầu ra
```
🎯 HỖ TRỢ & KHÁNG CỰ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[KHÁNG CỰ]
R3: 99,500 - ATH 2024 (Chạm 2 lần)
R2: 98,100 - BB Upper + Fib 161.8%
R1: 96,800 - High phiên hôm nay ⚠️ YẾU

📍 GIÁ: 96,500
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[HỖ TRỢ]
S1: 95,000 - TC + MA20 ✅ MẠNH (Test 4 lần)
S2: 94,200 - Fib 38.2% + MA50
S3: 92,800 - Fib 50% + Vùng tích lũy
S4: 90,300 - BB Lower + MA200

🔍 Độ tin cậy:
- R1 (96,800): YẾU - Chỉ test 3 lần trong 5 phiên
- S1 (95,000): MẠNH - MA20 + TC + Volume spike + Test thành công 4 lần
```

---

## 3. ICHIMOKU CLOUD

### 3 Bộ tham số cho VN

| Bộ | Tham số | Ưu điểm | Nhược điểm | Phù hợp |
|---|---|---|---|---|
| **Truyền thống** | 9-26-52 | Chuẩn quốc tế, nhiều tài liệu | Tín hiệu nhanh, nhiễu cao | Bluechip, TK cao |
| **Tinh chỉnh VN** | 9-17-33-65 | Phù hợp chu kỳ VN | Cần backtest | VN30, đa số CP |
| **Dao găm** | 65-129 | Lọc nhiễu tốt, trend dài hạn | Rất chậm, bỏ lỡ đầu sóng | Long-term investor |

### Các thành phần

**Tenkan-sen (Chuyển đổi)**: (High9 + Low9) / 2
- Đường chuyển đổi ngắn hạn
- Phản ứng nhanh với giá

**Kijun-sen (Cơ sở)**: (High26 + Low26) / 2
- Đường cơ sở trung hạn
- S/R động quan trọng

**Senkou Span A (Mây trước)**: (Tenkan + Kijun) / 2, shift +26
- Cạnh nhanh của Cloud

**Senkou Span B (Mây sau)**: (High52 + Low52) / 2, shift +26
- Cạnh chậm của Cloud

**Chikou Span (Chậm)**: Close, shift -26
- Đường chậm, xác nhận tín hiệu

### Quy tắc giao dịch

**Bullish Setup (Tín hiệu tăng):**
```
✅ Giá trên Cloud
✅ Cloud màu xanh (Span A > Span B)
✅ Tenkan > Kijun (TK/KJ Cross)
✅ Chikou trên giá 26p trước
✅ Chikou trên Cloud
✅ Future Cloud tăng dần
```

**Bearish Setup (Tín hiệu giảm):**
```
❌ Giá dưới Cloud
❌ Cloud màu đỏ (Span A < Span B)
❌ Tenkan < Kijun
❌ Chikou dưới giá 26p trước
❌ Chikou dưới Cloud
❌ Future Cloud giảm dần
```

**Cơ hội giao dịch:**
- **Mua**: Giá về test Kijun trong uptrend + trên Cloud
- **Bán/Short**: Giá test Kijun trong downtrend + dưới Cloud
- **Breakout**: Giá break qua Cloud với volume lớn

### Format đầu ra
```
☁️ ICHIMOKU (Bộ 9-26-52)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[CẤU TRÚC]
Tenkan-sen: 95,100 ⬆️
Kijun-sen: 93,500 ⬆️
Senkou Span A: 94,300 ⬆️
Senkou Span B: 91,200 ➡️
Chikou Span: 95,800 (Trên giá 26p trước ✅)

Giá vs Cloud: 💚 TRÊN MÂY (+2,300)
Màu Cloud: 🟢 XANH (Span A > Span B - Bullish)
Độ dày Cloud: 3,100 (Hỗ trợ MẠNH)

[TÍN HIỆU] 6/6 Bullish
✅ TK/KJ Cross: Tenkan > Kijun (+1,600)
✅ Giá vs KJ: Price > Kijun (+3,000)
✅ Giá vs Cloud: Trên Cloud
✅ Màu Cloud: Xanh
✅ Chikou: Trên giá & Cloud
✅ Future Cloud: Tăng dần

[CƠNG VÀO LỆNH]
Mua khi: Giá pullback về Kijun (93,500)
Stop Loss: Dưới Cloud (91,000)
Take Profit: R1 (96,800) → R2 (98,100)
```

---

## 4. OSCILLATORS (Chỉ báo Dao động)

### 4.1 RSI (Relative Strength Index)

**Công thức:**
```python
# Bước 1: Tính gains và losses
gains = [max(prices[i] - prices[i-1], 0) for i in range(1, 15)]
losses = [max(prices[i-1] - prices[i], 0) for i in range(1, 15)]

# Bước 2: Average
avg_gain = sum(gains) / 14
avg_loss = sum(losses) / 14

# Bước 3: RS và RSI
RS = avg_gain / avg_loss if avg_loss != 0 else 0
RSI = 100 - (100 / (1 + RS))
```

**Vùng phân loại:**
- **< 30**: OVERSOLD (Quá bán) - Cơ hội mua
- **30-50**: BEARISH NEUTRAL
- **50-70**: BULLISH NEUTRAL
- **> 70**: OVERBOUGHT (Quá mua) - Cân nhắc chốt

**Lưu ý quan trọng:**
⚠️ Trong UPTREND mạnh, RSI có thể ở 70-80 kéo dài nhiều tuần
⚠️ RSI > 70 KHÔNG phải lúc nào cũng là tín hiệu bán

**Divergence:**
```
Bullish Divergence:
- Price: Lower Low
- RSI: Higher Low
→ Áp lực bán yếu dần → Sắp đảo chiều tăng

Bearish Divergence:
- Price: Higher High
- RSI: Lower High
→ Lực mua yếu dần → Sắp đảo chiều giảm
```

### 4.2 MACD (Moving Average Convergence Divergence)

**Công thức:**
```python
EMA12 = calculate_ema(prices, 12)
EMA26 = calculate_ema(prices, 26)

MACD_line = EMA12 - EMA26
Signal_line = calculate_ema(MACD_line, 9)
Histogram = MACD_line - Signal_line
```

**Tín hiệu:**
```
🟢 BULLISH:
- MACD > Signal (Histogram dương)
- Histogram mở rộng (momentum tăng tốc)
- MACD cắt lên trên Signal (Golden Cross)

🔴 BEARISH:
- MACD < Signal (Histogram âm)
- Histogram thu hẹp (momentum giảm tốc)
- MACD cắt xuống dưới Signal (Death Cross)
```

**Divergence tương tự RSI**

### 4.3 Stochastic (14,3,3)

**Công thức:**
```python
# %K
lowest_low = min(prices[-14:])
highest_high = max(prices[-14:])
%K = ((current_close - lowest_low) / (highest_high - lowest_low)) * 100

# %D (SMA của %K)
%D = average(%K[-3:])
```

**Tín hiệu:**
- **%K > %D trong vùng 50-80**: Bullish momentum
- **%K < %D trong vùng 20-50**: Bearish momentum
- **%K < 20**: Oversold
- **%K > 80**: Overbought

### Format đầu ra
```
⚡ OSCILLATORS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[RSI(14)]
Giá trị: 62.3
Vùng: 🟡 BULLISH NEUTRAL (50-70)

 0 ──── 30 ──── 50 ──── 70 ──── 100
 │ Oversold │ Neutral │ Overbought │
                  ▲ 62.3

✅ Trên 50 (momentum tăng)
✅ Chưa vào vùng quá mua
❌ Không phát hiện divergence

[MACD(12,26,9)]
MACD Line: 1.20 ⬆️
Signal Line: 0.80 ⬆️
Histogram: +0.40 (Tăng 3 phiên 📈)

Tín hiệu: 🟢 BULLISH CROSSOVER
- MACD > Signal
- Histogram dương và mở rộng
→ Momentum tăng tốc mạnh

[STOCHASTIC(14,3,3)]
%K: 68.5 | %D: 65.2
Vùng: 🟡 Bullish High

Tín hiệu: Golden Cross trong vùng 50-80
→ Xu hướng tăng ngắn hạn duy trì
```

---

## 5. PATTERNS (Mô hình)

### 5.1 Candlestick Patterns (Nến Nhật)

**Bullish Reversal (Đảo chiều tăng):**

| Pattern | Hình dạng | Điều kiện | Độ tin cậy |
|---------|-----------|-----------|------------|
| **Hammer** | 🔨 | Ở đáy, shadow dài phía dưới | 70% |
| **Bullish Engulfing** | 🟢⬆️ | Nến xanh nuốt nến đỏ | 75% |
| **Morning Star** | ⭐🌅 | 3 nến: Đỏ + Doji + Xanh | 80% |
| **Piercing Line** | ⬆️ | Nến xanh xuyên qua 50% nến đỏ | 65% |

**Bearish Reversal (Đảo chiều giảm):**

| Pattern | Hình dạng | Điều kiện | Độ tin cậy |
|---------|-----------|-----------|------------|
| **Shooting Star** | ☄️ | Ở đỉnh, shadow dài phía trên | 70% |
| **Bearish Engulfing** | 🔴⬇️ | Nến đỏ nuốt nến xanh | 75% |
| **Evening Star** | ⭐🌆 | 3 nến: Xanh + Doji + Đỏ | 80% |
| **Dark Cloud** | ⬇️ | Nến đỏ xuyên qua 50% nến xanh | 65% |

**Continuation (Tiếp diễn):**
- **Doji**: Phân vân, chờ xác nhận
- **Spinning Top**: Không rõ hướng
- **Three White Soldiers**: 3 nến xanh liên tiếp (tiếp tục tăng)
- **Three Black Crows**: 3 nến đỏ liên tiếp (tiếp tục giảm)

### 5.2 Chart Patterns (Mô hình Đồ thị)

**Continuation Patterns:**

**1. Triangle (Tam giác)**
```
Ascending Triangle (Bullish):
      ─────────────  Resistance ngang
     ╱ ╱ ╱ ╱ ╱ ╱ ╱   Higher lows
    ╱ ╱ ╱ ╱ ╱ ╱ ╱
Target = Height + Breakout point

Descending Triangle (Bearish):
   ╲ ╲ ╲ ╲ ╲ ╲ ╲    Lower highs
    ╲ ╲ ╲ ╲ ╲ ╲ ╲
  ─────────────   Support ngang
```

**2. Flag & Pennant**
- Flag: Hình chữ nhật nghiêng
- Pennant: Tam giác nhỏ
- Thường xuất hiện sau một đợt tăng/giảm mạnh
- Breakout cùng chiều với trend trước đó

**Reversal Patterns:**

**1. Head & Shoulders (Đầu Vai)**
```
    Đầu
   ╱  ╲
Vai╱    ╲Vai
  ╱      ╲
─────────────── Neckline

Target = Neckline - (Head - Neckline)
```

**2. Double Top/Bottom**
```
Double Top (M):
 ╱╲    ╱╲
╱  ╲  ╱  ╲  Đảo chiều giảm
    ╲╱

Double Bottom (W):
    ╱╲
╲  ╱  ╲  ╱  Đảo chiều tăng
 ╲╱    ╲╱
```

### Format đầu ra
```
🕯️ PATTERNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[NẾN PHIÊN GẦN NHẤT]
Ngày: 06/11/2024
Pattern: 🟢 BULLISH ENGULFING

     ┌────┐
     │ ▲  │  Hôm nay (Xanh)
 ┌───┤    │  Open: 95.5
 │ ▼ │    │  Close: 96.5
 └───┘────┘  Body lớn, +1.05%
   Hôm qua (Đỏ)

✅ Ý nghĩa:
- Lực mua đẩy từ thấp lên cao
- "Nuốt" nến giảm phiên trước
- Xác nhận: Volume 115% TB ✅

[MÔ HÌNH ĐỒ THỊ]
Phát hiện: 📐 ASCENDING TRIANGLE

      Resistance 96.8
      ─────────────────
     ╱ ╱ ╱ ╱ ╱ ╱ ╱
    ╱ ╱ ╱ ╱ ╱ ╱ ╱  Higher Lows
   ╱ ╱ ╱ ╱ ╱ ╱ ╱
  Support dốc lên

Breakout target: 99,400 (+3.1%)
Stop Loss: < 94,000 (-2.6%)
Risk/Reward: 1:1.2 ✅
```

---

## 6. WYCKOFF METHOD

### 4 Phases chính

**PHASE I: ACCUMULATION (Tích lũy)**

```
Phase A → B → C → D → E
```

**Phase A**: Ngừng downtrend
- PS (Preliminary Support): Hỗ trợ sơ bộ, mua lớn xuất hiện
- SC (Selling Climax): Đỉnh điểm bán tháo
- AR (Automatic Rally): Phục hồi tự động

**Phase B**: Building cause (Tạo nguyên nhân)
- Trading range, test nhiều lần
- Tích lũy của smart money

**Phase C**: Test cuối
- **Spring**: Fake breakdown xuống dưới support → Phục hồi nhanh
  * Đây là test cuối để "lắc" weak hands
  * Volume spike nhưng giá phục hồi ngay = Bullish
- **Test**: Test lại vùng Spring

**Phase D**: Tín hiệu mạnh
- **SOS (Sign of Strength)**: Break qua resistance với volume lớn
- **LPS (Last Point of Support)**: Test lại breakout thành công
- **Back to Support**: Giá về test lại vùng support cũ

**Phase E**: Markup
- Xu hướng tăng chính thức
- Target: Measuring move = Width of range

**PHASE II: MARKUP** (Xu hướng tăng)

**PHASE III: DISTRIBUTION** (Phân phối)
- Tương tự Accumulation nhưng ngược lại
- PSY (Preliminary Supply), BC (Buying Climax)
- **UTAD** (Upthrust After Distribution): Fake breakout lên → Giảm nhanh
- SOW (Sign of Weakness), LPSY

**PHASE IV: MARKDOWN** (Xu hướng giảm)

### Cách giao dịch

**Mua trong Accumulation:**
```
✅ Sau Spring: Entry ngay khi phục hồi lên
✅ Sau SOS: Entry khi break qua resistance
✅ Tại LPS: Entry khi test lại support thành công

Stop Loss: Dưới Spring low
Target: Width of accumulation range
```

**Bán trong Distribution:**
```
✅ Sau UTAD: Short ngay khi giảm
✅ Sau SOW: Short khi break dưới support
✅ Tại LPSY: Short khi test resistance thất bại

Stop Loss: Trên UTAD high
```

### Format đầu ra
```
🏛️ WYCKOFF ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[GIAI ĐOẠN HIỆN TẠI]
Chu kỳ: ACCUMULATION - Phase D

 Phase A | Phase B | Phase C | Phase D | Phase E
(Stop)   (Range)   (Test)   (Markup) (Trend)
                              ▲
                       Vị trí hiện tại

[DẤU HIỆU ĐÃ XẢY RA]
✅ Spring: 92,500 (Fake breakdown → Rally)
✅ LPS: 94,200 (Test thành công, volume giảm)
✅ SOS: 95,500 (Break với volume +180%)
🔄 Back to Support: Đang test 95,000

[DỰ BÁO]
Nếu giữ 95,000:
→ Phase D tiếp diễn (Markup phase)
→ Target: 99,500-102,000 (+3-6%)
→ Thời gian: 2-4 tuần

Nếu break < 94,000:
→ Quay lại Phase B
→ Test lại Spring 92,500

[GIAO DỊCH]
Entry zone: 95,000-95,500 (LPS area)
Stop Loss: 93,800 (dưới Spring)
Take Profit: 99,500 / 102,000
R/R: 1:2 ✅ Rất tốt
```

---

## 7. ICT CONCEPTS (Smart Money Concepts)

### 7.1 Order Blocks (Khối lệnh)

**Định nghĩa:**
- Vùng giá mà tổ chức/smart money đặt lệnh lớn
- Thường là nến có body lớn trước khi giá di chuyển mạnh

**Bullish Order Block:**
```
          ▲ Price surge
          │
      ┌───┤
      │ ▲ │ ← Bullish OB (Last down candle)
  ────┴───┘    before strong move up
```
- Nến tăng cuối cùng trước khi giá tăng vọt
- Khi giá về test lại OB = Cơ hội mua

**Bearish Order Block:**
- Nến giảm cuối cùng trước khi giá giảm sâu
- Test lại = Cơ hội bán

### 7.2 Fair Value Gap (FVG)

**Định nghĩa:**
- Khoảng trống giá giữa 3 nến liên tiếp
- Xảy ra khi thị trường di chuyển quá nhanh, bỏ qua một số vùng giá

**Bullish FVG:**
```
Nến 3: High      ┌──┐
               ╱ Gap! ╲  ← FVG
Nến 1: Low  ┌──┘      └──┐
```
- Gap giữa High của nến 1 và Low của nến 3
- Giá thường quay lại fill gap này

**Cách giao dịch:**
- Entry khi giá quay về fill FVG (50-75%)
- SL ngoài FVG
- TP tại S/R tiếp theo

### 7.3 Liquidity Pools (Vùng thanh khoản)

**Định nghĩa:**
- Vùng tập trung nhiều Stop Loss của traders
- Smart money thường "hunt" liquidity trước khi đảo chiều

**Buy-side Liquidity:**
- Phía trên: Equal Highs, Resistance zones
- Stop Loss của người short
- Giá đạt đây → Trigger SL → Tạo buying pressure

**Sell-side Liquidity:**
- Phía dưới: Equal Lows, Support zones
- Stop Loss của người long
- Giá đạt đây → Trigger SL → Tạo selling pressure

**Liquidity Sweep:**
- Smart money đẩy giá đến liquidity pool
- Trigger stop loss
- Sau đó đảo chiều

### 7.4 Market Structure

**Break of Structure (BoS):**
- Phá vỡ High/Low quan trọng trước đó
- Xác nhận xu hướng tiếp tục

**Change of Character (CHoCH):**
- Thay đổi đặc tính market structure
- VD: Trong uptrend, xuất hiện Lower High
- Cảnh báo đảo chiều sắp xảy ra

### Format đầu ra
```
💎 ICT ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ORDER BLOCKS]
Bullish OB: 94,000-94,500
- Nến tăng mạnh ngày 01/11
- Chưa test lại
- Entry nếu giá về vùng này

Bearish OB: 98,500-99,000
- Nến giảm ngày 28/10
- Đã test 1 lần

[FAIR VALUE GAP]
Bullish FVG: 95,200-95,600
- Gap ngày 04/11
- Chưa fill (0%)
- Giá có thể điều chỉnh về đây

[LIQUIDITY POOLS]
Buy-side: 99,500+ 
- Equal Highs tại 99,400-99,600
- SL của shorts
- Potential target

Sell-side: 93,800-
- Equal Lows
- SL của longs
- Risk nếu break

[MARKET STRUCTURE]
BoS: 95,500 ✅ (Break High 95,300)
CHoCH: Chưa xảy ra
Trend: Bullish intact

→ Xu hướng tăng còn nguyên vẹn
→ Ưu tiên tìm cơ hội mua

[GIAO DỊCH THEO ICT]
Entry: 95,000 (Bullish OB) hoặc 95,400 (FVG 50%)
SL: 93,700 (dưới Sell-side liquidity)
TP1: 98,500 (Bearish OB)
TP2: 99,500 (Buy-side liquidity)
```

---

## 8. VOLUME & MONEY FLOW

### 8.1 Volume Analysis

**Quy tắc cơ bản:**
```
Volume ⬆️ + Price ⬆️ = Xác nhận UPTREND ✅
Volume ⬆️ + Price ⬇️ = Áp lực bán mạnh 🔴
Volume ⬇️ + Price ⬆️ = UPTREND yếu ⚠️
Volume ⬇️ + Price ⬇️ = DOWNTREND yếu dần 🟡
```

**Volume Spike:**
```python
current_vol = 2850000
avg_vol_20 = 2480000
change = (current_vol - avg_vol_20) / avg_vol_20 * 100

if change > 50:
    signal = "🔥 SPIKE - Sự kiện quan trọng"
elif change > 15:
    signal = "⬆️ Tăng đáng kể - Xác nhận"
elif change < -30:
    signal = "⬇️ Giảm mạnh - Thiếu conviction"
else:
    signal = "➡️ Bình thường"
```

**Volume Profile:**
- High Volume Node (HVN): Vùng giao dịch tập trung → S/R mạnh
- Low Volume Node (LVN): Vùng ít giao dịch → Giá di chuyển nhanh qua
- Point of Control (POC): Giá có volume cao nhất → S/R quan trọng nhất

### 8.2 On Balance Volume (OBV)

**Công thức:**
```python
if close_today > close_yesterday:
    OBV += volume_today
elif close_today < close_yesterday:
    OBV -= volume_today
else:
    OBV = OBV_yesterday  # unchanged
```

**Cách sử dụng:**
- OBV tăng → Áp lực mua tích lũy
- OBV giảm → Áp lực bán tích lũy
- OBV flat → Cân bằng

**Divergence (Quan trọng!):**
```
Bullish Divergence:
- Price: Lower Low
- OBV: Higher Low
→ Dù giá giảm nhưng volume mua tăng → Sắp đảo chiều tăng

Bearish Divergence:
- Price: Higher High
- OBV: Lower High
→ Dù giá tăng nhưng volume mua giảm → Sắp đảo chiều giảm
```

### 8.3 Money Flow (Dòng tiền)

**Calculation:**
```python
typical_price = (high + low + close) / 3
money_flow = typical_price * volume

if close > close_yesterday:
    positive_flow += money_flow
else:
    negative_flow += money_flow

money_flow_ratio = positive_flow / negative_flow
MFI = 100 - (100 / (1 + money_flow_ratio))
```

**Interpretation:**
- MFI > 80: Overbought (Quá mua)
- MFI < 20: Oversold (Quá bán)
- Tương tự RSI nhưng có tính đến volume

### Format đầu ra
```
💰 VOLUME & MONEY FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[VOLUME PROFILE - 20 PHIÊN]
Hôm nay: 2,850,000 CP
TB 20p: 2,480,000 CP
So sánh: +14.9% ⬆️ TĂNG ĐÁN KỂ

│              ▓▓▓
│           ▓▓▓▓▓▓
│        ▓▓▓▓▓▓▓▓▓
│     ▓▓▓▓▓▓▓▓▓▓▓▓ ← Hôm nay
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
└───────────────────→
 -20        -10      0

✅ Giải thích:
- Volume tăng cùng giá → Xác nhận uptrend
- Không có spike bất thường → Không pump

[MONEY FLOW]
Giá trị GD: 273 tỷ VNĐ
TB 20 phiên: 238 tỷ VNĐ
Tăng: +14.7%

Phân bổ:
- Khớp lệnh: 268 tỷ (98.2%)
- Thỏa thuận: 5 tỷ (1.8%)

[ON BALANCE VOLUME]
Xu hướng: ⬆️ TĂNG
Divergence: KHÔNG phát hiện
→ Volume hỗ trợ tốt cho giá tăng

[ĐÁNH GIÁ CHUNG]
🟢 Volume Pattern: HEALTHY
- Tăng đều trong uptrend
- Không có red flags
- Xác nhận momentum tích cực
```

---

## 9. TỔNG HỢP & ĐIỂM SỐ

### Scoring System

```python
def calculate_score(analysis):
    scores = {
        'trend': trend_score,      # /10, weight 25%
        'sr': sr_score,            # /10, weight 15%
        'ichimoku': ichimoku_score, # /10, weight 20%
        'oscillators': osc_score,  # /10, weight 15%
        'volume': vol_score,       # /10, weight 10%
        'patterns': pattern_score, # /10, weight 10%
        'fundamentals': fund_score # /10, weight 5%
    }
    
    weights = {
        'trend': 0.25,
        'sr': 0.15,
        'ichimoku': 0.20,
        'oscillators': 0.15,
        'volume': 0.10,
        'patterns': 0.10,
        'fundamentals': 0.05
    }
    
    total = sum(scores[k] * weights[k] for k in scores)
    return round(total, 1)
```

### Đánh giá theo điểm

```
9.0 - 10.0: 🟢 RẤT TỐT - MUA MẠNH
7.0 - 8.9:  🟢 KHÁ TỐT - MUA
5.0 - 6.9:  🟡 TRUNG BÌNH - CHỜ ĐỢI
3.0 - 4.9:  🟠 KÉM - TRÁNH XA
0.0 - 2.9:  🔴 RẤT KÉM - BÁN/SHORT
```

### Format đầu ra
```
📊 BẢNG TỔNG HỢP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Chỉ tiêu       | Điểm | Trọng số | Weighted
---------------|------|----------|----------
Xu hướng       | 8/10 | 25%      | 2.00
S/R            | 7/10 | 15%      | 1.05
Ichimoku       | 8/10 | 20%      | 1.60
Oscillators    | 7/10 | 15%      | 1.05
Volume         | 8/10 | 10%      | 0.80
Patterns       | 7/10 | 10%      | 0.70
Fundamentals   | 8/10 | 5%       | 0.40
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TỔNG ĐIỂM                        | 7.60/10

📝 Đánh giá: 🟢 KHÁ TỐT
Khuyến nghị: MUA & GIỮ

Điểm mạnh:
✅ Xu hướng rõ ràng, momentum tốt
✅ Volume xác nhận
✅ Setup kỹ thuật đầy đủ

Điểm yếu:
⚠️ S/R chưa vững, cần test thêm
⚠️ Pattern mới hình thành

Confidence: 75% (Khá cao)
```

---

## 10. LƯU Ý QUAN TRỌNG

### Khi phân tích, PHẢI:
✅ Phân tích đầy đủ 8 phương pháp
✅ Cross-confirm giữa các methods
✅ Đưa ra confidence level rõ ràng
✅ Có kịch bản bull và bear
✅ Tính toán SL/TP cụ thể
✅ Đánh giá R/R ratio
✅ Check đặc thù thị trường VN (kb_vietnam_market.md)

### KHÔNG được:
❌ Chỉ dựa vào 1-2 indicators
❌ Bỏ qua volume analysis
❌ Quên check divergence
❌ Không có confirmation từ nhiều methods
❌ Đảm bảo chắc chắn 100%

### Độ ưu tiên các phương pháp:
1. **Trend** (Cao nhất) - Trend is your friend
2. **Volume** - Xác nhận mọi tín hiệu
3. **S/R** - Entry/Exit points
4. **Ichimoku / Wyckoff / ICT** - Confirmation & timing
5. **Oscillators** - Fine-tuning
6. **Patterns** - Triggers

### Khi tín hiệu mâu thuẫn:
```
Ví dụ:
✅ Bullish: MA20>MA50, Ichimoku trên cloud, Volume tăng
❌ Bearish: RSI overbought, MACD giảm

→ Đánh giá: Bullish vẫn mạnh hơn (60-70%)
→ Lý do: Trend + Volume > Oscillators
→ Khuyến nghị: Mua nhưng cẩn trọng, SL chặt
```

---

## REFERENCE QUICK

### Công thức nhanh cần nhớ:
```python
# MA
SMA = sum(prices[-n:]) / n

# RSI
RSI = 100 - (100 / (1 + RS))
RS = avg_gain / avg_loss

# MACD
MACD = EMA12 - EMA26
Signal = EMA9(MACD)
Histogram = MACD - Signal

# Bollinger Bands
Middle = MA20
Upper = MA20 + 2*StdDev
Lower = MA20 - 2*StdDev

# Fibonacci
38.2%, 50%, 61.8%, 100%, 161.8%

# Position Size
shares = (capital * risk%) / (entry - SL)

# Risk/Reward
R/R = (TP - Entry) / (Entry - SL)
```

### Ichimoku Signals Quick Check:
```
6/6 Bullish = Very Strong
5/6 = Strong
4/6 = Moderate
3/6 = Neutral
2/6 or less = Weak/Bearish
```

### Volume Rules:
```
Vol↑ Price↑ = Confirm uptrend ✅
Vol↑ Price↓ = Strong selling 🔴
Vol↓ Price↑ = Weak uptrend ⚠️
Vol↓ Price↓ = Weak downtrend 🟡
```

---

**End of kb_technical.md**

Để tham khảo chi tiết hơn về:
- Đặc thù thị trường VN → kb_vietnam_market.md
- Công thức đầy đủ → kb_formulas.md
- Ví dụ thực tế → kb_examples.md
- Thuật ngữ → kb_glossary.md