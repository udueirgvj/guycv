import os

# التحقق من وجود المتغير السري لجلسة العمل
session_data = os.getenv("SESSION_DATA")

print("--- Python Bot Executing via GitHub Actions ---")

if session_data:
  print("Success: SESSION_DATA was loaded securely!")
  # ضع كود التشغيل أو الأتمتة الخاص بك هنا لاحقاً
else:
  print("Notice: SESSION_DATA is empty or not configured yet.")

