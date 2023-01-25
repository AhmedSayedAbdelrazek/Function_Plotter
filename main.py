#import Libraries
from tkinter import *
#import messagebox
from tkinter import messagebox
from qbstyles import mpl_style
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import re

# initialize the FIGURE that will contains plot
figure= plt.Figure(figsize=(6, 6),dpi=100)

#set colour to figure
figure.patch.set_facecolor('#264752')



#function to plot the graph in tkinter window
def plot(canvas, plot1, min_x, max_x, equation):
    # input range
    X,y = [], []
    x = 0
    for i in range(int(min_x), int(max_x)):
        x = i
        # Create x data points using numpy.
        X.append(i)
        # Create a user-defined function using, def, i.e., f(x).
        y.append(eval(equation.replace("^", "**")))

    # clear last plotted figure
    plot1.clear()
    # Plot x and f(x) using plot() method.
    plot1.plot(X, y)
    # To display the figure, use draw() method.
    canvas.draw()

#this function uses to check
# equation valid or not
def validate_eq(eq_str):
    try:
        # check if contain any not valid character
        special_char = False
        regexp = re.compile('[^0-9x\+\-\/\*\^]+')
        if regexp.search(eq_str):
            special_char = True

        # show error message
        if special_char:
            messagebox.showerror("Error", "Invalid Syntax in Equation please write equation Again ")
            return False
        return True

    except:
        messagebox.showerror("Error", "Invalid Syntax in equation please write equation Again ")
        return False


# check syntax of x value min and max valid or not
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
        except ValueError:
            messagebox.showerror("Error", "No.. input is not a number. It's a string please write X Values again "
                                          "properly")
            # if can't convert x to int or float'
            return -1

    # if i could convert
    return val


# check input validation
def validate_input(canvas, plot1, min_x_entry, max_x_entry, eq_entry):
    # value coming from equation input
    # remove spaces
    eq_str = ''.join(eq_entry.get().split())
    # if condition returns True, then nothing happens:
    # if condition returns False, AssertionError is raised:
    f = validate_eq(eq_str)

    if not f:
        return

    # check valid number or not
    min_x = check_user_input(min_x_entry.get())

    # check valid number o r not
    max_x = check_user_input(max_x_entry.get())

    if min_x == -1 or max_x == -1:
        return

    # plot function
    plot(canvas, plot1, min_x, max_x, eq_str)


# make program GUI
def program_GUI():
    # the main Tkinter window
    window = Tk()

    # setting the title
    window.title('Function Plotter')

    # dimensions of the main window
    window.geometry("1000x600")

    # make grid response
    for i in range(5):
        window.grid_rowconfigure(i, weight=1)
        for j in range(3):
            window.grid_columnconfigure(j, weight=1)

    # set window color
    window.configure(bg='#1f3b3d')

    # adding the subplot
    mpl_style(dark=True)
    plot1 = figure.add_subplot(111)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(figure,master=window)
    canvas.draw()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,window, pack_toolbar=False)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(row=0, column=2,columnspan=6, rowspan=9, padx=15, pady=15)

    # equation label
    eq_label = Label(master=window,
                     height=1,
                     width=12,font=("Arial", 14),
                     text="Equation")
    # place the eq_label
    # in main window
    eq_label.grid(row=0, column=0, padx=15, pady=15)

    # equation input
    eq_entry = Entry(window,font=("Arial", 15))

    # place the eq_label
    # in main window
    eq_entry.grid(row=0, column=1, padx=15, pady=15)

    # min value of x label
    min_x_label = Label(master=window,
                        height=1,
                        width=12,

                        font=("Arial", 14),
                        text="Min Val of X"
                        )
    # place the min value of x label
    # in main window
    min_x_label.grid(row=1, column=0, padx=15, pady=15)

    # min value of x input
    min_x_entry = Entry(window,

                        font=("Arial", 15),
                        width=12)

    # place the min value of x input
    # in main window
    min_x_entry.grid(row=1, column=1, padx=15, pady=15)

    # max value of x label
    max_x_label = Label(master=window,
                        height=1,
                        width=12,

                        font=("Arial", 14),
                        text="Max Val of X"
                        )
    # place the max value of x label
    # in main window
    max_x_label.grid(row=2, column=0, padx=15, pady=15)

    # max value of x input
    max_x_entry = Entry(window,

                        font=("Arial", 15),
                        width=12)

    # place the max value of x input
    # in main window
    max_x_entry.grid(row=2, column=1, padx=15, pady=15)

    # button that displays the plot
    plot_button = Button(master=window,
                         command=lambda: validate_input(canvas, plot1, min_x_entry, max_x_entry, eq_entry),
                         height=2,
                         width=10,
                         bg='#232b2b',
                         fg='#dadddb',
                         font=("Arial", 15),
                         text="Show Plot")
    btn=Button(window, text="Exit", command=window.quit, bg='#232b2b',
                         fg='#dadddb',font=("Arial",10))
    btn.grid(row=3,column=1, padx=12, pady=10)
    # place the button
    # in main window
    plot_button.grid(row=3, column=0, columnspan=1, padx=15, pady=15)

    toolbar.grid(row=4, column=0, columnspan=2, padx=15, pady=15)

    # run the gui
    window.mainloop()


if __name__ == '__main__':
    # To plot a function defined with def in Python, we can take the following steps −
    program_GUI()
