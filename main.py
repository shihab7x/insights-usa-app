from kivy.app import App
from kivy.uix.browser import WebView # For some versions
from kivy.webbrowser import open as open_url
from kivy.uix.boxlayout import BoxLayout
import webbrowser

# আমরা সরাসরি আপনার ওয়েবসাইটটি লোড করব
class InsightsApp(App):
    def build(self):
        # এটি রান করলে সরাসরি ব্রাউজারে আপনার সাইট ওপেন হবে 
        # অথবা একটি WebView এর মাধ্যমে অ্যাপের ভেতরেই দেখাবে
        webbrowser.open("https://insightsofusa.blogspot.com/")
        return BoxLayout()

if __name__ == "__main__":
    InsightsApp().run()
