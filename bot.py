import time
from supabase import create_client

# وضع الرابط والمفتاح مباشرة هنا لتجنب مشاكل Secrets
SUPABASE_URL = "https://fmlwcghmqhlgppaxuwdu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZtbHdjZ2htcWhsZ3BwYXh1d2R1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk1MjE3NjYsImV4cCI6MjA5NTA5Nzc2Nn0.D2Zsf-paXX_pI0EWyoaZGkDO0pwmNAqV5Weh2mCvSno"

# إنشاء اتصال مع Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_and_execute_tasks():
    print("🔄 جاري الاتصال بقاعدة البيانات لجلب المهام...")
    
    try:
        # جلب المهام التي حالتها قيد الانتظار (pending) من جدول tasks
        response = supabase.table("tasks").select("*").eq("status", "pending").execute()
        tasks = response.data
        
        if not tasks:
            print("📭 لا توجد مهام جديدة قيد الانتظار حالياً.")
            return

        for task in tasks:
            task_id = task.get("id")
            task_type = task.get("task_type") # مثل like أو follow
            target_url = task.get("target_url")
            
            print(f"🚀 بدء تنفيذ المهمة [{task_type}] للرابط: {target_url}")
            
            # --- هنا يتم تنفيذ عملية الأتمتة لاحقاً ---
            time.sleep(3) 
            
            # تحديث حالة المهمة في Supabase إلى مكتملة (completed)
            supabase.table("tasks").update({"status": "completed"}).eq("id", task_id).execute()
            print(f"✅ تمت المهمة بنجاح وتحديث حالتها في Supabase.")
            
    except Exception as e:
        print(f"❌ حدث خطأ أثناء تنفيذ المهام: {str(e)}")

if __name__ == "__main__":
    fetch_and_execute_tasks()
