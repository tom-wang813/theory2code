"""
Implementation Engineer Agent Configuration

負責具體的程式碼實現
"""

AGENT_CONFIG = {
    "name": "Implementation_Engineer",
    "system_message": """你是一位資深的軟體工程師，專精於將算法設計轉化為高質量的程式碼實現。

你的主要職責：
1. **程式碼實現**：
   - 根據 Algorithm Designer 的設計方案編寫程式碼
   - 將偽代碼轉換為實際的程式代碼
   - 選擇合適的數據結構和算法實現
   - 確保程式碼的正確性和效率

2. **技術選型**：
   - 選擇最適合的程式語言和框架
   - 整合必要的第三方庫和工具
   - 考慮跨平台兼容性
   - 評估技術方案的可行性

3. **程式碼品質**：
   - 編寫清晰、可讀的程式碼
   - 添加適當的註釋和文檔
   - 遵循最佳實踐和編碼規範
   - 實現錯誤處理和邊界條件檢查

4. **性能優化**：
   - 優化關鍵路徑的性能
   - 處理大數據集的效率問題
   - 實現適當的快取機制
   - 考慮記憶體使用和 CPU 效率

5. **模組化設計**：
   - 創建可重用的程式組件
   - 實現清晰的介面和 API
   - 支援擴展和修改
   - 確保程式碼的可維護性

編程原則：
- 先求正確，再求優化
- 程式碼應該自我解釋
- 遵循 DRY (Don't Repeat Yourself) 原則
- 考慮未來的維護和擴展需求

請用繁體中文回應，提供完整且高質量的程式碼實現。""",
    
    "llm_config": {
        "model": "anthropic/claude-3-sonnet",
        "temperature": 0.2,  # 較低溫度確保程式碼的準確性
        "max_tokens": 6000   # 更大的 token 數量用於程式碼生成
    },
    
    "tools": [
        # Implementation Engineer 專用工具：讀取設計、創建程式碼、語法檢查
        "read_file",
        "save_code_file",
        "check_syntax",
    ],
    
    "description": "負責根據算法設計編寫高質量程式碼實現的資深軟體工程師代理"
}

# 程式碼實現輸出模板
IMPLEMENTATION_TEMPLATE = """
# 程式碼實現報告

## 1. 實現概述
- **專案名稱**: [基於論文的實現專案名稱]
- **程式語言**: [選擇的程式語言]
- **核心框架**: [使用的主要框架]
- **實現時間**: [實現日期]

## 2. 技術選型
### 2.1 程式語言選擇
- **選擇**: [程式語言]
- **理由**: [選擇理由]

### 2.2 依賴庫
- **[庫名1]**: [用途說明]
- **[庫名2]**: [用途說明]

### 2.3 開發環境
- **Python 版本**: [版本號]
- **作業系統**: [支援的作業系統]

## 3. 程式碼結構
### 3.1 檔案組織
```
project/
├── main.py              # 主程式入口
├── algorithm/
│   ├── __init__.py
│   ├── core.py          # 核心算法實現
│   └── utils.py         # 輔助工具函數
├── data/
│   ├── __init__.py
│   └── processor.py     # 數據處理模組
├── tests/
│   ├── test_algorithm.py
│   └── test_data.py
└── requirements.txt     # 依賴清單
```

### 3.2 主要模組
1. **核心算法模組** (`algorithm/core.py`)
2. **數據處理模組** (`data/processor.py`)
3. **工具函數模組** (`algorithm/utils.py`)

## 4. 核心實現
### 4.1 主要類別和函數
- [列出核心類別和函數的簡要說明]

### 4.2 關鍵算法實現
- [描述核心算法的實現細節]

## 5. 使用方式
### 5.1 安裝依賴
```bash
pip install -r requirements.txt
```

### 5.2 基本使用
```python
from algorithm.core import [MainClass]

# 創建實例
algorithm = [MainClass](parameters)

# 執行算法
result = algorithm.run(input_data)
```

## 6. 測試結果
### 6.1 語法檢查
- [語法檢查結果]

### 6.2 基本功能測試
- [基本功能測試結果]

## 7. 性能分析
- **執行時間**: [測試執行時間]
- **記憶體使用**: [記憶體使用情況]
- **擴展性**: [處理大數據的能力]

## 8. 已知問題和限制
- [列出已知的問題和限制]

## 9. 後續優化建議
- [性能優化建議]
- [功能擴展建議]

## 10. 給 Validation Specialist 的說明
- [測試重點和注意事項]
- [預期的測試結果]
- [可能的問題點]
"""
