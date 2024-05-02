#!/usr/bin/env python3
import os
from yaspin import yaspin
from simple_term_menu import TerminalMenu

class Database:
    def __init__(self, db_type: str = "SQLite") -> None:
        self.db_type = db_type

class Style:
    def __init__(self, css_type: str = "CSS") -> None:
        self.css_type = css_type

    def css_setup(self, cwd: str) -> None:
        with yaspin() as loader:
            loader.text = f"Adding {self.css_type}"
            loader.color = "green"

            if self.css_type == "CSS":
                # Check if static dir exists and make style.css file
                if os.path.exists(f"{cwd}/static"):
                    os.system(f"cd {cwd}/static && touch style.css")
                # Create static dir and style.css file
                else:
                    os.system(f"mkdir static && cd {cwd}/static && touch style.css")
                
            if self.css_type == "TailwindCSS":
                # Adding TailwindCSS CDN to base.html file
                with open(f'{cwd}/templates/base.html', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in line:
                        tailwind_cdn = f'''
        <!-- Tailwind CSS -->
        <script src="https://cdn.tailwindcss.com"></script>'''
                        lines.insert(i + 1, tailwind_cdn + '\n')
                        break
                with open(f'{cwd}/templates/base.html', 'w') as file:
                    file.writelines(lines)
            if self.css_type == "Bootstrap":
                # Adding Bootstrap CDN to base.html file
                with open(f'{cwd}/templates/base.html', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in line:
                        bootstrap_cdn = f'''
        <!-- Bootstrap -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'''
                        lines.insert(i + 1, bootstrap_cdn + '\n')
                        break
                with open(f'{cwd}/templates/base.html', 'w') as file:
                    file.writelines(lines)
                # Adding Bootstrap scripts to base.html file
                with open(f'{cwd}/templates/base.html', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '<!-- Optional JavaScript -->' in line:
                        bootstrap_script = f'''
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>'''
                        lines.insert(i + 1, bootstrap_script + '\n')
                        break
                with open(f'{cwd}/templates/base.html', 'w') as file:
                    file.writelines(lines)
            else:
                pass

            loader.ok("✔")

class Ui:
    def __init__(self, ui_lib: str = "None") -> None:
        self.ui_lib = ui_lib

class Frontend:
    def __init__(self, js_cdn: str = "JS") -> None:
        self.js_cdn = js_cdn

    def js_cdn_setup(self, cwd: str) -> None:
        with yaspin() as loader:
            loader.text = f"Adding {self.js_cdn}"
            loader.color = "green"
            if self.js_cdn == "JS":
                # Check if static dir exists and make js dir
                if os.path.exists(f"{cwd}/static"):
                    os.system(f"cd {cwd}/static && mkdir js")
                # Make static dir and js dir
                else:
                    os.system(f"mkdir static && cd {cwd}/static && mkdir js")

            if self.js_cdn == "React":
                with open(f'{cwd}/templates/base.html', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in line:
                        js = '''
        <!-- React JS -->
        <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        '''
                        lines.insert(i + 1, js + '\n')
                        break
                with open(f'{cwd}/templates/base.html', 'w') as file:
                    file.writelines(lines)

                # Counter Code
                with open(f'{cwd}/templates/base.html', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '<body>' in line:
                        counter = '''        <div id="app"></div>
        <script type="text/babel">
            const Counter = () => {
                const [counter, setCounter] = React.useState(0);

                const handleIncrement = () => {
                    setCounter(counter + 1);
                };
                const handleDecreament = () => {
                    setCounter(counter - 1);
                }

                return (
                    <div class="flex-row gap-6 text-3xl">
                        <div>Counter</div>
                        <div class="pt-6 flex gap-4 p-4">
                            <button onClick={handleDecreament}> - </button>
                            <h1>{counter}</h1>
                            <button onClick={handleIncrement}> + </button>
                        </div>
                    </div>
                );
            };

            const App = () => {
                return (
                    <div class="h-screen flex items-center justify-center">
                        <Counter />
                    </div>
                );
            };
            ReactDOM.render(<App/>, document.getElementById('app'));
        </script>'''
                        lines.insert(i + 1, counter + '\n')
                        break
                with open(f'{cwd}/templates/base.html', 'w') as file:
                    file.writelines(lines)

                # Check if static dir exists and make js dir
                if os.path.exists(f"{cwd}/static"):
                    os.system(f"cd {cwd}/static && mkdir js")
                # Make static dir and js dir
                else:
                    os.system(f"mkdir static && cd {cwd}/static && mkdir js")

            if self.js_cdn == "Vue":
                with open(f'{cwd}/templates/base.html', 'r') as file:
                    lines = file.readlines()
                for i, line in enumerate(lines):
                    if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in line:
                        js = '''
        <!-- Vue JS -->
        <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
        '''
                        lines.insert(i + 1, js + '\n')
                        break
                with open(f'{cwd}/templates/base.html', 'w') as file:
                    file.writelines(lines)

                # Check if static dir exists and make js dir
                if os.path.exists(f"{cwd}/static"):
                    os.system(f"cd {cwd}/static && mkdir js")
                # Make static dir and js dir
                else:
                    os.system(f"mkdir static && cd {cwd}/static && mkdir js")

            loader.ok("✔")

class Backend:
    def __init__(self) -> None:
        pass

    def create_django_project(self) -> None:
        with yaspin() as loader:
            loader.text = "Creating a new Django Project"
            loader.color = "green"

            # Activating conda env and creating new Django project
            os.system("conda run -n web django-admin startproject core .")
            
            loader.ok("✔")
    
    def env_setup(self, cwd: str) -> None:
        with yaspin() as loader:
            loader.text = "Setting up env"
            loader.color = "green"

            os.system("touch .env")
            with open(f'{cwd}/.env', 'w') as file:
                file.writelines("DEBUG=True")
            
            # Importing environ
            with open(f'{cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if 'from pathlib import Path' in line:
                    env_import = 'import environ \n\n'
                    lines.insert(i + 1, env_import + '\n')
                    break
            with open(f'{cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)

            # Initializing ENV
            with open(f'{cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if 'BASE_DIR = Path(__file__).resolve().parent.parent' in line:
                    init_env = '''
env = environ.Env(
    DEBUG = (bool,False)
    ) \n''' + "environ.Env.read_env(BASE_DIR / '.env') \n"
                    lines.insert(i + 1, init_env + '\n')
                    break
            with open(f'{cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)

            # Using DEBUG of env
            with open(f'{cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if "DEBUG = True" in line:
                    lines[i] = "DEBUG = env('DEBUG')"
                    break
            with open(f'{cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)

            loader.ok("✔")

    def frontend_template(self, cwd: str) -> None:
        with yaspin() as loader:
            base_html = '''{% load static %}
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

        <!-- Optional JavaScript -->
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
            with open(f'{cwd}/templates/base.html', 'w') as file:
                file.writelines(base_html)
            # Adding Template files path to settings.py
            with open(f'{cwd}/core/settings.py', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                    if '"DIRS": []' in line:
                        lines[i] = '        "DIRS": [BASE_DIR / "templates"],\n'
                        break
            with open(f'{cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)

            # Adding Static files path to settings.py
            with open(f'{cwd}/core/settings.py', 'r') as file:
                    lines = file.readlines()
            for i, line in enumerate(lines):
                if '# Static files (CSS, JavaScript, Images)' in line:
                    tailwindcdn = 'STATICFILES_DIRS = [BASE_DIR / "static"]'
                    lines.insert(i + 1, tailwindcdn + '\n')
                    break
            with open(f'{cwd}/core/settings.py', 'w') as file:
                file.writelines(lines)

            loader.ok("✔")
    
    def db_menu(self) -> str:
        db_options = [ "SQLite", "MySQL", "Quit" ]
        db_menu = TerminalMenu(db_options, title= "Choose a Database")

        while not self.quitting:
            db_options_index = db_menu.show()
            db_options_choice = db = db_options[db_options_index]

            if db_options_choice == "SQLite":
                db = Database(db_type="SQLite")
                return db.db_type
            
            if db_options_choice == "MySQL":
                db = Database(db_type="MySQL")
                return db.db_type
            
            if db_options_choice == "Quit":
                self.quitting = True


class Menu:
    def __init__(self, quitting: bool = False) -> None:
        self.quitting = quitting
        self.cwd: str = os.getcwd()

    def js_cdn_menu(self) -> str:
        js_cdn_options = [ "JS", "React", "Vue", "Quit" ]
        js_cdn_menu = TerminalMenu(js_cdn_options, title= "Choose a JS CDN")

        while not self.quitting:
            js_cdn_options_index = js_cdn_menu.show()
            js_cdn_options_choice = js_cdn_options[js_cdn_options_index]

            if js_cdn_options_choice == "JS":
                frontend = Frontend()
                return frontend.js_cdn
                

            if js_cdn_options_choice == "React":
                frontend = Frontend(js_cdn="React")
                return frontend.js_cdn
                

            if js_cdn_options_choice == "Vue":
                frontend = Frontend(js_cdn="Vue")
                return frontend.js_cdn
            
            if js_cdn_options_choice == "Quit":
                self.quitting = True
            
    def css_menu(self) -> str:
        css_options = [ "CSS", "TailwindCSS", "Bootstrap", "Quit" ]
        css_menu = TerminalMenu(css_options, title= "Choose a CSS Library")

        while not self.quitting:
            css_options_index = css_menu.show()
            css_options_choice = css_options[css_options_index]

            if css_options_choice == "CSS":
                style = Style()
                return style.css_type

            if css_options_choice == "TailwindCSS":
                style = Style(css_type="TailwindCSS")
                return style.css_type
            
            if css_options_choice == "Bootstrap":
                style = Style(css_type="Bootstrap")
                return style.css_type

            if css_options_choice == "Quit":
                self.quitting = True

    def main_menu(self):
        main_options = [ "Django", "Quit" ]
        main_menu = TerminalMenu(main_options, title = "Choose a new project")

        while not self.quitting:
            main_options_index = main_menu.show()
            main_options_choice = main_options[main_options_index]

            if main_options_choice == "Quit":
                self.quitting = True
            
            if main_options_choice == "Django":
                js = self.js_cdn_menu()
                css = self.css_menu()
                db = self.db_menu()
                if self.quitting == True:
                    break
                backend = Backend()
                backend.create_django_project()
                backend.env_setup(cwd=self.cwd)
                backend.frontend_template(cwd=self.cwd)
                forntend = Frontend(js_cdn=js)
                forntend.js_cdn_setup(cwd=self.cwd)
                style = Style(css_type=css)
                style.css_setup(cwd=self.cwd)
                break
                
                
class InitializeProject:
    def run(self):
        Menu().main_menu()

if __name__ == '__main__':
    InitializeProject().run()