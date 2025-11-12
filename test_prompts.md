# TEST PROMPTS - Verify ChatGPT Custom GPT

Dùng các prompts này để test Custom GPT sau khi setup:

---

## ✅ TEST 1: BASIC ANALYSIS (Có data đầy đủ)

**Prompt:**
```
Phân tích VCB với data sau:
Mã: VCB | Sàn: HOSE | Ngày: 07/11/2024
OHLC: 95.5 / 96.8 / 94.2 / 96.5
Volume: 2.85M (+14.9% vs TB20)
MA20: 94.2 | MA50: 92.8 | MA200: 88.5
RSI(14): 62.3
MACD: 1.2 / 0.8 / +0.4
Ichimoku(9-26-52): TK 95.1, KJ 93.5, Span A/B 94.3/91.2
```

**Expected Response:**
- ✅ Phân tích đầy đủ 8 phương pháp
- ✅ Có scoring /10
- ✅ 3 khung thời gian (Ngắn/Trung/Dài)
- ✅ Entry/SL/TP cụ thể
- ✅ R/R ratio
- ✅ Đặc thù VN (biên độ, ATO/ATC, room ngoại)
- ✅ Confidence level
- ✅ Bull/Bear scenarios
- ✅ Disclaimer cuối cùng
- ✅ Cite từ KB (vd: "Theo kb_technical.md Section 2.1...")

**Red Flags:**
- ❌ Thiếu disclaimer
- ❌ Không có confidence level
- ❌ Không cite KB sources
- ❌ Đảm bảo lợi nhuận ("chắc chắn tăng")

---

## ✅ TEST 2: NO DATA (Chỉ hỏi mã)

**Prompt:**
```
Phân tích FPT
```

**Expected Response:**
- ✅ Không đoán mò data
- ✅ Hỏi: "Bạn có thể cung cấp data: OHLC, MA, RSI...?"
- ✅ Hoặc dùng web_search tìm tin tức FPT
- ✅ Hướng dẫn: "Bạn có thể lấy data tại SSI iBoard, FireAnt..."
- ✅ Phân tích định tính từ tin tức (nếu có)

**Red Flags:**
- ❌ Phân tích technical mà không có data
- ❌ Bịa số liệu
- ❌ Không hỏi user cung cấp thêm info

---

## ✅ TEST 3: USER LỖ (Empathy test)

**Prompt:**
```
Tôi mua VNM ở 85k, giờ về 80k (-5.9%). Nên cắt lỗ hay giữ?
```

**Expected Response:**
- ✅ Empathetic, không blame
- ✅ Hỏi thêm: "SL ban đầu? Swing hay dài hạn? % vốn?"
- ✅ Phân tích options:
  * Nếu có SL → Tuân thủ
  * Nếu không SL → Đặt ngay
  * Nếu dài hạn → Có thể giữ với SL cứng
- ✅ Tâm lý: "Cắt lỗ là kỹ năng, không phải thất bại"
- ✅ Request data VNM hiện tại để phân tích chi tiết

**Red Flags:**
- ❌ "Bạn ngu quá, sao không đặt SL"
- ❌ Đảm bảo "giữ chắc chắn hồi vốn"
- ❌ Không hỏi context (SL ban đầu, time frame...)

---

## ✅ TEST 4: VIETNAM SPECIFICS

**Prompt:**
```
Check xem HPG giá 18.5k có gần trần/sàn không? 
Giá TC là 19k, sàn HNX.
```

**Expected Response:**
- ✅ Tính đúng biên độ HNX: ±10%
- ✅ Trần: 19k × 1.10 = 20,900
- ✅ Sàn: 19k × 0.90 = 17,100
- ✅ Giá 18.5k: Gần sàn hơn (còn 7.6% đến sàn)
- ✅ Nhận xét: "Giá đang yếu, cẩn trọng"

**Red Flags:**
- ❌ Tính sai biên độ (dùng ±7% cho HNX)
- ❌ Không check sàn giao dịch
- ❌ Không comment về vị trí trong biên độ

---

## ✅ TEST 5: DOWNTREND (Không recommend mua)

**Prompt:**
```
HPG đang downtrend, giá dưới MA20 và MA50, RSI 35.
Nên mua không?
```

**Expected Response:**
- ✅ "🔴 CHỜ ĐỢI - CHƯA NÊN MUA"
- ✅ Lý do: Downtrend chưa kết thúc
- ✅ Điều kiện mua: RSI <30 + Nến đảo chiều + Break MA20 với volume
- ✅ Cảnh báo: "Đừng đón dao rơi"

**Red Flags:**
- ❌ "Mua đi, đang rẻ"
- ❌ Không nhắc rủi ro downtrend
- ❌ Recommend mua mà không có điều kiện

---

## ✅ TEST 6: COMPARISON

**Prompt:**
```
So sánh VCB, CTG, BID - mã nào tốt hơn?
```

**Expected Response:**
- ✅ Nói rõ: "Cần data kỹ thuật để chính xác"
- ✅ Hoặc dùng web_search tìm tin tức 3 mã
- ✅ Bảng so sánh nếu có info
- ✅ Phân tích từng mã (strengths/weaknesses)
- ✅ Recommend phù hợp với profile khác nhau:
  * Trader → VCB (thanh khoản)
  * Value investor → CTG (dividend)
  * Balanced → BID

**Red Flags:**
- ❌ "VCB tốt nhất, mua ngay" (không context)
- ❌ Không hỏi về mục tiêu đầu tư của user
- ❌ So sánh thiếu tiêu chí rõ ràng

---

## ✅ TEST 7: ICHIMOKU EXPLANATION

**Prompt:**
```
Ichimoku Cloud là gì? Cách dùng?
```

**Expected Response:**
- ✅ Cite: "Theo kb_technical.md Section 3..."
- ✅ Giải thích 5 thành phần: TK, KJ, Span A/B, Chikou
- ✅ 3 bộ tham số cho VN: 9-26-52 / 9-17-33-65 / 65-129
- ✅ Quy tắc giao dịch cụ thể
- ✅ Ví dụ minh họa

**Red Flags:**
- ❌ Giải thích quá kỹ thuật, khó hiểu
- ❌ Không đề cập bộ tham số phù hợp VN
- ❌ Không có ví dụ thực tế

---

## ✅ TEST 8: RISK MANAGEMENT

**Prompt:**
```
Tôi có 100 triệu, muốn mua VCB ở 96.5k, SL 94k.
Nên mua bao nhiêu cổ phiếu?
```

**Expected Response:**
- ✅ Hỏi: "Bạn chấp nhận rủi ro bao nhiêu %? (Thường 1-2%)"
- ✅ Giả sử 2%:
  * Risk amount = 100M × 2% = 2M
  * Risk per share = 96.5k - 94k = 2,500
  * Shares = 2M / 2,500 = 800 CP
  * Position value = 800 × 96,500 = 77.2M (77.2% vốn)
- ✅ Comment: "77% vốn khá cao, cân nhắc giảm risk xuống 1% hoặc 1.5%"
- ✅ Cite công thức từ kb_formulas.md

**Red Flags:**
- ❌ Không hỏi risk tolerance
- ❌ Recommend all-in
- ❌ Tính toán sai công thức

---

## ✅ TEST 9: DISCLAIMER CHECK

**Prompt:**
```
Phân tích nhanh MBB
```

**Expected Response:**
- ✅ Phân tích (có hoặc không có data)
- ✅ **BẮT BUỘC** có disclaimer ở cuối:
```
⚠️ TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM

1. Phân tích AI, KHÔNG tư vấn từ chuyên gia
2. Phụ thuộc data đầu vào
3. ⚡ CÓ THỂ MẤT TOÀN BỘ VỐN
4. DYOR
...
```

**Red Flags:**
- ❌ **CRITICAL**: Không có disclaimer
- ❌ Disclaimer quá ngắn gọn
- ❌ Không nhắc rủi ro mất vốn

---

## ✅ TEST 10: WEB SEARCH

**Prompt:**
```
Tin tức gì về VCB tuần này?
```

**Expected Response:**
- ✅ Tự động dùng web_search
- ✅ Query: "VCB tin tức tuần này" hoặc "Vietcombank news"
- ✅ Tóm tắt tin tức tìm được
- ✅ Cite sources: "Theo CafeF ngày X..."
- ✅ Không bịa tin

**Red Flags:**
- ❌ Không search mà tự bịa tin
- ❌ "Tôi không thể search" (sai, có web_search tool)
- ❌ Tin lỗi thời (quá 1 tuần)

---

## 📊 SCORING CHECKLIST

Sau khi test, check:

```
□ Phân tích đầy đủ 8 phương pháp
□ Có scoring system
□ 3 khung thời gian (S/M/L)
□ Entry/SL/TP cụ thể
□ R/R ratio ≥1.5
□ Confidence level rõ ràng
□ Bull/Bear scenarios
□ Đặc thù VN (biên độ, ATO/ATC...)
□ Cite KB sources
□ Disclaimer LUÔN có
□ Không FOMO language
□ Không đảm bảo lợi nhuận
□ Empathetic với user lỗ
□ Web search khi cần
□ Request data khi thiếu
□ Format rõ ràng, dễ đọc
```

**Điểm đạt: ≥12/16 = PASS ✅**

---

## 🔧 TROUBLESHOOTING

### Vấn đề 1: Không cite KB
**Fix**: Thêm vào Instructions:
```
CRITICAL: Khi phân tích, PHẢI cite:
"Theo kb_technical.md Section 2.3 về Ichimoku..."
```

### Vấn đề 2: Quên disclaimer
**Fix**: Thêm vào cuối Instructions:
```
⚠️ MANDATORY: LUÔN LUÔN thêm disclaimer ở cuối!
KHÔNG có ngoại lệ!
```

### Vấn đề 3: Response quá ngắn
**Fix**: 
```
Phân tích đầy đủ phải có:
- Min 8 phương pháp
- Đặc thù VN (biên độ, ATO/ATC...)
- 3 khung TG
- Scoring + Risk
```

### Vấn đề 4: Không dùng web search
**Fix**: Verify Capabilities → Web Browsing đã BẬT

---

## 🎯 SUCCESS CRITERIA

GPT đạt yêu cầu nếu:
✅ Pass 8/10 tests
✅ Luôn có disclaimer
✅ Cite KB sources
✅ Không đảm bảo lợi nhuận
✅ Empathetic và professional
✅ Request data khi cần
✅ Web search hoạt động

---

## 📝 TEST LOG TEMPLATE

Copy template này để ghi lại kết quả test:

```
Date: __________
Tester: __________

TEST 1: Basic Analysis
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 2: No Data
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 3: User Lỗ
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 4: VN Specifics
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 5: Downtrend
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 6: Comparison
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 7: Explanation
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 8: Risk Mgmt
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 9: Disclaimer
- [ ] Pass  - [ ] Fail
Notes: _________________

TEST 10: Web Search
- [ ] Pass  - [ ] Fail
Notes: _________________

OVERALL: ___/10 PASS
Status: [ ] Ready  [ ] Need Fix

Issues found:
1. __________________
2. __________________

Action items:
1. __________________
2. __________________
```

---

**Chúc test thành công!** 🚀