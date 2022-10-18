__version__ = '0.0.1'

from .app import JupJs9App

# Main js9 server to serve the html page
# initialized from pyproject.toml
def js9_main_server():
    return {
        'command': ['python', '-m', 'http.server', '-d', '/opt/js9-web', '{port}'],
        'launcher_entry': {
            'enabled': True,
            'title': 'JS9'
        }}

# Server side helpers to support external communication with JS9 
# (via the shell and Python) and handle the display of large files.
# See: https://js9.si.edu/js9/help/helper.html
# initlizaed from pyproject.toml
def js9_helper_server():
    return {
        'command': ['bash', '-c', 'node /opt/js9-web/js9Helper.js'],
        'port': 2718,
        'launcher_entry': {
           'enabled': False,
        }}
    

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