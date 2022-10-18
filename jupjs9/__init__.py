__version__ = '0.0.1'

from .app import JupJs9App

appentry = launch_new_instance = JupJs9App.launch_instance
    

def _jupyter_server_extension_points():
    """
    Returns a list of dictionaries with metadata describing
    where to find the `_load_jupyter_server_extension` function.
    """
    return [
        {
            "module": "jupjs9",
            "app": JupJs9App
        }
    ]