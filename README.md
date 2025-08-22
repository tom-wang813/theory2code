# Paper2Code - AI Multi-Agent System

> 🚀 讓 AI 幫你把學術論文變成可執行程式碼！

Paper2Code 是一個基於 Microsoft AutoGen 的 AI 多代理系統，能夠將學術論文自動轉換為可執行的程式碼實現。

## 🎯 系統特色

- **5 個專業 AI 代理**: 涵蓋從論文分析到程式碼驗證的完整流程
- **AutoGen 框架**: 使用 Microsoft AutoGen 進行代理間協作
- **OpenRouter 整合**: 支援多種頂級 LLM 模型 (Claude-3, GPT-4, Gemini 等)
- **簡潔架構**: 專注核心功能，避免過度複雜的設計

## 🤖 AI 代理團隊

| 代理 | 職責 | 輸出 |
|------|------|------|
| 📚 **Paper Analyst** | 深度分析學術論文，提取核心理論 | 結構化分析報告 |
| 🎯 **Domain Expert** | 評估理論適用性，提供領域建議 | 領域適配方案 |
| 🔧 **Algorithm Designer** | 設計可實現的算法架構 | 詳細設計文檔 |
| 💻 **Implementation Engineer** | 編寫高質量程式碼實現 | 完整可執行程式 |
| ✅ **Validation Specialist** | 設計測試並驗證正確性 | 全面測試報告 |

## 🛠️ 技術架構

```
paper2code/
├── backend/           # 後端 AI 代理系統
│   ├── agents/       # 5 個專業代理配置
│   ├── tools/        # 核心工具系統
│   ├── config.py     # 系統配置
│   └── example_usage.py  # 使用範例
└── tests/            # 測試套件
```

## 🚀 快速開始

### 1. 克隆倉庫
```bash
git clone git@github.com:tom-wang813/paper2code.git
cd paper2code
```

### 2. 安裝依賴
```bash
cd backend
pip install -r requirements.txt
```

### 3. 配置 API Key
```bash
cp .env.example .env
# 編輯 .env 設置你的 OPENROUTER_API_KEY
```

### 4. 測試系統
```bash
python test_system.py
```

### 5. 運行範例
```bash
python example_usage.py
```

## 📚 使用方式

### 簡單使用
```python
from agents import create_agent_team

# 創建 AI 代理團隊
team = create_agent_team()

# 分析論文
paper_analyst = team["paper_analyst"]
analysis = paper_analyst.generate_reply(
    messages=[{"content": "請分析這篇深度學習論文...", "role": "user"}]
)
```

### 完整工作流程
```python
from example_usage import run_paper_to_code_workflow

# 執行完整的論文→程式碼轉換
results = run_paper_to_code_workflow(paper_content)
```

## 🔄 工作流程

```mermaid
graph LR
    A[📄 論文輸入] --> B[📚 Paper Analyst]
    B --> C[🎯 Domain Expert]
    C --> D[🔧 Algorithm Designer]
    D --> E[💻 Implementation Engineer]
    E --> F[✅ Validation Specialist]
    F --> G[🎉 可執行程式碼]
```

1. **論文分析**: 提取核心理論和算法
2. **領域評估**: 評估適用性和提供專業建議
3. **算法設計**: 設計可實現的架構
4. **程式實現**: 編寫高質量程式碼
5. **驗證測試**: 全面測試和驗證

## 📋 支援的 AI 模型

透過 [OpenRouter](https://openrouter.ai/)，系統支援：

- 🧠 **Anthropic**: Claude-3 (Sonnet, Opus, Haiku)
- 🤖 **OpenAI**: GPT-4 (Turbo, Vision, Omni)
- 🔍 **Google**: Gemini Pro/Ultra
- ⚡ **其他**: Mistral, Llama, Qwen 等 50+ 模型

## 🎯 應用場景

- 📊 **研究加速**: 快速將論文想法轉為原型
- 🎓 **教育輔助**: 幫助學生理解算法實現
- 💡 **創新探索**: 探索論文的實際應用潛力
- 🔬 **科研複現**: 協助複現論文實驗

## 📝 詳細文檔

- [後端系統文檔](./backend/README_new.md)
- [代理配置指南](./backend/agents/)
- [工具系統說明](./backend/tools/)

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📄 授權

MIT License

---

**讓 AI 成為你的研究夥伴，將論文變成程式碼！** 🚀
