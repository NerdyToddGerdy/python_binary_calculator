import logging
import tkinter as tk
from tkinter import Tk, Label, Button, Entry


def setup_logging() -> logging.Logger:
    # create logger
    logs = logging.getLogger("python_binary_calculator")
    logs.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logs.addHandler(ch)

    logs.info('Logger has been set')
    return logs


class MainGui:
    def __init__(self, leader):
        self.leader = leader
        leader.title("Binary Calculator")

        self.input_label = Label(leader, text="numerical input").grid(row=0)
        self.input_entry = Entry(leader)
        self.input_entry.grid(row=0, column=1)
        self.calculate_to_binary_button = Button(
            leader,
            text='Calculate',
            command=self.calculate_to_binary
        ).grid(
            row=2,
            column=0,
            sticky=tk.W,
            pady=4
        )
        self.output: tk.Label = Label(leader, text="result:")
        self.output.grid(row=2, column=1)

    def calculate_to_binary(self):
        logger.info("calculating to binary")
        try:
            res = int(self.input_entry.get())
            logger.info(f"input is {str(self.input_entry.get())}")
            self.output.configure(text=f"result: {bin(int(self.input_entry.get()))[2:]}")
        except TypeError as e:
            self.output.configure(text=f"{self.input_entry.get()} is not a valid integer")
            logger.error("Value is not an integer")
            logger.error(e)





if __name__ == '__main__':
    logger: logging.Logger = setup_logging()

    calculator = Tk()
    main = MainGui(calculator)
    calculator.mainloop()
