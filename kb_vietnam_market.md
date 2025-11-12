# ĐẶC THÙ THỊ TRƯỜNG CHỨNG KHOÁN VIỆT NAM

## 1. CÁC SÀN GIAO DỊCH

### 1.1 HOSE (Sở Giao dịch Chứng khoán TP.HCM)
- **Tên đầy đủ**: Ho Chi Minh Stock Exchange  
- **Niêm yết**: Cổ phiếu công ty lớn, uy tín  
- **Biên độ**: ±7% (Trần/Sàn)  
- **Ví dụ**: VCB, VNM, HPG, VIC, VHM...  
- **Website**: https://www.hsx.vn/  
- **Đơn vị giao dịch**: 100 cổ phiếu (lô chẵn); hỗ trợ giao dịch lô lẻ 1-99 cổ phiếu

### 1.2 HNX (Sở Giao dịch Chứng khoán Hà Nội)
- **Tên đầy đủ**: Hanoi Stock Exchange  
- **Niêm yết**: Công ty vừa và nhỏ  
- **Biên độ**: ±10%  
- **Ví dụ**: PVS, TNG, VCS, PVI...  
- **Website**: https://www.hnx.vn/  
- **Đơn vị giao dịch**: 100 cổ phiếu (lô chẵn); hỗ trợ giao dịch lô lẻ 1-99 cổ phiếu

### 1.3 UPCOM (Thị trường giao dịch chưa niêm yết)
- **Tên đầy đủ**: Unlisted Public Company Market  
- **Niêm yết**: Công ty chưa đủ điều kiện niêm yết  
- **Biên độ**: ±15%  
- **Đặc điểm**: Thanh khoản thấp, rủi ro cao  
- **Giao dịch**: Chỉ có khớp lệnh liên tục (không có phiên ATO/ATC)  
- **Đơn vị giao dịch**: 100 cổ phiếu (lô chẵn); có thể giao dịch lô lẻ (1-99 cổ phiếu)

---

## 2. BIÊN ĐỘ GIAO DỊCH

### 2.1 Quy định biên độ

**Công thức tính:**
```python
def calculate_price_range(ref_price, exchange='HOSE'):
    """
    ref_price: Giá tham chiếu (TC)
    exchange: 'HOSE', 'HNX', hoặc 'UPCOM'
    """
    limits = {
        'HOSE': 0.07,   # ±7%
        'HNX': 0.10,    # ±10%
        'UPCOM': 0.15   # ±15%
    }

    limit = limits[exchange]
    ceiling = ref_price * (1 + limit)
    floor = ref_price * (1 - limit)

    return {
        'ceiling': round(ceiling, -2),  # Làm tròn 100đ
        'floor': round(floor, -2),
        'ref': ref_price
    }

# Ví dụ
prices = calculate_price_range(95000, 'HOSE')
# ceiling: 101,650 (Trần)
# floor: 88,350 (Sàn)
# ref: 95,000 (TC)
```

### 2.2 Màu sắc giá

```
🟣 TÍM/MAGENTA: Giá trần (Ceiling)
🟢 XANH: Giá > TC (Tăng)
🟡 VÀNG: Giá tham chiếu (TC)
🔴 ĐỎ: Giá < TC (Giảm)
🔵 XANH DƯƠNG: Giá sàn (Floor)
```

### 2.3 Ý nghĩa biên độ trong phân tích

**Giá gần TRẦN (>95% biên độ):**
```
⚠️ Rủi ro:
- Khó mua thêm (bị limit)
- Có thể là pump
- Ngày mai thường gap down hoặc sideways

✅ Cơ hội:
- Momentum rất mạnh
- Có thể tiếp tục trần T+1, T+2
- Đặc biệt nếu có tin tốt
```

**Giá gần SÀN (>95% biên độ):**
```
⚠️ Rủ ro:
- Panic selling
- Có thể tiếp tục sàn nhiều ngày
- Tin xấu hoặc thao túng

✅ Cơ hội:
- Oversold ngắn hạn
- Nếu có tin tốt bác bỏ → Rebound mạnh
- Chỉ mua nếu fundamental vẫn tốt
```

**Giá ở GIỮA biên độ (±3%):**
```
✅ Lý tưởng:
- Linh hoạt cả 2 chiều
- Dễ vào/ra lệnh
- Thanh khoản tốt
- Ít rủi ro về biên độ
```

### Format kiểm tra
```
🇻🇳 BIÊN ĐỘ (HOSE ±7%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Giá TC: 95,000  
Trần: 101,650 (Còn +5.3% = 53% biên độ)  
Sàn: 88,350 (Xa -8.5% = 85% biên độ)

Đánh giá: 🟢 Ở giữa biên độ  
→ Linh hoạt, dễ giao dịch  
→ Không có risk về limit  
```

---

## 3. PHIÊN GIAO DỊCH

### 3.1 Lịch giao dịch chuẩn

```
09:00 - 09:15  │ ATO (At The Open)
               │ Khớp lệnh mở cửa - 1 giá duy nhất
               │
09:15 - 11:30  │ Liên tục - Buổi sáng
               │ Khớp theo giá thị trường
               │
11:30 - 13:00  │ NGHỈ TRƯA
               │
13:00 - 14:30  │ Liên tục - Buổi chiều
               │
14:30 - 14:45  │ ATC (At The Close)
               │ Khớp lệnh đóng cửa - 1 giá duy nhất
```

**Lưu ý (KRX 2025)**: Từ 2025, lệnh ATO/ATC không còn được ưu tiên tuyệt đối so với lệnh LO trong các phiên khớp lệnh định kỳ (quy tắc ưu tiên thay đổi khi áp dụng hệ thống KRX mới).

### 3.2 ATO (At The Open) - Quan trọng!

**Cách hoạt động:**
- Tất cả lệnh đặt trước 9:00 được tập hợp
- Hệ thống tìm giá khớp nhiều lệnh nhất
- Khớp 1 lần duy nhất lúc 9:15

**Phân tích ATO:**
```python
def analyze_ato(ato_price, ref_price, ato_volume, avg_volume):
    change = (ato_price - ref_price) / ref_price * 100
    vol_ratio = ato_volume / avg_volume

    # Gap analysis
    if change > 2:
        gap = "Gap Up mạnh (+{:.1f}%)".format(change)
        signal = "🟢 Tâm lý tích cực, tin tốt overnight"
    elif change > 0.5:
        gap = "Gap Up nhẹ"
        signal = "🟢 Tích cực vừa phải"
    elif change < -2:
        gap = "Gap Down mạnh ({:.1f}%)".format(change)
        signal = "🔴 Tâm lý tiêu cực, tin xấu hoặc panic"
    elif change < -0.5:
        gap = "Gap Down nhẹ"
        signal = "🔴 Tiêu cực vừa phải"
    else:
        gap = "Không gap"
        signal = "🟡 Bình thường"

    # Volume analysis
    if vol_ratio > 0.15:  # ATO thường chiếm 10-20% volume ngày
        vol_signal = "Volume cao - Conviction mạnh"
    elif vol_ratio < 0.05:
        vol_signal = "Volume thấp - Thiếu quan tâm"
    else:
        vol_signal = "Volume bình thường"

    return {
        'gap': gap,
        'signal': signal,
        'volume_signal': vol_signal
    }
```

**Format đầu ra:**
```
ATO ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Giá ATO: 95,500 (TC: 95,000)  
Gap: +0.53% (Gap Up nhẹ)  
Volume: 348K CP (14% volume ngày)

Phân tích:  
🟢 Tâm lý mở cửa tích cực  
✅ Volume khớp tốt  
→ Kỳ vọng phiên giao dịch tích cực  
```

### 3.3 ATC (At The Close) - Quan trọng!

**Cách hoạt động:**
- Lệnh đặt từ 14:30-14:45
- Khớp 1 lần lúc 14:45
- Giá đóng cửa chính thức

**Phân tích ATC:**
```python
def analyze_atc(atc_price, ato_price, high, low, atc_volume):
    # So với ATO
    ato_change = (atc_price - ato_price) / ato_price * 100

    # Vị trí trong phiên
    range_size = high - low
    position = (atc_price - low) / range_size if range_size > 0 else 0.5

    # Đánh giá
    if ato_change > 1:
        trend = "🟢 Tăng mạnh suốt phiên"
        sentiment = "Lực mua mạnh, kỳ vọng tiếp tục tích cực"
    elif ato_change > 0:
        trend = "🟢 Tăng nhẹ"
        sentiment = "Tích cực nhưng không mạnh"
    elif ato_change < -1:
        trend = "🔴 Giảm mạnh"
        sentiment = "Chốt lời/cắt lỗ cuối phiên, cảnh giác"
    elif ato_change < 0:
        trend = "🔴 Giảm nhẹ"
        sentiment = "Hơi tiêu cực"
    else:
        trend = "➡️ Đi ngang"
        sentiment = "Trung tính"

    # Close position
    if position > 0.8:
        close_pos = "Gần High (Top {:.0f}%) - Rất mạnh".format(position*100)
    elif position > 0.6:
        close_pos = "Trên TB (Top {:.0f}%) - Khá tốt".format(position*100)
    elif position > 0.4:
        close_pos = "Giữa range - Trung tính"
    elif position > 0.2:
        close_pos = "Dưới TB (Bottom {:.0f}%) - Yếu".format((1-position)*100)
    else:
        close_pos = "Gần Low (Bottom {:.0f}%) - Rất yếu".format((1-position)*100)

    return {
        'trend': trend,
        'sentiment': sentiment,
        'close_position': close_pos,
        'volume': atc_volume
    }
```

**Format đầu ra:**
```
ATC ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Giá ATC: 96,500 (ATO: 95,500)  
Thay đổi: +1,000 (+1.05%)  
Volume: 420K CP (17% volume ngày)

So với range: Gần High (Top 85%)  
Range ngày: 94,200 - 96,800

Phân tích:  
🟢 Tăng đều suốt phiên  
✅ Đóng cửa gần đỉnh ngày  
✅ Volume ATC tốt  
→ Tâm lý kỳ vọng tiếp tục tích cực phiên sau  
```

### 3.4 So sánh ATO vs ATC

```
TH1: ATC > ATO (↗️)
→ Tích cực suốt phiên
→ Lực mua mạnh
→ Khả năng cao tiếp tục tích cực T+1

TH2: ATC < ATO (↘️)
→ Chốt lời cuối phiên
→ Hoặc có tin xấu chiều
→ Cẩn trọng phiên sau

TH3: ATC ≈ ATO (→)
→ Dao động trong ngày
→ Trung tính

TH4: ATC tăng mạnh so ATO + Volume cao
→ Accumulation rõ ràng
→ Tín hiệu rất tốt

TH5: ATC giảm mạnh so ATO + Volume thấp
→ Thiếu conviction
→ Cảnh giác
```

---

## 4. THANH KHOẢN

### 4.1 Phân loại theo volume

```python
def classify_liquidity(avg_volume_20):
    """
    avg_volume_20: Khối lượng TB 20 phiên (shares)
    """
    if avg_volume_20 > 5_000_000:
        return {
            'level': 'Rất tốt',
            'emoji': '🟢',
            'desc': 'Bluechip, dễ vào/ra lệnh',
            'slippage': 'Rất thấp (< 0.1%)',
            'suitable': 'Mọi loại trading'
        }
    elif avg_volume_20 > 1_000_000:
        return {
            'level': 'Tốt',
            'emoji': '🟢',
            'desc': 'Thanh khoản tốt, ít ảnh hưởng giá',
            'slippage': 'Thấp (0.1-0.3%)',
            'suitable': 'Mọi loại trading'
        }
    elif avg_volume_20 > 200_000:
        return {
            'level': 'Trung bình',
            'emoji': '🟡',
            'desc': 'Vào/ra lệnh cẩn thận',
            'slippage': 'Trung bình (0.5-1%)',
            'suitable': 'Trade ngắn hạn hoặc đầu tư'
        }
    else:
        return {
            'level': 'Thấp',
            'emoji': '🔴',
            'desc': 'Khó vào/ra lệnh lớn',
            'slippage': 'Cao (> 1%)',
            'suitable': 'Đầu tư dài hạn'
        }
```

**Mức thanh khoản (20 phiên):**
- > 5 triệu CP/ngày: 🟢 **Rất tốt**
- 1-5 triệu: 🟢 **Tốt**
- 200k-1 triệu: 🟡 **Trung bình**
- < 200k: 🔴 **Thấp**

**Ảnh hưởng:** Thanh khoản tốt giúp **dễ giao dịch**, ngược lại thanh khoản thấp **tăng rủi ro** (khó thoát hàng, spread cao).

---

## 5. ROOM NGOẠI (Foreign Ownership)

### 5.1 Quy định

**Giới hạn sở hữu:**
- **Mặc định**: 49% vốn điều lệ  
- **Ngành đặc biệt**: Thấp hơn (VD: Hàng không 30%, Ngân hàng 30%)  
- **Một số công ty**: Được nới lên 100%  

⚠️ Lưu ý: Nhà đầu tư nước ngoài cần kiểm tra giới hạn room của ngành nghề và từng mã cổ phiếu trước khi đầu tư.

**Công thức:**
```python
def analyze_foreign_room(current_foreign_ownership, limit=49):
    """
    current_foreign_ownership: % sở hữu hiện tại
    limit: Giới hạn (thường 49%)
    """
    remaining = limit - current_foreign_ownership
    usage_rate = (current_foreign_ownership / limit) * 100

    if remaining < 1:
        status = {
            'level': '🔴 Hết room',
            'risk': 'CAO',
            'impact': 'NN không mua được → Áp lực bán nếu NN muốn thoát'
        }
    elif remaining < 3:
        status = {
            'level': '🟠 Gần hết',
            'risk': 'TRUNG BÌNH CAO',
            'impact': 'NN khó mua thêm, cẩn trọng khi NN bán ròng'
        }
    elif remaining < 10:
        status = {
            'level': '🟡 Còn ít',
            'risk': 'TRUNG BÌNH',
            'impact': 'NN vẫn mua được nhưng hạn chế'
        }
    else:
        status = {
            'level': '🟢 Còn nhiều',
            'risk': 'THẤP',
            'impact': 'NN có thể mua thoải mái'
        }

    return {
        'current': current_foreign_ownership,
        'limit': limit,
        'remaining': remaining,
        'usage_rate': usage_rate,
        **status
    }
```

### 5.2 Ảnh hưởng đến giá

**Room còn nhiều (>10%):**
```
✅ Tích cực:
- NN có thể mua thêm
- Dòng tiền ngoại dễ vào
- Ít rủi ro bị "kẹt" room

⚠️ Lưu ý:
- Nếu NN bán ròng vẫn có áp lực
```

**Room gần hết (<3%):**
```
⚠️ Rủi ro:
- NN không mua thêm được
- Nếu NN muốn thoát → Bán ròng mạnh
- Giá khó tăng nếu chỉ dựa vào NN

✅ Cơ hội:
- Nếu có "deal room" → Giá có thể tăng đột biến
```

### 5.3 Theo dõi dòng tiền ngoại

**Mua ròng dương (+):**
```
✅ Tín hiệu tích cực
- NN đang tích lũy
- Confidence vào cổ phiếu
- Hỗ trợ tăng giá

Đặc biệt mạnh nếu:
- Mua ròng liên tục 3-5 phiên
- Volume mua lớn (>10% KLGD)
- Trong uptrend
```

**Bán ròng âm (-):**
```
⚠️ Cảnh báo
- NN đang thoát vốn
- Có thể có thông tin tiêu cực
- Áp lực giảm giá

Đặc biệt nguy hiểm nếu:
- Bán ròng liên tục
- Room gần hết (không mua lại được)
- Volume bán lớn
```

### Format đầu ra
```
🌍 ROOM NGOẠI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Giới hạn: 49%  
Sở hữu hiện tại: 42.3%  
Còn lại: 6.7% (Sử dụng: 86%)

Đánh giá: 🟡 CÒN ÍT  
Rủi ro: TRUNG BÌNH

Dòng tiền NN (5 phiên gần):  
T: +120 tỷ | T-1: +85 tỷ  
T-2: -30 tỷ | T-3: +150 tỷ | T-4: +200 tỷ  
Tổng 5p: +525 tỷ (MUA RÒNG)

Nhận xét:  
✅ NN đang tích cực mua vào  
⚠️ Room còn ít, cẩn trọng nếu NN đảo chiều  
```

---

## 6. YẾU TỐ VĨ MÔ VIỆT NAM

### 6.1 Chính sách tiền tệ NHNN

**Các yếu tố cần theo dõi:**

**1. Lãi suất điều hành (OMO)**
```
Tăng lãi suất:
🔴 Tiêu cực cho TTCK
- Vốn dịch chuyển sang tiết kiệm/trái phiếu
- Chi phí vay tăng → Lợi nhuận doanh nghiệp giảm

Giảm lãi suất:
🟢 Tích cực cho TTCK
- Vốn chảy vào chứng khoán
- Chi phí vay giảm → Lợi nhuận tăng
```

**2. Tỷ giá USD/VND**
```
USD tăng (VND yếu):
🟡 Tùy ngành:
- 🟢 Xuất khẩu (Dệt may, Thủy sản...)
- 🔴 Nhập khẩu (Dầu khí, Điện tử...)

USD giảm (VND mạnh):
- Ngược lại
```

**3. Tăng trưởng tín dụng**
```
Mục tiêu: ~15-16%/năm (2025)

Cao (>16%):
🟢 Tích cực cho ngân hàng
🟢 Kinh tế nóng, doanh nghiệp mở rộng

Thấp (<12%):
🔴 Kinh tế chậm
🔴 Doanh nghiệp thận trọng
```

### 6.2 Kinh tế vĩ mô

**1. GDP Growth**
```
Mục tiêu 2025: ~6.5%

> 6.5%: 🟢 Rất tốt
6.0-6.5%: 🟢 Đạt mục tiêu
5.5-6.0%: 🟡 Chấp nhận được
< 5.5%: 🔴 Dưới kỳ vọng
```

**2. CPI Lạm phát**
```
Mục tiêu 2025: < 4%

< 3%: 🟢 Lý tưởng
3-4%: 🟢 Trong kiểm soát
4-5%: 🟡 Cảnh giác
> 5%: 🔴 Cao, NHNN có thể thắt chặt
```

**3. PMI Manufacturing**
```
> 50: 🟢 Mở rộng (Expansion)
= 50: ➡️ Trung lập
< 50: 🔴 Thu hẹp (Contraction)

> 52: Rất tích cực
48-50: Còn ổn
< 48: Đáng lo
```

### 6.3 Thị trường chứng khoán

**VN-Index levels:**
```
> 1,300: 🟢 Bullish
1,200-1,300: 🟡 Neutral-Bullish
1,100-1,200: 🟡 Neutral
1,000-1,100: 🟠 Neutral-Bearish
< 1,000: 🔴 Bearish
```

**P/E thị trường:**
```
< 12x: Hấp dẫn (Undervalued)
12-15x: Hợp lý (Fair value)
15-18x: Hơi đắt (Slight overvalued)
> 18x: Đắt (Overvalued)
```

**P/B thị trường:**
```
< 1.5x: Rẻ
1.5-2.0x: Hợp lý
2.0-2.5x: Hơi đắt
> 2.5x: Đắt
```

### 6.4 Yếu tố quốc tế ảnh hưởng VN

**1. Lãi suất FED**
```
FED tăng lãi suất:
🔴 Vốn rút khỏi thị trường mới nổi (EM)
🔴 USD mạnh → Vốn ra khỏi VN

FED giữ nguyên/giảm:
🟢 Vốn quay lại EM
🟢 Tích cực cho TTCK VN
```

**2. Chứng khoán Trung Quốc**
```
Correlation cao với VN (~0.7)

CN tăng:
🟢 VN thường theo (cùng khu vực)

CN giảm:
🔴 VN chịu áp lực
```

**3. Giá dầu**
```
Dầu tăng:
🔴 Chi phí sản xuất tăng
🔴 CPI tăng
🟢 Cổ phiếu dầu khí (PVS, PVD...)

Dầu giảm:
🟢 Chi phí giảm
🟢 CPI kiểm soát
🔴 Dầu khí giảm
```

### Format kiểm tra vĩ mô
```
📈 VĨ MÔ VIỆT NAM (Tháng 11/2025)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[CHÍNH SÁCH TIỀN TỆ]  
Lãi suất OMO: 4.50% (Giữ nguyên) ➡️  
Tỷ giá USD/VND: 26,300 (VND yếu) 🟡  
Tín dụng: +15.5% YTD (Gần đạt target) ✅

[KINH TẾ]  
GDP Q3: +8.2% YoY 🟢  
CPI: +3.5% YoY 🟢  
PMI: 54.5 (Mở rộng) 🟢

[THỊ TRƯỜNG]  
VN-Index: 1,580 (+30% YTD)  
P/E: 16.5x (Hơi đắt)  
NN: Mua ròng 2,100 tỷ (5 tuần) ✅

[QUỐC TẾ]  
FED: Giữ nguyên 5.25-5.50% ✅  
Shanghai: +2.0% tuần này 🟢  
Dầu WTI: $60/thùng (Giảm)

ĐÁNH GIÁ CHUNG: 🟢 TÍCH CỰC  
- Vĩ mô trong nước tốt  
- Chính sách hỗ trợ  
- Dòng vốn ngoại tích cực  
→ Môi trường thuận lợi cho TTCK  
```

---

## 7. SEASONALITY (Tính mùa vụ)

### 7.1 Patterns theo quý

**Q1 (Tháng 1-3):**
```
Tháng 1-2: 🟢 Thường tích cực
- Hiệu ứng năm mới
- Kỳ vọng tích cực
- Window dressing từ quỹ

Tháng 3: 🟡 Mixed
- Bắt đầu mùa ĐHCĐ
- Profit-taking sau rally đầu năm
```

**Q2 (Tháng 4-6):**
```
Tháng 4: 🟡 ĐHCĐ season
- Giá tăng trước ĐHCĐ
- Giảm sau ĐHCĐ ("sell the news")

Tháng 5-6: 🟡 Neutral to Bearish
- Sau ĐHCĐ, thiếu catalyst
- Chờ BCTC Q2
```

**Q3 (Tháng 7-9):**
```
Tháng 7-8: 🔴 Thường yếu
- Mùa hè, thanh khoản giảm
- Các quỹ đi nghỉ
- "Summer doldrums"

Tháng 9: 🟡 Bắt đầu hồi phục
- BCTC Q3
- Chuẩn bị rally cuối năm
```

**Q4 (Tháng 10-12):**
```
Tháng 10-11: 🟢 Thường tốt
- Window dressing cuối năm
- Kỳ vọng tích cực
- Các quỹ điều chỉnh danh mục

Tháng 12: 🟡 Mixed
- Đầu tháng: Tiếp tục tích cực
- Cuối tháng: Profit-taking, tax loss harvesting
```

### 7.2 Lưu ý quan trọng

```
⚠️ Seasonality KHÔNG phải quy luật cứng
⚠️ Chỉ là xu hướng thống kê
⚠️ Yếu tố vĩ mô quan trọng hơn

✅ Sử dụng seasonality để:
- Tăng caution trong tháng yếu
- Tận dụng cơ hội trong tháng mạnh
- Kết hợp với technical và fundamental
```

---

## 8. QUY ĐỊNH GIAO DỊCH ĐẶC BIỆT

### 8.1 T+2 Settlement

```
Ngày T: Đặt lệnh mua  
Ngày T+1: Lệnh khớp  
Ngày T+2: Thanh toán và nhận cổ phiếu

Ý nghĩa:
- Mua hôm nay, T+2 mới bán được  
- Ngoại trừ: Giao dịch ký quỹ (có thể bán T+0 nhưng quyền sở hữu vẫn T+2)
```

### 8.2 Lệnh đặc biệt

**LO (Limit Order):**
- Đặt giá cụ thể
- Chỉ khớp tại giá đó hoặc tốt hơn

**MTL (Market-To-Limit):**
- Lệnh thị trường giới hạn: Khớp tại mức giá tốt nhất, phần còn lại (nếu có) chuyển thành lệnh LO
- Áp dụng chung cho HOSE & HNX (thay thế lệnh MP trước đây)

**FAK (Fill And Kill):**
- Khớp ngay tối đa khối lượng có thể, phần còn lại sẽ bị hủy
- Trước đây gọi là lệnh MAK (Match And Kill)

**FOK (Fill Or Kill):**
- Khớp toàn bộ khối lượng, nếu không được sẽ hủy lệnh
- Trước đây gọi là lệnh MOK (Match Or Kill)

### 8.3 Cảnh báo và kiểm soát

**Cảnh báo (Alert):**
```
Điều kiện:
- BCTC lỗ 2 năm liên tiếp
- Vốn chủ sở hữu âm
- Không nộp BCTC đúng hạn

Ảnh hưởng:
⚠️ Cảnh báo rủi ro cho NĐT
⚠️ Biên độ vẫn bình thường
```

**Kiểm soát (Control):**
```
Điều kiện:
- BCTC lỗ 3 năm liên tiếp
- Vi phạm nghiêm trọng quy định

Ảnh hưởng:
🔴 Biên độ giảm còn ±2%
🔴 Thanh khoản rất thấp
🔴 Rủi ro hủy niêm yết
```

**Đình chỉ giao dịch:**
```
Lý do:
- Sự kiện đặc biệt (M&A, họp ĐHCĐ...)
- Chờ thông tin quan trọng
- Vi phạm nghiêm trọng

Thời gian: Tạm thời (vài ngày đến vài tuần)
```

---

## 9. SỰ KIỆN QUAN TRỌNG TRONG NĂM

### 9.1 Đại hội cổ đông (ĐHCĐ)

**Thời điểm:** Tháng 3-5 (chủ yếu tháng 4)

**Pattern giá:**
```
Trước ĐHCĐ (2-4 tuần):
🟢 Thường tăng giá
- Kỳ vọng cổ tức cao
- Tin tốt về kế hoạch kinh doanh

Sau ĐHCĐ (1-2 tuần):
🔴 Thường giảm
- "Sell the news"
- Profit-taking

Ngoại lệ:
✅ Nếu có tin bất ngờ tích cực → Tiếp tục tăng
```

**Thông tin quan trọng:**
- Tỷ lệ cổ tức (tiền mặt, cổ phiếu)
- Kế hoạch SXKD năm sau
- Phát hành thêm cổ phiếu
- M&A, mua lại cổ phiếu quỹ

### 9.2 Công bố BCTC

**Lịch công bố:**
```
Q1: Trước 30/4  
Q2: Trước 30/7  
Q3: Trước 30/10  
Q4 & Năm: Trước 31/3 năm sau  
```

**Phân tích BCTC:**
```
Beat expectations:
🟢 EPS > Dự báo → Giá thường tăng
🟢 Doanh thu tăng trưởng cao
🟢 Lợi nhuận biên cải thiện

Miss expectations:
🔴 EPS < Dự báo → Giá giảm
🔴 Doanh thu giảm
🔴 Chi phí tăng, biên lợi nhuận giảm

In-line:
🟡 Đúng kỳ vọng → Phản ứng nhẹ
```

### 9.3 Ngày cổ tức

**Các mốc quan trọng:**
```
1. Ngày ĐHCĐ quyết định: Công bố tỷ lệ

2. Ngày đăng ký cuối cùng (Record Date):
   - Ngày chốt danh sách
   - Mua trước ngày này mới được hưởng

3. Ngày giao dịch không hưởng quyền (Ex-date):
   - T-2 của Record Date
   - Mua từ ngày này trở đi KHÔNG được hưởng
   - Giá thường giảm = mức cổ tức

4. Ngày thanh toán:
   - Nhận cổ tức (thường sau 1-2 tháng)
```

**Pattern giá:**
```
Trước Ex-date:
🟢 Tăng (người mua để hưởng quyền)

Ex-date:
🔴 Giảm ≈ Mức cổ tức (Technical)
VD: Cổ tức 2,000đ → Giá giảm 2,000đ

Sau Ex-date:
🟡 Phục hồi dần nếu công ty tốt
🔴 Tiếp tục giảm nếu yếu
```

---

## 10. TIPS ĐẶC THÙ KHI GIAO DỊCH VN

### 10.1 Thời điểm tốt giao dịch

**Buổi sáng (9:15-10:30):**
```
✅ Ưu điểm:
- Volume cao, thanh khoản tốt
- Phản ánh rõ sentiment
- Dễ vào lệnh

⚠️ Nhược điểm:
- Biến động mạnh
- Cảm xúc cao
- Dễ FOMO
```

**Trưa (10:30-11:30, 13:00-14:00):**
```
🟡 Trung tính:
- Volume giảm
- Ít biến động
- Phù hợp lệnh limit chờ giá

⚠️ Lưu ý:
- Không phù hợp lệnh market
- Slippage có thể cao hơn
```

**Cuối giờ (14:00-14:30):**
```
⚠️ Cẩn trọng:
- Biến động mạnh
- "Closing pump/dump"
- Đợi ATC xem sentiment

✅ Phù hợp:
- Đánh giá trend ngày
- Đặt lệnh cho T+1
```

### 10.2 Ngày trong tuần

```
Thứ 2:
🟡 Thận trọng
- Phản ánh tin cuối tuần
- Có thể gap mạnh
- Chờ ổn định rồi vào

Thứ 3-4:
🟢 Tốt nhất
- Trend rõ ràng
- Volume ổn định
- Phù hợp mọi chiến lược

Thứ 5:
🟡 Trung tính
- Bắt đầu chốt lời cuối tuần
- Volume có thể giảm

Thứ 6:
⚠️ Cẩn trọng
- Profit-taking mạnh
- Không muốn giữ qua weekend
- Tránh vào lệnh mới lớn
```

### 10.3 Tránh các bẫy phổ biến

**1. Bẫy biên độ:**
```
❌ Không nên:
- Mua khi gần trần (FOMO)
- Bán panic khi gần sàn
- Trade penny stock (<10k)

✅ Nên:
- Chờ pullback trong uptrend
- Mua ở S/R mạnh
- Tập trung bluechip
```

**2. Bẫy ATC:**
```
❌ Không:
- Tin tưởng 100% giá ATC
- "Closing pump" có thể giả

✅ Làm:
- Xem xét cả range ngày
- Check volume ATC
- So sánh với ATO
```

**3. Bẫy ĐHCĐ:**
```
❌ Sai lầm:
- Mua quá muộn (sau Ex-date)
- Giữ qua ĐHCĐ khi giá đã tăng nhiều

✅ Đúng:
- Mua 1-2 tháng trước
- Bán trước Ex-date nếu mục đích chỉ là giá
- Hoặc nắm dài hạn, không quan tâm ngắn hạn
```

**4. Bẫy thanh khoản:**
```
❌ Rủi ro:
- Mua mã thanh khoản thấp
- Khó thoát khi cần

✅ An toàn:
- Chỉ trade mã >500K CP/ngày
- Check bid-ask spread
- Position size nhỏ nếu TK thấp
```

### 10.4 Quy tắc vàng cho trader VN

```
1️⃣ Luôn check biên độ trước khi vào lệnh
   - Giá còn bao nhiêu % đến trần/sàn?

2️⃣ Phân tích ATO/ATC mỗi ngày
   - Sentiment của thị trường

3️⃣ Theo dõi dòng vốn ngoại
   - NN mua/bán ròng bao nhiêu?

4️⃣ Cảnh giác với mã room ngoại gần hết
   - Rủi ro cao nếu NN muốn thoát

5️⃣ Đọc thông báo từ công ty
   - ĐHCĐ, cổ tức, BCTC...
   - Không giao dịch chỉ dựa trên tin đồn

6️⃣ Tôn trọng T+2
   - Không overleverage
   - Giữ cash buffer
   - Cẩn trọng khi dùng margin (đòn bẩy)

7️⃣ Tránh trade trong:
   - Thứ 2 buổi sáng (chờ ổn định)
   - Thứ 6 chiều (closing)
   - Ngày lễ, Tết

8️⃣ Ưu tiên mã VN30
   - Thanh khoản tốt
   - Ít bị thao túng
   - Dữ liệu đáng tin cậy

9️⃣ Kiểm tra vĩ mô định kỳ
   - Lãi suất, GDP, CPI, VN-Index

🔟 Đọc báo cáo từ SSI, VND, VCBS
   - Insight về thị trường
   - Sector rotation
   - Top picks
```

---

## 11. NGUỒN THÔNG TIN UY TÍN

### 11.1 Dữ liệu realtime

```
📱 SSI iBoard:
- https://iboard.ssi.com.vn/
- Dữ liệu realtime, biểu đồ
- Báo cáo phân tích

📊 VNDirect:
- https://trading.vndirect.com.vn/
- Nền tảng giao dịch + thông tin

🔥 FireAnt:
- https://fireant.vn/
- Thân thiện, dễ sử dụng
- Tin tức nhanh

📈 VietStock:
- https://finance.vietstock.vn/
- Dữ liệu chi tiết, sàng lọc cổ phiếu
- Lịch sự kiện ĐHCĐ

💹 Investing.com VN:
- https://vn.investing.com/
- Dữ liệu quốc tế + VN
- Lịch kinh tế
```

### 11.2 Báo cáo phân tích

```
🏦 SSI Research:
- https://www.ssi.com.vn/en/research
- Vĩ mô, ngành, doanh nghiệp
- Morning News daily

🏦 VNDirect Securities:
- Báo cáo strategy, sector
- Company reports

🏦 VCBS (Vietcombank Securities):
- Macro, sector outlook
- Top picks

🏦 FPTS (FPT Securities):
- Technical và fundamental
```

### 11.3 Tin tức

```
📰 CafeF:
- https://cafef.vn/
- Tin chứng khoán, tài chính

📰 VnExpress Kinh Doanh:
- https://vnexpress.net/kinh-doanh
- Tin tức kinh tế tổng quát

📰 Bloomberg Vietnam:
- Tin quốc tế ảnh hưởng VN

📰 Thanh Niên Kinh Tế:
- Phân tích chuyên sâu
```

### 11.4 Dữ liệu chính thống

```
🏛️ Sở GDCK HOSE:
- https://www.hsx.vn/
- Thông báo chính thức
- Quy chế giao dịch

🏛️ Sở GDCK HNX:
- https://www.hnx.vn/
- Dữ liệu HNX, UPCOM

🏛️ Ủy ban Chứng khoán Nhà nước:
- http://www.ssc.gov.vn/
- Văn bản pháp lý
- Thông tin niêm yết

🏦 Ngân hàng Nhà nước:
- https://www.sbv.gov.vn/
- Chính sách tiền tệ
- Tỷ giá, lãi suất

📊 Tổng cục Thống kê:
- https://www.gso.gov.vn/
- GDP, CPI, PMI
- Dữ liệu kinh tế vĩ mô
```

---

## 12. CHECK-LIST ĐẶC THÙ VN

Khi phân tích cổ phiếu VN, PHẢI check:

```
□ Sàn giao dịch (HOSE/HNX/UPCOM)  
□ Biên độ (±7%/10%/15%)  
□ Giá hiện tại vs Trần/Sàn (còn bao nhiêu %)  
□ Thanh khoản (>500K CP/ngày?)  
□ Phiên ATO: Gap? Volume?  
□ Phiên ATC: Trend trong ngày?  
□ Room ngoại (Còn bao nhiêu %?)  
□ Dòng vốn NN (Mua/bán ròng?)  
□ Sự kiện sắp tới (ĐHCĐ, BCTC, cổ tức?)  
□ Cảnh báo/Kiểm soát (Nếu có)  
□ Vĩ mô VN hiện tại  
□ Sector performance (Ngành đang mạnh/yếu?)  
□ VN-Index trend (Cùng chiều hay ngược?)  
□ Seasonality (Tháng nào trong năm?)  
□ Ngày giao dịch (Thứ mấy? Trước/sau lễ?)  
```

---

## 13. FORMAT STANDARD OUTPUT

```
🇻🇳 ĐẶC THÙ THỊ TRƯỜNG VIỆT NAM  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[CƠ BẢN]  
Sàn: HOSE  
Ngành: Ngân hàng (Financials)

[BIÊN ĐỘ ±7%]  
TC: 95,000 | Trần: 101,650 (+7%) | Sàn: 88,350 (-7%)  
Giá hiện tại: 96,500  
→ Cách Trần: 5,150 (5.3%) | Cách Sàn: 8,150 (8.5%)  
→ 🟢 Ở giữa biên độ, linh hoạt

[PHIÊN GIAO DỊCH]  
ATO: 95,500 @ 9:15 (Gap +0.53%, Vol 348K)  
Range: 94,200 - 96,800 (2,600đ = 2.7%)  
ATC: 96,500 @ 14:45 (Vol 420K)  
→ 🟢 Tăng đều suốt phiên, đóng cửa gần đỉnh

[THANH KHOẢN]  
Volume TB 20p: 2.48M CP/ngày  
Hôm nay: 2.85M (+14.9%)  
Giá trị: 273 tỷ  
Phân loại: 🟢 TỐT  
→ Dễ vào/ra, slippage thấp

[ROOM NGOẠI]  
Giới hạn: 30% (Ngân hàng)  
Hiện tại: 24.5%  
Còn lại: 5.5%  
→ 🟡 Còn vừa phải

Dòng vốn NN (5 phiên):  
+120 tỷ | +85 | -30 | +150 | +200  
Tổng: +525 tỷ (MUA RÒNG)  
→ ✅ NN tích cực

[SỰ KIỆN SẮP TỚI]  
- 15/11: BCTC tháng 10  
- 25/11: Họp HĐQT bàn cổ tức  
- 05/12: Ngày GDKHQ nhận cổ tức  
→ Catalyst tích cực

[VĨ MÔ]  
VN-Index: 1,285 (+0.8% hôm nay) 🟢  
Sector: Financials +1.2% 🟢  
Lãi suất: 4.50% (giữ nguyên)  
→ 🟢 Môi trường thuận lợi

[TỔNG ĐÁNH GIÁ ĐẶC THÙ VN]  
✅ Biên độ linh hoạt  
✅ Thanh khoản tốt  
✅ NN mua ròng mạnh  
✅ ATC tích cực  
✅ Có catalyst (cổ tức)  
⚠️ Room ngoại còn vừa  
→ 🟢 CÁC YẾU TỐ VN HỖ TRỢ TỐT  
```

---

**End of kb_vietnam_market.md**

Reference:  
- Technical analysis → kb_technical.md  
- Formulas → kb_formulas.md  
- Examples → kb_examples.md  
- Terms → kb_glossary.md
