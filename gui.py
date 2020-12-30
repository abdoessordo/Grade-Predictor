from tkinter import *
from main import predict_grade

WIDTH = 500
HEIGHT = 600

# fonts = ['Arial','Helvetica', 'Courier New', 'Courier', 'Comic Sans MS', 'Fixedsys', 'MS Sans Serif', 'MS Serif',
# 'Symbol', 'System', 'Times New Roman', 'Times', 'Verdana']
# for font in fonts:
#     label = Label(labels_frame,
#     text=font, font=(font, 13)) label.pack()


# -------------------------------------------------------------
#                       FUNCTIONS
# -------------------------------------------------------------

def predict():
    entries = [g1_entry, g2_entry, studytime_entry, failures_entry, absences_entry]
    try:
        entries_values = [int(entry.get()) for entry in entries]
        g3 = predict_grade(entries_values)
        g3_label['text'] = g3
        error_label['text'] = ''
    except ValueError:
        error_label['text'] = 'ALL ENTRIES MUST BE INTEGERS'
    finally:
        for entry in entries:
            entry.delete(0, 'end')


# -------------------------------------------------------------
#                   INITIALIZATION
# -------------------------------------------------------------

root = Tk()
root.title("Grade Predictor")
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()


# -------------------------------------------------------------
#                       FRAMES
# -------------------------------------------------------------

bg_frame = Frame(root, bg='red')
bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

holder_frame = Frame(root)
holder_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

labels_frame = Frame(holder_frame)
labels_frame.place(relx=0, rely=0.01, relwidth=0.7, relheight=1)

entries_frame = Frame(holder_frame)
entries_frame.place(relx=0.65, rely=0.02, relwidth=0.3, relheight=1)


# -------------------------------------------------------------
#                           GUI
# -------------------------------------------------------------

# ==================== Labels ==================================
title_label = Label(holder_frame, text='Final Exam Grade Predictor', font=('Times New Roman', 16), fg='red')
title_label.pack()

g1_label = Label(labels_frame, text='Enter grade of the first exam :', fg='black', font=('Arial', 13))
g1_label.place(relx=0.1, rely=0.1)

g2_label = Label(labels_frame, text='Enter grade of the second exam :', fg='black', font=('Arial', 13))
g2_label.place(relx=0.1, rely=0.2)

studytime_label = Label(labels_frame, text='Enter the studying time :', fg='black', font=('Arial', 13))
studytime_label.place(relx=0.1, rely=0.3)

failures_label = Label(labels_frame, text='Enter the amount of failures :', fg='black', font=('Arial', 13))
failures_label.place(relx=0.1, rely=0.4)

absences_label = Label(labels_frame, text='Enter number of absences :', fg='black', font=('Arial', 13))
absences_label.place(relx=0.1, rely=0.5)

g3_label = Label(holder_frame, text='', font=('Arial', 15), fg='red')
g3_label.place(relx=0.48, rely=0.8)

error_label = Label(holder_frame, text='', font=('Arial', 15), fg='red')
error_label.place(relx=0.15, rely=0.8)

# ==================== Entries ==================================

g1_entry = Entry(entries_frame)
g1_entry.place(relx=0.1, rely=0.1)

g2_entry = Entry(entries_frame,)
g2_entry.place(relx=0.1, rely=0.2)

studytime_entry = Entry(entries_frame)
studytime_entry.place(relx=0.1, rely=0.3)

failures_entry = Entry(entries_frame)
failures_entry.place(relx=0.1, rely=0.4)

absences_entry = Entry(entries_frame)
absences_entry.place(relx=0.1, rely=0.5)

# ==================== Buttons ==================================
predict_btn = Button(holder_frame, text='Predict Grade', font=('Arial', 11), command=lambda: predict())
predict_btn.place(relx=0.35, relwidth=0.3, rely=0.7)


# -------------------------------------------------------------
#                        MAIN LOOP
# -------------------------------------------------------------
if __name__ == '__main__':
    root.mainloop()
