from ttkbootstrap import ScrolledText
from ttkbootstrap.constants import DEFAULT
from services.sql_tokenizer import SQLTokenizer

class SQLEditor(ScrolledText):

    def __init__(self, master=None, *, padding=2, bootstyle=DEFAULT, auto_hide=False, vbar=True, hbar=False, **kwargs):
        super().__init__(master, padding=padding, bootstyle=bootstyle, auto_hide=auto_hide, vbar=vbar, hbar=hbar, **kwargs)

        # defined syntax tags
        self.tags = ("KEYWORD", "STRING", "COMMENT", "NUMBER", "OPERATOR")

        # Configure visual tag styles
        self.text.tag_configure("KEYWORD", foreground="#569CD6", font=("Consolas", 11, "bold"))  
        self.text.tag_configure("STRING", foreground="#CE9178")
        self.text.tag_configure("COMMENT", foreground="#6A9955", font=("Consolas", 11, "italic"))
        self.text.tag_configure("NUMBER", foreground="#B5CEA8")
        self.text.tag_configure("OPERATOR", foreground="#D4D4D4")
    
        # Bind the modified virtual event
        self.text.bind("<<Modified>>", self.highlight)

    def highlight(self, event=None):
        if self.text.edit_modified():
            # Clear previous highlighting tags across the entire document
            for tag in self.tags:
                self.text.tag_remove(tag, "1.0", "end")

            # Get all text split by line ('end-1c' ignores trailing newline)
            content = self.text.get("1.0", "end-1c").splitlines()

            # Tokenize and apply tags line by line
            for line_idx, line in enumerate(content, start=1):
                if not line.strip():
                    continue

                for token_type, start_col, end_col in SQLTokenizer.get_line_tokens(line):
                    if token_type in self.tags:
                        start_index = f"{line_idx}.{start_col}"
                        end_index = f"{line_idx}.{end_col}"
                        self.text.tag_add(token_type, start_index, end_index)

            # Reset flag to capture subsequent edits
            self.text.edit_modified(False)