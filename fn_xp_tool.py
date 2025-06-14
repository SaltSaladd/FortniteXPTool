import tkinter as tk
from tkinter import ttk, messagebox
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
import threading
import time
import random
import json

keyboard = KeyboardController()
mouse = MouseController()

running = True
macro_thread = None

# ---------- Macro Functions ----------
def lego_afk():
    global running
    running = True

    def worker():
        while running:
            keyboard.press('p')
            keyboard.release('p')
            time.sleep(random.uniform(1, 5))

    threading.Thread(target=worker, daemon=True).start()
    messagebox.showinfo("Lego AFK", "Lego AFK macro started!")

def start_macro():
    global running, macro_thread
    running = True

    key = key_entry.get().lower()
    try:
        delay = float(delay_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the delay.")
        return

    def macro_worker():
        while running:
            if key == "scrollup":
                mouse.scroll(0, 1)
            elif key == "scrolldown":
                mouse.scroll(0, -1)
            else:
                keyboard.press(key)
                keyboard.release(key)
            time.sleep(delay)

    macro_thread = threading.Thread(target=macro_worker, daemon=True)
    macro_thread.start()
    messagebox.showinfo("Macro Started", f"Macro for '{key}' started with {delay} second delay.")

def stop_all():
    global running
    running = False
    messagebox.showinfo("Stopped", "All macros have been stopped.")

# ---------- Macro Configuration Saving/Loading ----------
def save_macro_config():
    key = key_entry.get()
    delay = delay_entry.get().strip()
    config = {"key": key, "delay": delay}
    try:
        with open("macro_config.json", "w") as f:
            json.dump(config, f)
        messagebox.showinfo("Saved", "Macro saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save macro configuration:\n{e}")

def load_macro_config():
    try:
        with open("macro_config.json", "r") as f:
            config = json.load(f)
        key_entry.delete(0, tk.END)
        key_entry.insert(0, config.get("key", ""))
        delay_entry.delete(0, tk.END)
        delay_entry.insert(0, config.get("delay", "1"))
        messagebox.showinfo("Loaded", "Macro loaded successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved macro found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load macro configuration:\n{e}")

# ---------- Help Popup ----------
def show_help(text):
    messagebox.showinfo("Help", text)

# ---------- GUI ----------
root = tk.Tk()
root.title("FN XP Tool")
root.geometry("350x340")

# Button 1: Lego AFK
row1 = ttk.Frame(root)
row1.pack(pady=5)
ttk.Button(row1, text="Lego AFK", command=lego_afk).pack(side="left")
ttk.Button(row1, text="?", width=2, command=lambda: show_help(
    "To use this macro correctly:\n\n"
    "- In the lobby, change the mode to Battle Royale.\n"
    "- Set your 'Fire' (or 'Fire Weapon') keybind to 'P'.\n"
    "- Disable 'Auto claim rewards' for ALL passes, or popups may interfere.\n"
    "- Load into your Lego sandbox world.\n"
    "- Then, launch this macro."
)).pack(side="left", padx=5)

# Custom Macro Frame
frame = ttk.LabelFrame(root, text="Custom Macro")
frame.pack(pady=10, padx=10, fill="x")

ttk.Label(frame, text="Key (e.g. a, space, scrollup, scrolldown):").pack(padx=5, pady=2, anchor="w")
key_entry = ttk.Entry(frame)
key_entry.pack(padx=5, fill="x")

ttk.Label(frame, text="Delay (seconds):").pack(padx=5, pady=2, anchor="w")
delay_entry = ttk.Entry(frame)
delay_entry.insert(0, "1")
delay_entry.pack(padx=5, fill="x")

# Row for Custom Macro and Help Button
row2 = ttk.Frame(frame)
row2.pack(pady=5)
ttk.Button(row2, text="Custom Macro", command=start_macro).pack(side="left")
ttk.Button(row2, text="?", width=2, command=lambda: show_help(
    "Spams your selected key or mouse scroll with the chosen delay.\n"
    "- Use 'scrollup' or 'scrolldown' for mouse.\n"
    "- Use standard keys like a, b, space, etc."
)).pack(side="left", padx=5)

# Row for Save and Load Macro configuration buttons
row_save = ttk.Frame(frame)
row_save.pack(pady=5)
ttk.Button(row_save, text="Save Macro", command=save_macro_config).pack(side="left", padx=5)
ttk.Button(row_save, text="Load Macro", command=load_macro_config).pack(side="left", padx=5)

# Button 3: Stop All
row3 = ttk.Frame(root)
row3.pack(pady=10)
ttk.Button(row3, text="Stop All", command=stop_all).pack(side="left")
ttk.Button(row3, text="?", width=2, command=lambda: show_help("Stops all running macros immediately.")).pack(side="left", padx=5)

root.mainloop()
