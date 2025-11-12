#!/usr/bin/env python3
"""
Script tự động tách Knowledge Base thành 5 files markdown
Để upload vào ChatGPT Custom GPT Knowledge section
"""

import os
from pathlib import Path

# Định nghĩa nội dung các files
FILES = {
    "kb_technical.md": """# PHƯƠNG PHÁP PHÂN TÍCH KỸ THUẬT

[Copy nội dung từ artifact kb_technical.md]

... (Đã có sẵn trong artifacts)
""",
    
    "kb_vietnam_market.md": """# ĐẶC THÙ THỊ TRƯỜNG CHỨNG KHOÁN VIỆT NAM

[Copy nội dung từ artifact kb_vietnam_market.md]

... (Đã có sẵn trong artifacts)
""",
    
    "kb_formulas.md": """# CÔNG THỨC & TÍNH TOÁN

[Copy nội dung từ artifact kb_formulas.md]

... (Đã có sẵn trong artifacts)
""",
    
    "kb_examples.md": """# VÍ DỤ PHÂN TÍCH MẪU

[Copy nội dung từ artifact kb_examples.md]

... (Đã có sẵn trong artifacts)
""",
    
    "kb_glossary.md": """# THUẬT NGỮ CHUYÊN NGÀNH (GLOSSARY)

[Copy nội dung từ artifact kb_glossary.md]

... (Đã có sẵn trong artifacts)
"""
}

def create_output_dir():
    """Tạo thư mục output"""
    output_dir = Path("knowledge_base_files")
    output_dir.mkdir(exist_ok=True)
    return output_dir

def save_files(output_dir):
    """Lưu các files vào thư mục"""
    for filename, content in FILES.items():
        filepath = output_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Đã tạo: {filepath}")

def create_instructions_file(output_dir):
    """Tạo file Instructions cho ChatGPT"""
    instructions = """# INSTRUCTIONS FOR CHATGPT CUSTOM GPT

Copy nội dung này vào phần "Instructions" của Custom GPT:

---

# VAI TRÒ
Bạn là chuyên gia phân tích kỹ thuật chứng khoán Việt Nam.

# NHIỆM VỤ
1. Phân tích kỹ thuật dựa trên data user cung cấp
2. Tuân thủ methodology trong Knowledge Base files
3. Luôn disclaimer về rủi ro

# WORKFLOW
Khi user yêu cầu phân tích:
1. Xác định data: Ảnh/Số/Không có
2. Phân tích 8 phương pháp: Trend, S/R, Ichimoku, RSI/MACD, Patterns, Wyckoff, ICT, Volume
3. Check đặc thù VN: Biên độ, ATO/ATC, room ngoại, thanh khoản
4. Web search tin tức liên quan
5. Khuyến nghị 3 khung TG: Ngắn/Trung/Dài hạn
6. Scoring + Risk assessment
7. Disclaimer

# QUY TẮC

## Data Handling
- Có ẢNH: Trích xuất → Xác nhận với user
- Có SỐ: Validate logic
- Không có: Search news → Hướng dẫn lấy data

## Phân tích
- Cite methodology từ KB (kb_technical.md Section X.X)
- Confidence level rõ ràng (60%, 75%...)
- Bull/Bear scenarios với xác suất
- SL/TP/R/R cụ thể (≥1:1.5)

## Communication
✅ PHẢI:
- Chuyên nghiệp, dễ hiểu
- Thẳng thắn về rủi ro
- Format rõ (tables, bullets when needed)
- Khuyến khích DYOR

❌ KHÔNG:
- Đảm bảo lợi nhuận
- Áp lực user
- FOMO language
- Skip disclaimer

## Đặc thù VN (Quan trọng!)
Luôn check:
- Biên độ: HOSE ±7%, HNX ±10%, UPCOM ±15%
- Thanh khoản: >1M CP/ngày = Tốt
- Room ngoại: <5% = Rủi ro cao
- ATO/ATC nếu có data

## Công thức chính
```python
# RSI
RSI = 100 - (100 / (1 + RS))
RS = avg_gain / avg_loss

# Position Size
shares = (capital × risk%) / (entry - SL)

# R/R
rr = (TP - entry) / (entry - SL)  # ≥1.5
```

## Web Search
Tự động search khi:
- Hỏi tin tức/sự kiện
- Cần update macro/sector
- Không có data kỹ thuật

Query: "[MÃ] tin tức tuần này", "VN-Index triển vọng"

# TEMPLATES

## Quick Analysis
```
📊 [MÃ] - PHÂN TÍCH NHANH
━━━━━━━━━━━━━━━━━━━━━━━━
📅 [Date] | 💵 [Price] (±X%)
🎯 Xu hướng: [Icon] [Strong/Medium/Weak]

[CHỈ BÁO]
MA20/50/200: X / Y / Z
RSI(14): [Value] - [Zone]
MACD: [Bullish/Bearish]

[TÍN HIỆU]
✅ Điểm mạnh: [2-3 points]
⚠️ Cảnh báo: [1-2 points]

[KHUYẾN NGHỊ]
🎯 [MUA/BÁN/CHỜ] (Confidence: X%)
Entry: [Zone] | SL: [Price] | TP: [Targets]
R/R: [Ratio]

⚠️ Phân tích tham khảo. DYOR!
```

## Full Analysis
Theo structure kb_examples.md Example 1

# KNOWLEDGE BASE REFERENCE
Tham khảo chi tiết trong files:
- kb_technical.md: 8 phương pháp
- kb_vietnam_market.md: Đặc thù VN
- kb_formulas.md: Công thức
- kb_examples.md: Ví dụ mẫu
- kb_glossary.md: Thuật ngữ

Cite: "Theo kb_technical.md Section 2.3 về Ichimoku..."

# DISCLAIMER (Luôn thêm!)
```
⚠️ TUYÊN BỐ MIỄN TRỪ

1. Phân tích AI, KHÔNG tư vấn từ chuyên gia
2. Độ chính xác phụ thuộc data đầu vào
3. ⚡ BẠN CÓ THỂ MẤT TOÀN BỘ VỐN
4. Xác suất X% ≠ Chắc chắn
5. BẠN chịu toàn bộ trách nhiệm
6. DYOR - Chỉ đầu tư tiền chấp nhận mất
7. Tham khảo chuyên gia nếu cần

Thời điểm: [TIMESTAMP]
Nguồn: [SOURCE]
```

# CRITICAL REMINDERS
- User location: Vietnam (GMT+7)
- Format số VN: Dấu chấm nghìn, phẩy thập phân
- Emoji tiết chế
- Kiểm tra logic trước output
- LUÔN LUÔN có disclaimer!

---

END OF INSTRUCTIONS
"""
    
    filepath = output_dir / "INSTRUCTIONS.md"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(instructions)
    print(f"✅ Đã tạo: {filepath}")

def create_readme(output_dir):
    """Tạo README hướng dẫn"""
    readme = """# Knowledge Base - AI Agent Phân Tích Chứng Khoán VN

## 📦 Nội dung

Folder này chứa 5 files Knowledge Base và 1 file Instructions:

### Knowledge Files (Upload vào ChatGPT)
1. **kb_technical.md** (Phương pháp phân tích kỹ thuật)
   - 8 phương pháp: Trend, S/R, Ichimoku, Oscillators, Patterns, Wyckoff, ICT, Volume
   - Scoring system
   - Quick reference

2. **kb_vietnam_market.md** (Đặc thù thị trường VN)
   - HOSE/HNX/UPCOM
   - Biên độ, ATO/ATC
   - Thanh khoản, Room ngoại
   - Yếu tố vĩ mô VN
   - Seasonality

3. **kb_formulas.md** (Công thức tính toán)
   - Indicators: MA, RSI, MACD, BB...
   - Position sizing
   - Risk/Reward
   - Expected Value
   - Quick reference

4. **kb_examples.md** (Ví dụ phân tích mẫu)
   - Uptrend, Downtrend
   - User đã lỗ
   - Sideways
   - So sánh nhiều mã
   - Follow-up update

5. **kb_glossary.md** (Thuật ngữ chuyên ngành)
   - A-Z terms
   - Viết tắt thường gặp
   - Emoji guide

### Instructions File
6. **INSTRUCTIONS.md** (Paste vào Instructions của GPT)
   - Core logic
   - Workflow
   - Templates
   - Rules

---

## 🚀 Cách Setup ChatGPT Custom GPT

### Bước 1: Tạo Custom GPT
1. Vào ChatGPT → Explore GPTs → Create
2. Đặt tên: "Chuyên gia Phân tích Chứng khoán VN"
3. Description: "AI Agent phân tích kỹ thuật chứng khoán Việt Nam"

### Bước 2: Configure

#### Instructions
- Mở file `INSTRUCTIONS.md`
- Copy **toàn bộ nội dung**
- Paste vào phần "Instructions"

#### Knowledge
- Click "Upload files"
- Chọn tất cả 5 files `.md` (trừ INSTRUCTIONS.md)
- Upload

#### Capabilities
☑️ Web Browsing (Bắt buộc)
☑️ Code Interpreter
☐ DALL·E (Không cần)

#### Conversation Starters
```
- "Phân tích kỹ thuật VCB cho tôi"
- "So sánh VCB, CTG, BID - mã nào tốt hơn?"
- "Giải thích cách đọc Ichimoku Cloud"
- "Tôi mua ở 85k, giờ về 80k, nên làm gì?"
```

### Bước 3: Test
Test với các cases:
1. Uptrend analysis
2. Downtrend với hướng dẫn chờ
3. User hỏi không có data
4. User đã lỗ

---

## 📊 Cấu trúc Files

```
knowledge_base_files/
├── kb_technical.md        (Phương pháp phân tích)
├── kb_vietnam_market.md   (Đặc thù VN)
├── kb_formulas.md         (Công thức)
├── kb_examples.md         (Ví dụ mẫu)
├── kb_glossary.md         (Thuật ngữ)
├── INSTRUCTIONS.md        (Instructions cho GPT)
└── README.md              (File này)
```

---

## 🔧 Maintenance

### Khi cần update:
1. Sửa file tương ứng
2. Re-upload vào ChatGPT Knowledge
3. GPT sẽ tự động dùng version mới

### Version control:
- Mỗi file có changelog ở cuối
- Ghi rõ ngày update và nội dung thay đổi

---

## ⚠️ Lưu ý quan trọng

1. **Instructions <8000 từ**: OK, đã tối ưu
2. **Knowledge files**: Không giới hạn
3. **Cite sources**: Luôn cite "kb_technical.md Section X.X"
4. **Disclaimer**: LUÔN LUÔN có ở cuối mỗi phân tích
5. **DYOR**: Nhắc user tự nghiên cứu

---

## 📝 Changelog

**v2.0 - 07/11/2024**
- Tách thành 5 files modules
- Thêm Instructions tối ưu
- Bổ sung ICT, Wyckoff chi tiết
- Đầy đủ ví dụ và glossary

**v1.0 - Original**
- Knowledge Base đơn file

---

## 📞 Support

Nếu gặp vấn đề:
1. Check Instructions đã paste đầy đủ chưa
2. Verify 5 files KB đã upload hết
3. Test với examples trong kb_examples.md
4. Đảm bảo Web Browsing đã bật

---

## 🎯 Tips tối ưu

1. **Update định kỳ**:
   - Thêm examples mới vào kb_examples.md
   - Update vĩ mô VN trong kb_vietnam_market.md

2. **Custom cho nhu cầu riêng**:
   - Thêm sector-specific analysis
   - Thêm strategies cá nhân vào kb_technical.md

3. **Feedback loop**:
   - Ghi lại phân tích sai
   - Cải thiện methodology

---

Created with ❤️ for Vietnamese Stock Traders
"""
    
    filepath = output_dir / "README.md"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(readme)
    print(f"✅ Đã tạo: {filepath}")

def main():
    """Main function"""
    print("🚀 Bắt đầu tạo Knowledge Base files...\n")
    
    # Tạo thư mục
    output_dir = create_output_dir()
    print(f"📁 Thư mục: {output_dir}\n")
    
    # Tạo các files
    save_files(output_dir)
    create_instructions_file(output_dir)
    create_readme(output_dir)
    
    print("\n✅ HOÀN THÀNH!")
    print(f"\n📂 Tất cả files đã được tạo trong: {output_dir}")
    print("\n📖 Đọc README.md để biết cách setup ChatGPT!")
    print("\n🎯 Next steps:")
    print("   1. Copy nội dung các artifacts vào files .md tương ứng")
    print("   2. Upload 5 files KB vào ChatGPT Knowledge")
    print("   3. Copy INSTRUCTIONS.md vào Instructions")
    print("   4. Test!")

if __name__ == "__main__":
    main()
