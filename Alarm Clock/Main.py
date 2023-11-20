import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import time
import threading
import pygame


class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("600x400")  # Custom screen size

        # Load background image
        bg_image = tk.PhotoImage(file="bgimg.jpg")  # Provide your image file path
        bg_label = tk.Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        self.alarm_time = None
        self.alarm_active = False

        self.create_widgets()

    def create_widgets(self):
        # Label to display the current time
        self.time_label = ttk.Label(self.root, text="", font=('Helvetica', 24))
        self.time_label.pack(pady=10)

        # Entry to input the alarm time
        self.alarm_entry = ttk.Entry(self.root, font=('Helvetica', 14))
        self.alarm_entry.insert(0, "HH:MM")
        self.alarm_entry.pack(pady=10)

        # Button to set the alarm
        self.set_alarm_button = ttk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)

        # Button to stop the alarm
        self.stop_alarm_button = ttk.Button(self.root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_alarm_button.pack(pady=10)

        # Update the time display
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

        if self.alarm_active and self.alarm_time is not None:
            now = datetime.now().strftime("%H:%M")
            if now == self.alarm_time:
                self.activate_alarm()

    def set_alarm(self):
        alarm_time_str = self.alarm_entry.get()
        try:
            datetime.strptime(alarm_time_str, "%H:%M")
        except ValueError:
            self.show_error("Invalid time format. Please use HH:MM.")
            return

        self.alarm_time = alarm_time_str
        self.alarm_active = True

        self.set_alarm_button.config(state=tk.DISABLED)
        self.stop_alarm_button.config(state=tk.NORMAL)

    def stop_alarm(self):
        self.alarm_active = False
        self.set_alarm_button.config(state=tk.NORMAL)
        self.stop_alarm_button.config(state=tk.DISABLED)

    def activate_alarm(self):
        self.alarm_active = False
        self.set_alarm_button.config(state=tk.NORMAL)
        self.stop_alarm_button.config(state=tk.DISABLED)

        # Play a sound in a separate thread using threading
        threading.Thread(target=self.play_sound).start()

    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("alarm_sound.mp3")  # Provide your sound file path
        pygame.mixer.music.play()

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
