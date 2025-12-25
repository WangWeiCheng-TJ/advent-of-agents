import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. 載入環境變數 (讀取你的 .env 檔)
load_dotenv()

# 2. 設定 API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ 找不到 API Key，請檢查 .env 檔案")
    exit()

genai.configure(api_key=api_key)

# 3. 建立模型 (這是 Agent 的大腦)
model = genai.GenerativeModel("models/gemma-3-27b") 
# https://aistudio.google.com/usage?timeRange=last-28-days&project=gen-lang-client-0799236729&tab=rate-limit
# testing: gemma-3-27b - 1b 2b 4b 12b 27b
# smarter: gemini-2.5-flash-lite 

# 4. 測試對話
print("🤖 Agent 啟動中...")
response = model.generate_content("你好！請用一句話形容什麼是 AI Agent？")

print("-" * 30)
print(f"Gemini 回答：\n{response.text}")
print("-" * 30)