import os

class ConsoleTools:
    @staticmethod
    def clearConsole():
        os.system("cls" if os.name == "nt" else "clear")