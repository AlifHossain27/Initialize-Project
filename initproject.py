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

    def css_menu(self):
        css_options = [ "CSS", "TailwindCSS", "Quit" ]
        css_menu = TerminalMenu(css_options, title= "Choose a CSS Library")

        while not self.quitting:
            css_options_index = css_menu.show()
            css_options_choice = css_options[css_options_index]

            if css_options_choice == "CSS":
                self.css_type = "CSS"
                break
            if css_options_choice == "TailwindCSS":
                self.css_type = "TailwindCSS"
                break
            if css_options_choice == "Quit":
                self.quitting = True


    def create_django_project(self) -> None:
        self.css_menu()
        with yaspin() as loader:
            loader.text = "Creating a new Django Project"
            loader.color = "green"
            os.system("conda run -n web django-admin startproject core .")
            os.system("touch .env")
            with open(f'{self.cwd}/.env', 'w') as file:
                file.writelines("DEBUG=True")
            loader.ok("✔")

    def env_setup(self) -> None:
        with yaspin() as loader:
            loader.text = "Setting up env"
            loader.color = "green"
            # Importing environ
            with open(f'{self.cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if 'from pathlib import Path' in line:
                    env_import = 'import environ \n\n'
                    lines.insert(i + 1, env_import + '\n')
                    break
            with open(f'{self.cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)
            # Initializing ENV
            with open(f'{self.cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if 'BASE_DIR = Path(__file__).resolve().parent.parent' in line:
                    init_env = '''
env = environ.Env(
    DEBUG = (bool,False)
    ) \n''' + "environ.Env.read_env(BASE_DIR / '.env') \n"
                    lines.insert(i + 1, init_env + '\n')
                    break
            with open(f'{self.cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)
            # Using DEBUG of env
            with open(f'{self.cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if "DEBUG = True" in line:
                    lines[i] = "DEBUG = env('DEBUG')"
                    break
            with open(f'{self.cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)


        
    def create_frontend_templates(self) -> None:
        with yaspin() as loader:
            base_html = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block head_title %}{% endblock %}</title>
        {% block extra_head %}
        {% endblock %}
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>
'''
            loader.text = "Adding Template"
            loader.color = "green"
            # Creating templates folder
            os.mkdir("templates")
            # Creating base.html file in templates folder
            os.system("cd templates && touch base.html")
            # Writing base html
            with open(f'{self.cwd}/templates/base.html', 'w') as file:
                file.writelines(base_html)
            # Adding Template files path to settings.py
            with open(f'{self.cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                    if '"DIRS": []' in line:
                        lines[i] = '        "DIRS": [BASE_DIR / "templates"],\n'
                        break
            with open(f'{self.cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)
            loader.ok("✔")
    
    def css_setup(self) -> None:
        with yaspin() as loader:
            loader.text = "Adding CSS"
            loader.color = "green"
            if self.css_type == "CSS":
                # Creating static folder
                os.mkdir("static")
                # Creating style.css in static folder
                os.system("cd static && touch style.css")
                # Adding Static files path to settings.py
                with open(f'{self.cwd}/core/settings.py', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '# Static files (CSS, JavaScript, Images)' in line:
                        tailwindcdn = 'STATICFILES_DIRS = [BASE_DIR / "static"]'
                        lines.insert(i + 1, tailwindcdn + '\n')
                        break
                with open(f'{self.cwd}/core/settings.py', 'w') as file:
                    file.writelines(lines)
            if self.css_type == "TailwindCSS":
                # Adding TailwindCSS CDN to base.html file
                with open(f'{self.cwd}/templates/base.html', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in line:
                        tailwindcdn = '        <script src="https://cdn.tailwindcss.com"></script>'
                        lines.insert(i + 1, tailwindcdn + '\n')
                        break
                with open(f'{self.cwd}/templates/base.html', 'w') as file:
                    file.writelines(lines)
            else:
                pass
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
                self.env_setup()
                self.create_frontend_templates()
                self.css_setup()
                break


if __name__ == '__main__':
    InitializeProject().run()