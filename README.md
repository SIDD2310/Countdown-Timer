# Countdown-Timer

This project is a Python implementation of a countdown timer that can be used in a GUI application. The code consists of two main classes: CountdownTimer and TimerApp.

The CountdownTimer class is responsible for keeping track of the time and providing methods for starting, stopping, resetting, pausing, and resuming the timer. The class also includes a remaining_time() method which returns the remaining time in seconds.

The TimerApp class is a subclass of tkinter's Tk class, which is used to create the GUI for the countdown timer. The class includes several methods that correspond to the different buttons in the GUI: start_timer, stop_timer, reset_timer, pause_timer, and resume_timer. These methods control the behavior of the timer and update the GUI accordingly. The class also includes an update_time method that updates the time display on the GUI every second and an alarm method that plays an alarm sound when the timer reaches zero.

The GUI consists of a label that displays the remaining time, an entry box where the user can input the number of seconds for the timer, and several buttons for starting, stopping, resetting, pausing, and resuming the timer. The buttons change their state according to the actions and the remaining time is displayed in the format of minutes and seconds.

The code also uses the after method to schedule the next call of the update_time function, thus allowing for real-time updates of the remaining time in the GUI.

In summary, the code provides a full-featured countdown timer with a graphical user interface (GUI) that allows the user to input a number of seconds for the countdown timer, and then start, stop, reset, pause, and resume the timer. It also plays an alarm sound when the timer reaches zero, and updates the remaining time on the GUI in real time. This makes it easy for the user to monitor the remaining time and take appropriate actions.

It follows object oriented programming paradigm, where a class CountdownTimer is defined which provides the basic functionality of the timer and another class TimerApp is used to create GUI and handle the events of the timer.

<img width="158" alt="image" src="https://user-images.githubusercontent.com/108021988/212564733-10d7f090-f774-4aac-b122-80d981fe04e1.png">
