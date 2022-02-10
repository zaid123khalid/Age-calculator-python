from tkinter import *
import datetime
from tkinter import ttk

age_calc = Tk()
age_calc.title("Age Calculator")
age_calc.resizable(False, False)

disp = StringVar()


def calc_age():
    year = datetime.date.today().year
    month = datetime.date.today().month
    date = datetime.date.today().day

    birth_year = int(yrs.get())
    birth_month = int(months.get())
    birth_date = int(day.get())

    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if birth_date > date:
        month = month - 1
        date = date + mon[birth_month - 1]

    if birth_month > month:
        year = year - 1
        month = month + 12

    your_age = f"{year - birth_year}years {month - birth_month}month {date - birth_date}days"
    disp.set(your_age)


yrs_lbl = Label(age_calc, text="Birth Year", font=15)
yrs_lbl.grid(row=2, column=1)

mon_lbl = Label(age_calc, text="Birth Month", font=15)
mon_lbl.grid(row=3, column=1)

day_lbl = Label(age_calc, text="Birth Day", font=15)
day_lbl.grid(row=4, column=1)

values = [[a] for a in range(1950, 2022)]

yrs = ttk.Combobox(age_calc, values=values, width=30)
yrs.grid(row=2, column=2)

values1 = [[a] for a in range(00, 13)]

months = ttk.Combobox(age_calc, values=values1, width=30)
months.grid(row=3, column=2)

values2 = [[a] for a in range(00, 32)]

day = ttk.Combobox(age_calc, values=values2, width=30)
day.grid(row=4, column=2)

btn = Button(age_calc, text="Calculate Age", font=5, bg="black", fg="white", width=25, command=calc_age)
btn.grid(row=5, column=2)

ages_lbl = Label(age_calc, text="Your Age", font=15)
ages_lbl.grid(row=6, column=1)

age_lbl = Label(age_calc, textvariable=disp, font=50, width=25, fg="white", bg="black")
age_lbl.grid(row=6, column=2)

age_calc.mainloop()