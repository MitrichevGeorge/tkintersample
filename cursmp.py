import tkinter as tk
from tkinter import ttk

cursors = [
    "arrow", "based_arrow_down", "based_arrow_up", "boat", "bogosity",
    "bottom_left_corner", "bottom_right_corner", "bottom_side", "bottom_tee",
    "box_spiral", "center_ptr", "circle", "clock", "coffee_mug", "cross",
    "cross_reverse", "crosshair", "diamond_cross", "dot", "dotbox",
    "double_arrow", "draft_large", "draft_small", "draped_box", "exchange",
    "fleur", "gobbler", "gumby", "hand1", "hand2", "heart", "icon",
    "iron_cross", "left_ptr", "left_side", "left_tee", "leftbutton",
    "ll_angle", "lr_angle", "man", "middlebutton", "mouse", "pencil",
    "pirate", "plus", "question_arrow", "right_ptr", "right_side",
    "right_tee", "rightbutton", "rtl_logo", "sailboat", "sb_down_arrow",
    "sb_h_double_arrow", "sb_left_arrow", "sb_right_arrow", "sb_up_arrow",
    "sb_v_double_arrow", "shuttle", "sizing", "spider", "spraycan",
    "star", "target", "tcross", "top_left_arrow", "top_left_corner",
    "top_right_corner", "top_side", "top_tee", "trek", "ul_angle",
    "umbrella", "ur_angle", "watch", "xterm", "X_cursor"
]

root = tk.Tk()
root.title("Курсоры")
root.geometry("400x600")
root.configure(bg="#262635")

tree = ttk.Treeview(root, columns=("cursor_name"), show="headings")
tree.heading("cursor_name", text="Cursor Name")
tree.column("cursor_name", anchor="center", width=200)

for index, cursor in enumerate(cursors):
    tree.insert("", "end", values=(cursor,), tags=("oddrow" if index % 2 == 0 else "evenrow",))

tree.tag_configure("oddrow", background="#262635", foreground="white")
tree.tag_configure("evenrow", background="#3a3a4a", foreground="white")

cursor_label = tk.Label(root, text="Hover over a cursor to see it here", bg="#262635", fg="white")
cursor_label.pack(pady=10)

def on_enter(event):
    item = tree.identify_row(event.y)
    if item:
        cursor_name = tree.item(item, "values")[0]
        root.config(cursor=cursor_name)
        cursor_label.config(text=f"Current Cursor: {cursor_name}")

tree.bind("<Motion>", on_enter)
tree.bind("<Leave>", lambda event: root.config(cursor=""))

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
root.mainloop()