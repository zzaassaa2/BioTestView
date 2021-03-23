from tkinter import ttk


class NumberEntry(ttk.Entry):
    def __init__(self, parent, allowDouble: bool, **kwargs):
        validation = parent.register(self.validateComm)
        super().__init__(parent, **kwargs, validate="key", validatecommand=(validation, "%S"))
        self.allow_double = allowDouble

    def validateComm(self, char: bytes):
        if self.allow_double:
            return char.isdigit() or char == '.'
        else:
            return char.isdigit()
