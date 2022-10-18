
from jupyter_server.auth import authorized
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerJinjaMixin,
    ExtensionHandlerMixin,
)
from jupyter_server.utils import url_escape


class DefaultHandler(ExtensionHandlerMixin, JupyterHandler):
    auth_resource = "jupjs9:default"

    @authorized
    def get(self):
        # The name of the extension to which this handler is linked.
        self.log.info(f"Extension Name in {self.name} Default Handler: {self.name}")
        # A method for getting the url to static files (prefixed with /static/<name>).
        self.log.info(
            "Static URL for / in jupjs9 Default Handler: {}".format(self.static_url(path="/"))
        )
        self.write("<h1>Hello Simple 1 - I am the default...</h1>")
        self.write(f"Config in {self.name} Default Handler: {self.config}")
