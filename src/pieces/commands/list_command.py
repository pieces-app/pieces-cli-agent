from pieces.settings import Settings
from collections.abc import Iterable
from pieces.assets import check_assets_existence, AssetsCommandsApi
from pieces_os_client.api.applications_api import ApplicationsApi
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.styles import Style
from typing import List, Tuple

class PiecesSelectMenu:
    def __init__(self, menu_options: List[Tuple]):
        self.menu_options = menu_options
        self.current_selection = 0
        self.selected_index = None
    
    def get_menu_text(self):
        result = []
        for i, option in enumerate(self.menu_options):
            if i == self.current_selection:
                result.append(('class:selected', f'> {option[0]}\n'))
            else:
                result.append(('class:unselected', f'  {option[0]}\n'))
        return result

    def run(self):
        bindings = KeyBindings()

        @bindings.add('up')
        def move_up(event):
            if self.current_selection > 0:
                self.current_selection -= 1
            event.app.layout.focus(self.menu_window)

        @bindings.add('down')
        def move_down(event):
            if self.current_selection < len(self.menu_options) - 1:
                self.current_selection += 1
            event.app.layout.focus(self.menu_window)

        @bindings.add('enter')
        def select_option(event):
            self.selected_index = self.current_selection
            event.app.exit()

        menu_control = FormattedTextControl(text=self.get_menu_text)
        self.menu_window = Window(content=menu_control, always_hide_cursor=True)
        layout = Layout(HSplit([self.menu_window]))
        style = Style.from_dict({
            'selected': 'reverse',
            'unselected': ''
        })
        app = Application(layout=layout, key_bindings=bindings, style=style, full_screen=True)
        app.run()

        return self.selected_index


class ListCommand:
    selected_item = None

    @classmethod
    def select_command(cls, **kwargs):
        type = kwargs.get("type", "assets")
        max_assets = kwargs.get("max_assets", 10)
        if max_assets < 1:
            print("Max assets must be greater than 0")
            max_assets = 10
        
        if type == "assets":
            cls.select_assets(max_assets)
        elif type == "apps":
            cls.select_apps()
        elif type == "models":
            cls.select_models()
    @staticmethod
    def list_models():
        for idx,model_name in enumerate(Settings.models,start=1):
            print(f"{idx}: {model_name}")
        print(f"Currently using: {Settings.model_name} with uuid {Settings.model_id}")

    @staticmethod
    def list_apps():
        # Get the list of applications
        
        applications_api = ApplicationsApi(Settings.api_client)

        application_list = applications_api.applications_snapshot()
        # Check if the application_list object has an iterable attribute and if it is an instance of Iterable
        if hasattr(application_list, 'iterable') and isinstance(application_list.iterable, Iterable):
            # Iterate over the applications in the list
            for i, app in enumerate(application_list.iterable, start=1):
                # Get the name of the application, default to 'Unknown' if not available
                app_name = getattr(app, 'name', 'Unknown').value if hasattr(app, 'name') and hasattr(app.name, 'value') else 'Unknown'
                # Get the version of the application, default to 'Unknown' if not available
                app_version = getattr(app, 'version', 'Unknown')
                # Get the platform of the application, default to 'Unknown' if not available
                app_platform = getattr(app, 'platform', 'Unknown').value if hasattr(app, 'platform') and hasattr(app.platform, 'value') else 'Unknown'
                    
                # Print the application details
                print(f"{i}: {app_name}, {app_version}, {app_platform}")
        else:
            # Print an error message if the 'Applications' object does not contain an iterable list of applications
            print("Error: The 'Applications' object does not contain an iterable list of applications.")
    
    @staticmethod
    @check_assets_existence
    def list_assets(max_assets:int=10):
        assets_snapshot = AssetsCommandsApi().assets_snapshot
        for i, uuid in enumerate(list(assets_snapshot.keys())[:max_assets], start=1):
            asset = assets_snapshot[uuid]
            if not asset:
                asset = AssetsCommandsApi.get_asset_snapshot(uuid)
            print(f"{i}: {asset.name}")
