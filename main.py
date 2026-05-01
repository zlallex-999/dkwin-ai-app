from kivymd.app import MDApp
from kivy.lang import Builder
import random
from ai_engine import AIEngine

KV = open("ui.kv").read()

class App(MDApp):
    def build(self):
        self.engine = AIEngine()
        return Builder.load_string(KV)

    def add_fake(self):
        num = random.randint(0,9)
        self.engine.add_result(num)

        pred, conf, s, b = self.engine.predict()

        self.root.ids.pred.text = f"PRED: {pred}"
        self.root.ids.conf.text = f"CONF: {conf}%"
        self.root.ids.nums.text = f"S:{s} B:{b}"

if __name__ == "__main__":
    App().run()
