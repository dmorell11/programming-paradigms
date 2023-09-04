
import tkinter as tk

class EventExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Handling Example")

        self.button = tk.Button(self.root, text="Click Me!", command=self.handle_button_click)
        self.button.pack(pady=20)

    def handle_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EventExample(root)
    root.mainloop()
