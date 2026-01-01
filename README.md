# Advent of Agents 

這是一個基於 Python 與 Google GenAI SDK (v1.0) 開發的 AI Agent 系統。包含職缺搜尋、自動爬蟲與履歷分析功能。

## 功能特色
- **Job Hunter**: 自動搜尋 DuckDuckGo 並結合 User Profile 進行職缺分析。
- **Profile Builder**: 爬取個人網站並使用gemini生成履歷摘要，。
- **Pipeline**: 採用 `Input -> Search -> Analyze` 三階段設計。

## 快速開始
1. 安裝依賴: `uv sync`
2. 設定 `.env` (設定`MODEL_NAME`與`GOOGLE_API_KEY`)
3. 執行: `uv run main.py`

## Development Roadmap

### Core Infrastructure
- [x] **環境建置**: 使用 `uv` 進行套件管理，Python 3.12+ 環境。
- [x] **SDK 升級**: 整合 Google GenAI SDK v1.0 (`google-genai`)。
- [x] **配置管理**: 實作 `config.py` 與 `.env`，分離敏感資料與程式邏輯。
- [x] **模組化設計**: 建立 `Main Dispatcher` 模式，統一由 `main.py` 調度不同 Agent。

### Agent: Job Hunter
- [x] **工具整合**: 串接 DuckDuckGo Search (無須 API Key for search)。
- [x] **流程設計**: 實作 `Input` -> `Keywords` -> `Search` -> `Analyze` 的三階段 Pipeline。
- [x] **個人化分析**: 支援讀取使用者 `profile.md` 進行精準職缺媒合。
- [x] **防呆機制**: 針對 Gemma/Gemini 不同模型自動切換 Prompt 策略。

### Agent: Profile Builder
- [x] **網頁爬蟲**: 使用 `requests` + `BeautifulSoup` 抓取個人網站。
- [x] **智慧爬取**: 實作 `Recursive Crawling` (遞迴爬取)，自動抓取網站內的子分頁。
- [] **LinkedIn支援**: To Do
- [x] **自動摘要**: Call Gemini api 整理爬下來的資訊為 Markdown 履歷。

### 未來規劃 (To-Do)
- [ ] **Web UI**: 預計整合 Streamlit 或 Chainlit 建立網頁介面。
- [ ] **Interview Agent**: 新增模擬面試官，針對 JD 進行對答練習。
- [ ] **資料庫整合**: 將搜尋過的職缺存入 SQLite 以避免重複搜尋。
---

<details>
<summary><b>開發日誌 & 技術決策 (點擊展開)</b></summary>

#### LinkedIn 爬蟲的失敗與轉折 26.01.01
- **挑戰**: 嘗試爬取 LinkedIn Profile 時遭遇 `Status 999` 錯誤。
- **原因**: 觸發了 LinkedIn 的 Anti-bot 機制 (User-Agent/JS Check)。
- **解決方案**: 轉而支援 **本地檔案讀取模式**，並建議使用者改用 GitHub Profile 或個人網站作為資料源。這讓我學到了在 Agent 設計中，「備案 (Fallback)」的重要性。

#### 從 Script 到 Module 25.12.xx
將原本散落在各處的 `.py` 檔重構為 `agents/` 套件架構，並引入 `config.py` 統一管理 `Gemini 2.0` 模型參數，解決了跨檔案 import 的路徑問題。

#### SDK 遷移 25.12.xx
棄用 `google.generativeai`，全面升級至 `google-genai` v1.0，以支援更現代的 Tool Config 寫法。

</details>