import os
from pathlib import Path

from traitlets import Unicode

from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin

from .handlers import (
    JupJS9Handler,
    FileFindHandler,
    RedirectHandler,
)

JS9_FORK_PATH = Path("E:\HEASARC\gitrepos\scieserver-js9\js9-fork")

DEFAULT_STATIC_FILES_PATH = str(JS9_FORK_PATH)#'/opt/js9-web/'
DEFAULT_TEMPLATE_FILES_PATH = str(JS9_FORK_PATH)#'/opt/js9-web/'


class JupJs9App(ExtensionAppJinjaMixin, ExtensionApp):

    # The name of the extension.
    name = "js9"

    # The url that your extension will serve its homepage.
    extension_url = "/js9"

    # Should your extension expose other server extensions when launched directly?
    load_other_extensions = True

    # Local path to static files directory.
    static_paths = [DEFAULT_STATIC_FILES_PATH]

    # Local path to templates directory.
    template_paths = [DEFAULT_TEMPLATE_FILES_PATH]

    def initialize_handlers(self):
        self.handlers.extend(
            [
                # serve JS9
                (rf"/{self.name}", RedirectHandler),
                (rf"/{self.name}/([0-9a-zA-Z]+)?$", JupJS9Handler),
                
                # serve files
                (rf"/{self.name}/(.*)", FileFindHandler, {"path": DEFAULT_STATIC_FILES_PATH}),
            ]
        )

    def initialize_settings(self):
        self.log.info(f"Config {self.config}")
