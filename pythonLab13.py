import tkinter as tk # imports required for program to function
from tkinter import messagebox, scrolledtext
import numpy as np
import matplotlib.pyplot as plt
import sys




def on_ok(): # main method, executes on button press
 
    
    try:
       
        output_text.delete(1.0, tk.END) # Clear the text widget
        # create a time-series array of random values
        np.random.seed(0)
        data = np.random.randn(40)
        # perform exponential smoothing on the data
        smoothed_data = np.zeros_like(data)
        alpha = 0.5
        for i in range(1, len(data)):
            smoothed_data[i] = alpha * data[i] + (1 - alpha) * smoothed_data[i - 1]

            # printing results to the text widget
            print("Original Data:\n", data, "\n")
            print("Smoothed Data:\n", smoothed_data, "\n")


        # plot the original data and the smoothed data
        plt.plot(data, label='Original data')
        plt.plot(smoothed_data, label='Smoothed data', linestyle='dashed')
        plt.legend(loc='upper right')
        plt.show(block=False)

      

    except ValueError:
            messagebox.showerror("Invalid Input", "Please enter values in all fields.")

    
def on_exit(): # exit logic to close the program and present a popup thanking the user
    messagebox.showinfo("Exit", "Thanks for using the program!")
    window.destroy()


window = tk.Tk() # window logic and sizing
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = screen_width // 2  
window_height = screen_height // 2 
window.geometry("500x200+100+50")


window.title("Nicholas C. Simone - Python Lab 13 (numpy)") #titlebar naming

row1 = tk.Frame(window)
row1.pack(pady=(45, 0)) # creating rows for the input and output boxes
row2 = tk.Frame(window)
row2.pack(pady=(10, 0))
row3 = tk.Frame(window)
row3.pack(pady=(10, 0))




output_text = scrolledtext.ScrolledText(window, width=50, height=15)
output_text.pack(padx=10, pady=10, fill='both', expand=True)

class RedirectText:
    def __init__(self, widget):
        self.widget = widget
    def write(self, string):
        self.widget.insert(tk.END, string)
        self.widget.see(tk.END)
    def flush(self):
        pass

# After creating output_text
sys.stdout = RedirectText(output_text)

ok_button = tk.Button(row3, text="Show Arrays", command=on_ok) # OK and EXIT button logic and positioning
ok_button.pack(side=tk.LEFT, padx=(0, 0))
exit_button = tk.Button(row3, text="Exit", command=on_exit)
exit_button.pack(side=tk.LEFT)
window.protocol("WM_DELETE_WINDOW", on_exit)

window.mainloop()