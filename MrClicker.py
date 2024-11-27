import time
from colorama import Fore, Back, Style
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import colorama
from pystyle import Colors, Colorate

# Affichage de la bannière
print(Colorate.Horizontal(Colors.green_to_cyan, """
  __  __         _       _        ___ _ _    _           
 |  \/  |_ _    /_\ _  _| |_ ___ / __| (_)__| |_____ _ _ 
 | |\/| | '_|  / _ \ || |  _/ _ \ (__| | / _| / / -_) '_|
 |_|  |_|_|   /_/ \_\_,_|\__\___/\___|_|_\__|_\_\___|_|  
                                                         
""", 1))

# Configuration de l'auto clicker
delay = 0.01
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class FastAutoClicker:
    def __init__(self):
        self.running = False
        self.program_running = True
        self.mouse = Controller()

    def start_clicking(self):
        while self.program_running:
            if self.running:
                self.mouse.click(button)
                time.sleep(delay)

    def toggle_running(self):
        self.running = not self.running
        state = "ENABLED" if self.running else "DISABLED"
        print(f"Auto Clicker: {state}")

    def exit(self):
        self.program_running = False

auto_clicker = FastAutoClicker()

def on_press(key):
    if key == start_stop_key:
        auto_clicker.toggle_running()
    elif key == exit_key:
        auto_clicker.exit()
        return False

with Listener(on_press=on_press) as listener:
    print(Fore.GREEN+"Fast Auto Clicker Ready:")
    print(Fore.GREEN+"- Press 's' to start/stop.")
    print(Fore.GREEN+"- Press 'e' to exit.")
    auto_clicker.start_clicking()
    listener.join()
