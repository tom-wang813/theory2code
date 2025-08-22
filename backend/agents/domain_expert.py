"""
Domain Expert Agent Configuration

負責橋接理論與應用領域，評估論文理論在目標領域的適用性
"""

AGENT_CONFIG = {
    "name": "Domain_Expert", 
    "system_message": """你是一位跨領域的專業領域專家，具備深厚的理論基礎和豐富的實際應用經驗。

你的主要職責：
1. **領域適配評估**：
   - 分析論文理論在目標應用領域的適用性
   - 識別理論與實際應用之間的差距
   - 評估方法在特定領域的可行性和實用性
   - 考慮領域特有的約束和限制

2. **技術轉化建議**：
   - 提出將抽象理論適配到具體領域的方案
   - 建議必要的調整、修改或簡化
   - 識別需要額外考慮的領域特定因素
   - 推薦合適的工具、庫和技術棧

3. **數據和格式規範**：
   - 定義輸入數據的格式和預處理需求
   - 建議輸出結果的表示方式
   - 考慮與現有系統的整合需求
   - 提出數據品質和驗證標準

4. **實用性評估**：
   - 評估實現的技術難度和開發成本
   - 考慮性能需求和資源限制
   - 分析維護和擴展的可行性
   - 提出風險評估和應對策略

專業領域包括但不限於：
- 生物信息學 (Bioinformatics)
- 計算機視覺 (Computer Vision)  
- 自然語言處理 (NLP)
- 機器學習 (Machine Learning)
- 數據科學 (Data Science)
- 金融科技 (FinTech)
- 醫療健康 (Healthcare)

請基於具體的目標領域提供專業建議，用繁體中文回應。""",
    
    "llm_config": {
        "model": "anthropic/claude-3-sonnet",
        "temperature": 0.2,  # 稍高溫度允許創造性的適配建議
        "max_tokens": 3500
    },
    
    "tools": [
        # Domain Expert 專用工具：讀取分析結果、保存適配建議
        "read_file",
        "save_analysis_result",
    ],
    
    "description": "負責評估論文理論在特定領域的適用性，提供領域適配建議的專業領域專家代理"
}

# 領域專業知識庫 - 預定義的常見領域特徵
DOMAIN_KNOWLEDGE = {
    "bioinformatics": {
        "common_data_formats": ["FASTA", "PDB", "VCF", "SAM/BAM", "GFF/GTF"],
        "standard_tools": ["BioPython", "BLAST", "HMMER", "PyMOL", "RDKit"],
        "performance_requirements": ["高記憶體使用", "大數據處理", "並行計算"],
        "validation_standards": ["統計顯著性", "生物學意義", "實驗驗證"],
        "common_challenges": ["數據異質性", "噪音處理", "可解釋性"]
    },
    "computer_vision": {
        "common_data_formats": ["JPEG", "PNG", "COCO", "Pascal VOC", "ImageNet"],
        "standard_tools": ["OpenCV", "PIL", "scikit-image", "TensorFlow", "PyTorch"],
        "performance_requirements": ["實時處理", "GPU 加速", "記憶體效率"],
        "validation_standards": ["mAP", "IoU", "F1-score", "視覺品質評估"],
        "common_challenges": ["光照變化", "尺度變化", "遮擋處理"]
    },
    "nlp": {
        "common_data_formats": ["Text", "JSON", "XML", "CoNLL", "CSV"],
        "standard_tools": ["NLTK", "spaCy", "Transformers", "Gensim", "jieba"],
        "performance_requirements": ["語言模型大小", "推理速度", "多語言支援"],
        "validation_standards": ["BLEU", "ROUGE", "BERTScore", "人工評估"],
        "common_challenges": ["語言多樣性", "語義理解", "上下文處理"]
    },
    "machine_learning": {
        "common_data_formats": ["CSV", "JSON", "Parquet", "HDF5", "NumPy"],
        "standard_tools": ["scikit-learn", "pandas", "NumPy", "XGBoost", "LightGBM"],
        "performance_requirements": ["訓練時間", "模型大小", "推理延遲"],
        "validation_standards": ["交叉驗證", "A/B 測試", "統計檢驗"],
        "common_challenges": ["特徵工程", "模型解釋", "數據漂移"]
    }
}

# 適配分析輸出模板
ADAPTATION_TEMPLATE = """
# 領域適配分析報告

## 1. 目標領域概況
- **領域名稱**: [目標應用領域]
- **領域特徵**: [該領域的核心特點]
- **技術成熟度**: [領域的技術發展水平]

## 2. 適用性評估
### 2.1 理論適配度
- **適用程度**: [高/中/低]
- **適用原因**: [為什麼該理論適合這個領域]
- **潛在價值**: [能帶來什麼改進或創新]

### 2.2 技術可行性
- **實現難度**: [簡單/中等/困難]
- **所需資源**: [計算、數據、人力資源需求]
- **預期開發時間**: [預估的實現時間]

## 3. 適配建議
### 3.1 理論調整
- [需要對原理論進行的修改或簡化]

### 3.2 技術棧建議
- **推薦語言**: [Python/R/Java/C++ 等]
- **核心庫**: [具體的第三方庫]
- **開發框架**: [如果需要的話]

### 3.3 數據處理
- **輸入格式**: [標準的輸入數據格式]
- **預處理步驟**: [必要的數據清理和轉換]
- **輸出格式**: [結果的標準表示方式]

## 4. 領域特定考量
### 4.1 性能要求
- [速度、準確性、穩定性等要求]

### 4.2 合規性
- [法規、標準、倫理等考量]

### 4.3 整合需求
- [與現有系統的整合方式]

## 5. 風險評估
### 5.1 技術風險
- [實現過程中可能遇到的技術挑戰]

### 5.2 應用風險
- [在實際應用中的潛在問題]

### 5.3 風險應對
- [建議的風險緩解策略]

## 6. 驗證策略
### 6.1 評估指標
- [領域特定的評估標準]

### 6.2 測試數據
- [建議的測試數據集或收集方式]

### 6.3 基準對比
- [與現有方法的比較標準]

## 7. 實施路線圖
1. [第一階段：基礎實現]
2. [第二階段：領域優化] 
3. [第三階段：驗證測試]
4. [第四階段：部署整合]
"""
