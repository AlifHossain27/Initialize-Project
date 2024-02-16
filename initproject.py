#!/usr/bin/env python3
import os
from yaspin import yaspin
from simple_term_menu import TerminalMenu

class InitializeProject:
    def __init__(self) -> None:
        self.quitting: bool =  False
        self.cwd: str = os.getcwd()
        self.db_type: str = "SQLite"
        self.css_type: str = "CSS"
        self.ui_lib: str = "None"


    def create_django_project(self) -> None:
        with yaspin() as loader:
            loader.text = "Creating a new Django Project"
            loader.color = "green"
            os.system("conda run -n web django-admin startproject core .")
            os.system("touch .env")
            loader.ok("✔")
        


    def run(self) -> None:
        main_options = [ "Django", "Quit" ]

        main_menu = TerminalMenu(main_options, title = "Choose a new project")

        while not self.quitting:
            main_options_index = main_menu.show()
            main_options_choice = main_options[main_options_index]
            if main_options_choice == "Quit":
                self.quitting = True
            if main_options_choice == "Django":
                self.create_django_project()
                break


if __name__ == '__main__':
    InitializeProject().run()