"""
Tommy Ju
A01347715

Matthew
A01373290
"""
import tkinter as tk

rows = 10
columns = 10

# root window
root = tk.Tk()
root.title("RPS Ninja")
root.geometry("600x600")
root.configure(background='black')
# root.columnconfigure(rows)
# root.rowconfigure(rows)



for row in range(rows):
    root.grid_rowconfigure(row, weight=1)
    for column in range(columns):
        root.grid_columnconfigure(column, weight=1)
        # add x to cell
        cell = tk.Frame(root, bg="lightblue")
        cell.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)


# widgets

# x = tk.Label(root, text="x", bg="purple").grid(row=0, column=0)
# y = tk.Label(root, text="y", bg="purple").grid(row=0, column=1)

root.mainloop()


def main():
    pass


if __name__ == "__main__":
    main()
