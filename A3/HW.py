import tkinter as tk 

window = tk()
window.geometry('400x200')
window.title('interest Calculator APP')

amt_lbl = tk.Label(window,text='Amount:')
amt_lbl.pack(pady=10)
amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)

time_label = tk.label(window,text = 'Time(in years):')
time_label.pack(pady=10)
time_label.pack(pady=10)
time_entry = tk.Entry(window)
time_entry.pack(pady=5)

rate_label = tk.Label(window,text= 'Interest Rate(%)')
rate_label.pack(pady=10)