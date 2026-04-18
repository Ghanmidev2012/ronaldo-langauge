import sys
import os

class RonaldoInterpreter:
    def __init__(self):
        self.memory = [0] * 300  # شريط الذاكرة (ملعب المباراة)
        self.pointer = 0         # مكان اللاعب الحالي
        self.commands = {
            "SU!": self.goal,        # +1
            "suu..": self.foul,      # -1
            "sUu": self.run_right,   # Move Right
            "UuS": self.run_left,    # Move Left
            "SUUUU": self.celebrate  # Print Char
        }

    def goal(self): self.memory[self.pointer] += 1
    def foul(self): self.memory[self.pointer] -= 1
    def run_right(self): self.pointer += 1
    def run_left(self): self.pointer -= 1
    def celebrate(self): print(chr(self.memory[self.pointer]), end="", flush=True)

    def run(self, filepath):
        if not os.path.exists(filepath):
            print(f"❌ Error: {filepath} is not in the stadium!")
            return

        print("🎬 Kick-off! The match has started...")
        print("-" * 30)

        with open(filepath, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                # تجاهل التعليقات والأسطر الفارغة
                line = line.split("//")[0].strip()
                tokens = line.split()
                
                for token in tokens:
                    if token in self.commands:
                        self.commands[token]()

        print("\n" + "-" * 30)
        print("🏁 Full Time! SIUUUUUUUUUU! 🏆⚽")

if __name__ == "__main__":
    engine = RonaldoInterpreter()
    # تأكد من وجود ملف main.ronaldo في نفس المجلد
    engine.run("main.ronaldo")