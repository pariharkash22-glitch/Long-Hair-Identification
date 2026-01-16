print("1. Starting main.py...")
import sys
import os

print("2. Importing Tkinter...")
try:
    import tkinter as tk
except Exception as e:
    print(f"FAILED to import tkinter: {e}")

print("3. Attempting to import GenderApp from src...")
try:
    from src.gui import GenderApp
    print("4. Import successful!")
except Exception as e:
    print(f"FAILED at Step 3: {e}")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    print("5. Initializing Root...")
    try:
        root = tk.Tk()
        app = GenderApp(root)
        print("6. Entering MainLoop (Window should open now)...")
        root.mainloop()
    except Exception as e:
        print(f"FAILED to start GUI: {e}")