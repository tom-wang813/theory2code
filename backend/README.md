# Paper2Code Backend

歡迎使用 Paper2Code 後端系統。這是一個基於 Python 和 Microsoft AutoGen 框架的 AI 多代理（Multi-Agent）系統，旨在將學術論文中的新理論和方法自動轉化為可執行的程式碼，特別適用於將前沿研究應用到特定領域（如生物信息學等）。

## ✨ 功能特性 (Features)

- **智能論文解析**: 自動分析學術論文，提取核心理論、數學公式和算法邏輯
- **領域適配**: 評估論文理論在目標應用領域的適用性，提供領域特定的調整建議
- **算法設計**: 將抽象理論轉化為具體可實現的算法架構
- **程式碼實現**: 根據算法設計自動生成高質量的程式碼實現
- **智能驗證**: 自動設計測試案例，驗證實現的正確性和性能
- **異步任務處理**: 通過 RESTful API 接收任務，並在背景異步執行，適合處理複雜的論文轉換任務
- **模組化架構**: 清晰的目錄結構，將代理、工具、工作流和 API 服務解耦，易於維護和擴展

## 🏗️ 專案架構 (Project Architecture)

```
backend/
├── agents/
│   ├── __init__.py
│   ├── paper_analyst.py      # Paper Analyst 配置：prompt、tools、參數
│   ├── domain_expert.py      # Domain Expert 配置：prompt、tools、參數
│   ├── algorithm_designer.py # Algorithm Designer 配置：prompt、tools、參數  
│   ├── implementation_engineer.py # Implementation Engineer 配置：prompt、tools、參數
│   └── validation_specialist.py   # Validation Specialist 配置：prompt、tools、參數
├── tools/
│   ├── __init__.py
│   ├── file_ops.py          # 文件和文件夾操作
│   ├── code_runner.py       # 程式碼執行和測試
│   └── pdf_parser.py        # PDF 解析（可選）
├── workflows/
│   ├── __init__.py
│   └── paper2code_workflow.py # 定義和編排代理之間的協作流程
├── config/
│   ├── __init__.py
│   └── llm_config.py        # LLM 相關配置（API Keys、模型設定）
├── workspace/
│   └── .gitkeep             # 每個任務的獨立工作目錄，用於存放生成的檔案
├── .env                     # 存儲環境變數，如 API Keys (不應提交到 Git)
├── app.py                   # Flask 應用主入口，提供 API 接口
├── requirements.txt         # Python 依賴套件列表
└── README.md                # 專案說明文件
```

## 🤖 代理系統 (Agent System)

本系統採用去中心化的多代理架構，每個代理都有明確的職責分工：

### 1. **Paper Analyst Agent (論文分析師)**
- **職責**: 理解和解析論文內容
- **具體工作**:
  - 提取論文的核心理論和方法
  - 識別關鍵的數學公式和算法
  - 理解論文的創新點和適用場景
  - 分析實驗設計和評估方法

### 2. **Domain Expert Agent (領域專家)**
- **職責**: 橋接理論與應用領域
- **具體工作**:
  - 評估論文理論在目標領域的適用性
  - 識別需要調整或適配的部分
  - 提出領域特定的約束和要求
  - 建議合適的數據格式和處理流程

### 3. **Algorithm Designer Agent (算法設計師)**
- **職責**: 將理論轉化為可實現的算法
- **具體工作**:
  - 將數學公式轉換為程式邏輯
  - 設計算法的整體架構
  - 考慮計算複雜度和優化方案
  - 處理理論與實際實現之間的差距

### 4. **Implementation Engineer Agent (實作工程師)**
- **職責**: 具體的程式碼實現
- **具體工作**:
  - 根據算法設計編寫程式碼
  - 選擇合適的工具庫和框架
  - 處理數據 I/O 和格式轉換
  - 實現性能優化

### 5. **Validation Specialist Agent (驗證專家)**
- **職責**: 確保實現的正確性
- **具體工作**:
  - 設計測試案例來驗證算法正確性
  - 對比論文中的實驗結果
  - 進行邊界條件和異常情況測試
  - 評估在目標領域數據上的表現

## 🔄 工作流程 (Workflow)

1. **Paper Analyst** 深度解析論文，提取核心理論和方法
2. **Domain Expert** 評估理論在特定領域的適用性
3. **Algorithm Designer** 設計具體的實現方案
4. **Implementation Engineer** 編寫程式碼實現
5. **Validation Specialist** 驗證和測試實現結果

代理之間通過去中心化的對話機制協作，同時共享統一的工作空間和文件系統。

## 🚀 開始使用 (Getting Started)

### 1. 環境準備

- Python 3.9+
- `pip` 和 `venv`

### 2. 安裝步驟

1.  **Clone 專案**
    ```bash
    git clone <your-repo-url>
    cd paper2code/backend
    ```

2.  **建立並啟用虛擬環境**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # Windows 使用: venv\Scripts\activate
    ```

3.  **安裝依賴套件**
    ```bash
    pip install -r requirements.txt
    ```

4.  **設定環境變數**
    複製 `.env.example` (如果有的話) 或手動建立一個 `.env` 檔案，並填入必要的 API Key。
    ```
    # .env
    OPENROUTER_API_KEY="sk-or-v1-..."
    ```

5.  **啟動應用**
    ```bash
    flask run
    # 或者
    python app.py
    ```
    服務將會運行在 `http://127.0.0.1:5000`。

## ⚙️ 工作流程說明 (How It Works)

1.  **論文提交**: 使用者通過 `POST /api/v1/papers` API 提交一篇學術論文（PDF 或文本格式）以及目標應用領域。

2.  **論文分析**: `Paper Analyst Agent` 首先介入，深度解析論文內容，提取核心理論、數學公式和算法邏輯。

3.  **領域適配**: `Domain Expert Agent` 評估論文理論在目標領域的適用性，識別需要調整的部分，提出領域特定的要求。

4.  **算法設計**: `Algorithm Designer Agent` 根據論文理論和領域要求，設計具體可實現的算法架構。

5.  **程式碼實現**: `Implementation Engineer Agent` 根據算法設計編寫高質量的程式碼，選擇合適的工具庫和框架。

6.  **驗證測試**: `Validation Specialist Agent` 設計測試案例，驗證實現的正確性，並與論文結果進行比較。

7.  **迭代優化**: 各代理之間會根據需要進行多輪協作，直到得到滿意的實現結果。

## 🔌 API 端點 (API Endpoints)

-   **`POST /api/v1/papers`**: 提交新的論文轉換任務。
    -   **Request Body**: `{"paper": "paper content or file", "domain": "target domain", "requirements": "specific requirements"}`
    -   **Success Response**: `{"task_id": "...", "status": "pending"}`

-   **`GET /api/v1/tasks/<task_id>/status`**: 查詢特定任務的狀態和進度。
    -   **Success Response**: `{"task_id": "...", "status": "analyzing|designing|implementing|validating|completed|failed", "current_agent": "...", "progress": "..."}`

-   **`GET /api/v1/tasks/<task_id>/result`**: 獲取任務完成後的結果（包括程式碼、文檔、測試結果等）。
    -   **Success Response**: `{"code_files": [...], "documentation": "...", "test_results": {...}, "workspace_path": "..."}`

-   **`GET /api/v1/tasks/<task_id>/history`**: 獲取任務執行過程中代理之間的對話歷史。
    -   **Success Response**: `{"messages": [...], "agent_interactions": [...]}`

## 🎯 使用案例 (Use Cases)

### 生物信息學應用
```json
{
  "paper": "關於新型蛋白質摺疊預測算法的論文內容",
  "domain": "bioinformatics",
  "requirements": "需要支援 PDB 格式，與現有的 AlphaFold 結果進行比較"
}
```

### 機器學習算法
```json
{
  "paper": "新的深度學習優化算法論文",
  "domain": "computer_vision", 
  "requirements": "實現 PyTorch 版本，在 ImageNet 數據集上進行驗證"
}
```

## 🚧 開發計劃 (Development Roadmap)

### Phase 1: 基礎架構 (Current)
- [x] 專案架構設計
- [ ] 基礎工具實現 (`tools/shared/`)
- [ ] Paper Analyst Agent 配置和基本功能
- [ ] 簡單的 API 端點

### Phase 2: 核心功能
- [ ] 完整的 5 個代理實現
- [ ] PDF 解析和公式提取工具
- [ ] 基本的代理協作工作流
- [ ] 任務狀態管理

### Phase 3: 高級功能
- [ ] 領域知識庫集成
- [ ] 程式碼執行和測試環境
- [ ] 結果可視化和報告生成
- [ ] 性能優化和錯誤處理

### Phase 4: 擴展功能
- [ ] 多語言程式碼生成支援
## 📚 相關資源 (Resources)

- [Microsoft AutoGen 文檔](https://microsoft.github.io/autogen/)
- [OpenRouter API 文檔](https://openrouter.ai/docs)
- [Flask 文檔](https://flask.palletsprojects.com/)

## 🤝 貢獻 (Contributing)

歡迎提交 Issue 和 Pull Request！請確保：
1. 遵循現有的程式碼風格
2. 為新功能添加適當的測試
3. 更新相關文檔

## � 授權 (License)

本專案採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 檔案。

---

*Paper2Code - 讓學術理論與實際應用無縫接軌*

### 2. 安裝步驟

1.  **Clone 專案**
    ```bash
    git clone <your-repo-url>
    cd matagent/backend
    ```

2.  **建立並啟用虛擬環境**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # Windows 使用: venv\Scripts\activate
    ```

3.  **安裝依賴套件**
    ```bash
    pip install -r requirements.txt
    ```

4.  **設定環境變數**
    複製 `.env.example` (如果有的話) 或手動建立一個 `.env` 檔案，並填入必要的 API Key。
    ```
    # .env
    OPENROUTER_API_KEY="sk-or-v1-..."
    ```

5.  **啟動應用**
    ```bash
    flask run
    # 或者
    python app.py
    ```
    服務將會運行在 `http://127.0.0.1:5000`。

## ⚙️ 工作流程說明 (How It Works)

1.  **任務提交**: 使用者通過 `POST /api/v1/tasks` API 提交一個開發需求（例如："幫我寫一個 FastAPI 的 Hello World 應用"）。
2.  **規劃階段**: API 服務啟動一個代理群組對話。`Planner_Agent` 首先介入，將使用者需求分解成一份詳細、可執行的步驟清單。
3.  **開發階段**: `Engineer_Agent` 根據 `Planner_Agent` 的計畫，開始編寫程式碼。它會使用 `file_tools` 將程式碼寫入到該任務專屬的 `workspace/{task_id}` 目錄下。
4.  **審查階段**: `Critic_Agent` 在 `Engineer_Agent` 完成程式碼後自動介入，對程式碼進行審查。如果發現問題，它會提出修改建議。
5.  **迭代循環**: 流程將在 `Engineer_Agent` 和 `Critic_Agent` 之間循環，直到程式碼通過審查。
6.  **任務完成**: 當所有計畫步驟都完成後，工作流結束。使用者可以通過其他 API 端點獲取最終的產出結果。

## 🔌 API 端點 (API Endpoints)

-   **`POST /api/v1/tasks`**: 創建一個新的異步開發任務。
    -   **Request Body**: `{"task": "your task description"}`
    -   **Success Response**: `{"task_id": "...", "status": "pending"}`

-   **`GET /api/v1/tasks/<task_id>/status`**: 查詢特定任務的狀態和進度。
    -   **Success Response**: `{"task_id": "...", "status": "running|completed|failed", "history": [...]}`

-   **`GET /api/v1/tasks/<task_id>/result`**: 獲取任務完成後的結果（例如，生成的檔案列表或打包的 zip 檔案）。
    -   **Success Response**: `{"files": ["path/to/file1.py", ...], "workspace_path": "..."}