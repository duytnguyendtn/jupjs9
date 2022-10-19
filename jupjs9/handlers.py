
from jupyter_server.auth import authorized
from jupyter_server.base.handlers import JupyterHandler, FileFindHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerJinjaMixin,
    ExtensionHandlerMixin,
)
from jupyter_server.utils import url_escape
import tornado


class RedirectHandler(ExtensionHandlerMixin, JupyterHandler):
    @tornado.web.authenticated
    def get(self):
        self.redirect(f'{self.name}/')


class JupJS9Handler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler):
    @tornado.web.authenticated
    def get(self, jid='JS9'):
        self.write(self.render_template("index.html", jid=jid))