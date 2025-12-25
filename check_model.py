import os
import google.generativeai as genai
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print(f"{'模型名稱 (Model Name)':<40} | {'顯示名稱 (Display Name)':<30}")
print("-" * 80)

try:
    for m in genai.list_models():
        # 我們只列出可以「對話/生成文字」的模型
        if 'generateContent' in m.supported_generation_methods:
            print(f"{m.name:<40} | {m.display_name:<30}")
except Exception as e:
    print(f"查詢失敗: {e}")