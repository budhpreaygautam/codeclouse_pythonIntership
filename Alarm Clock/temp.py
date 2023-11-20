import tkinter as tk
from time import strftime
from tkinter import ttk
from datetime import datetime, timedelta
import time
import threading
import pygame
from PIL import Image, ImageTk


class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock App")
        self.root.geometry("700x500")

        # Load background image
        bg_image = Image.open("bgimg.jpg")  # Replace with your image file path
        bg_image = bg_image.resize((700, 500))
        self.background_image = ImageTk.PhotoImage(bg_image)

        # Create canvas for background image
        self.canvas = tk.Canvas(self.root, width=700, height=500)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Create label for displaying time
        self.time_label = ttk.Label(self.canvas, text="", font=('Helvetica', 24), background='white')
        self.time_label.place(relx=0.5, rely=0.2, anchor='center')


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












# import tkinter
# from tkinter import *
#
# import customtkinter
# from PIL import ImageTk, Image
#
# root_tk = tkinter.Tk()  # create the Tk window like you normally do
# root_tk.geometry("700x500")
# root_tk.title("Alarm Clock")
#
# frame = Frame(root_tk, width=600, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)
#
# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("bgimg.jpg"))
#
# # Create a Label Widget to display the text or Image
# label = Label(frame, image=img)
# label.pack()
#
# def button_function():
#     print("button pressed")
#
#
# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=root_tk, corner_radius=2,
#                                  text="Set Alarm",
#                                  command=button_function)
# button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
# root_tk.mainloop()
