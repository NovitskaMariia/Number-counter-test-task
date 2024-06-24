from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("Numbers finder")
root.geometry("600x400")
root.resizable(0, 0)

frame_top = Frame(root, bg="#ffb700", bd=5)
frame_top.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_bottom = Frame(root, bg="#ffb700", bd=5)
frame_bottom.place(relx=0.1, rely=0.30, relwidth=0.8, relheight=0.6)

label_top = Label(
    frame_top,
    text="Choose a .txt file with numbers:",
    bg="#ffb700",
    font="Helvetica",
)
label_top.pack(side=LEFT, padx=20)

text_message = "Here you will see the result of calculation after opening file"
text_var = Text(frame_bottom, bg="#ffb700", font="Helvetica", wrap=WORD)
text_var.insert(1.0, text_message)
text_var.config(state=DISABLED)
text_var.pack(expand=True, fill=BOTH)
numbers = []


def open_file():
    global numbers
    file_path = filedialog.askopenfilename(
        title="Select a text file", filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        numbers = []
        try:
            with open(file_path) as file:
                for line in file:
                    try:
                        num = int(line.strip())
                        numbers.append(num)
                    except ValueError:
                        continue

            text_var.config(state=NORMAL)
            text_var.delete(1.0, END)
            text_var.insert(END, "Counting . . .")
            root.update_idletasks()

            if numbers:
                max_number = max(numbers)
                min_number = min(numbers)
                median_number = find_median()
                arith_mean_number = find_arithmetic_mean()
                increasing_seq = find_increasing_sequence()
                decreasing_seq = find_decreasing_sequence()
                text_var.delete(1.0, END)
                text_var.insert(
                    END,
                    f"Max number: {max_number}\n"
                    f"Min number: {min_number}\n"
                    f"Median number: {median_number}\n"
                    f"Arithmetic mean: {arith_mean_number}\n"
                    f"Increasing sequence: {increasing_seq}\n"
                    f"Decreasing sequence: {decreasing_seq}\n",
                )
            else:
                text_var.insert(END, "No valid numbers found in the file.")

            text_var.config(state=DISABLED)

        except Exception as e:
            text_var.config(state=NORMAL)
            text_var.delete(1.0, END)
            text_var.insert(END, f"Error: {e}")
            text_var.config(state=DISABLED)
        root.update_idletasks()


open_button = Button(
    frame_top,
    text="Open File",
    command=open_file,
)
open_button.pack(side=RIGHT, padx=20)


def find_median():
    lst = sorted(numbers)
    n = len(lst)
    if n % 2 == 0:
        median_number = (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        median_number = lst[n // 2]
    return median_number


def find_arithmetic_mean():
    arith_mean_number = sum(numbers) / len(numbers)
    return arith_mean_number


def find_increasing_sequence():
    if not numbers:
        return []
    increasing_sequence = []
    increasing_sequence_temp = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            increasing_sequence_temp.append(numbers[i])
        else:
            if len(increasing_sequence_temp) > len(increasing_sequence):
                increasing_sequence = increasing_sequence_temp
            increasing_sequence_temp = [numbers[i]]
    if len(increasing_sequence_temp) > len(increasing_sequence):
        increasing_sequence = increasing_sequence_temp
    return increasing_sequence


def find_decreasing_sequence():
    if not numbers:
        return []
    decreasing_sequence = []
    decreasing_sequence_temp = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            decreasing_sequence_temp.append(numbers[i])
        else:
            if len(decreasing_sequence_temp) > len(decreasing_sequence):
                decreasing_sequence = decreasing_sequence_temp
            decreasing_sequence_temp = [numbers[i]]
    if len(decreasing_sequence_temp) > len(decreasing_sequence):
        decreasing_sequence = decreasing_sequence_temp
    return decreasing_sequence


root.mainloop()
