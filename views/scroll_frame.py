
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class ScrollableFrame(ttk.Frame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.canvas = ttk.Canvas(self, highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview,
            bootstyle=ROUND
        )

        self.content = ttk.Frame(self.canvas)

        self.content.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.content,
            anchor="nw"
        )

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(
                canvas_window,
                width=e.width
            )
        )

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # --- Mouse Wheel Scrolling Setup ---
        
        def _on_mousewheel(event):
            # Windows and MacOS use event.delta
            if event.delta:
                self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            # Linux uses event.num (4 = scroll up, 5 = scroll down)
            elif event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

        # Bind events to the Canvas and Content frame when the mouse enters/leaves
        def _bind_to_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Windows / macOS
            self.canvas.bind_all("<Button-4>", _on_mousewheel)    # Linux up
            self.canvas.bind_all("<Button-5>", _on_mousewheel)    # Linux down

        def _unbind_from_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")

        # Trigger binding ONLY when the mouse is physically hovering over this widget
        self.bind("<Enter>", _bind_to_mousewheel)
        self.bind("<Leave>", _unbind_from_mousewheel)
