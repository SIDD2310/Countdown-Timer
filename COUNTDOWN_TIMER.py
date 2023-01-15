#!/usr/bin/env python
# coding: utf-8

# In[21]:


import tkinter as tk
from tkinter import ttk
import time
import winsound

class CountdownTimer:

    def __init__(self, seconds):
        self.seconds = seconds
        self.start_time = None
        self.end_time = None
        self.paused_time = None
        self.paused = False

    def start(self):
        self.start_time = time.time()
        self.end_time = self.start_time + self.seconds

    def stop(self):
        self.seconds = 0
        self.end_time = None

    def reset(self):
        self.seconds = 0
        self.start_time = None
        self.end_time = None
        self.paused_time = None
        self.paused = False

    def pause(self):
        if not self.paused:
            self.paused = True
            self.paused_time = time.time()

    def resume(self):
        if self.paused:
            self.paused = False
            self.start_time += time.time() - self.paused_time
            self.end_time += time.time() - self.paused_time

    def remaining_time(self):
        if self.start_time is None:
            return self.seconds
        elif self.paused:
            return self.end_time - self.paused_time
        else:
            return self.end_time - time.time()
        
    

class TimerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Countdown Timer")

        self.timer = CountdownTimer(0)

        self.time_string = tk.StringVar()
        self.time_string.set("00:00")

        self.label = ttk.Label(self, textvariable=self.time_string)
        self.label.pack()

        

        self.seconds_entry = ttk.Entry(self)
        self.seconds_entry.pack()

        self.start_button = ttk.Button(self, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = ttk.Button(self, text="Stop", command=self.stop_timer, state='disable')
        self.stop_button.pack()

        self.reset_button = ttk.Button(self, text="Reset", command=self.reset_timer, state='disable')
        self.reset_button.pack()

        self.pause_button = ttk.Button(self, text="Pause", command=self.pause_timer, state='disable')
        self.pause_button.pack()

        self.resume_button = ttk.Button(self, text="Resume", command=self.resume_timer, state='disable')
        self.resume_button.pack()

    def start_timer(self):
        self.timer.seconds = int(self.seconds_entry.get())
        self.timer.start()
        self.start_button.config(state='disable')
        self.stop_button.config(state='normal')
        self.reset_button.config(state='normal')
        self.pause_button.config(state='normal')
        self.update_time()


    def stop_timer(self):
        self.timer.stop()
        self.start_button.config(state='normal')
        self.stop_button.config(state='disable')
        self.reset_button.config(state='disable')
        self.pause_button.config(state='disable')
        self.resume_button.config(state='disable')

    def reset_timer(self):
        self.timer.reset()
        self.time_string.set("00:00")
        self.start_button.config(state='normal')
        self.stop_button.config(state='disable')
        self.reset_button.config(state='disable')
        self.pause_button.config(state='disable')
        self.resume_button.config(state='disable')

    def pause_timer(self):
        self.timer.pause()
        self.pause_button.config(state='disable')
        self.resume_button.config(state='normal')

    def resume_timer(self):
        self.timer.resume()
        self.pause_button.config(state='normal')
        self.resume_button.config(state='disable')
        self.update_time()
        
    def alarm(self):
        winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)

    def update_time(self):
        remaining = self.timer.remaining_time()
        if remaining <= 0:
            self.time_string.set("00:00")
            self.alarm()
            self.stop_timer()
        else:
            minutes, seconds = divmod(int(remaining), 60)
            self.time_string.set("{:02d}:{:02d}".format(minutes, seconds))
            self.after(1000, self.update_time)



if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()

       


# In[ ]:





# In[ ]:





# In[ ]:




