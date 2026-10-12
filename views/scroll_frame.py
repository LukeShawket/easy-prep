
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ScrollableFrame(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.canvas = ttk.Canvas(self, highlightthickness=0)

        scrollbar = ttk.Scrollbar(self,orient="vertical",command=self.canvas.yview,bootstyle=ROUND)

        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        canvas_window = self.canvas.create_window((0, 0),window=self.scrollable_frame,anchor="nw")

        # Keep frame width synced with canvas width
        self.canvas.bind("<Configure>",lambda e: self.canvas.itemconfig(canvas_window,width=e.width))

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left",fill="both",expand=True)

        scrollbar.pack(side="right",fill="y")