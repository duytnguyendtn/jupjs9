
from jupyter_server.auth import authorized
from jupyter_server.base.handlers import JupyterHandler, FileFindHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerJinjaMixin,
    ExtensionHandlerMixin,
)
from jupyter_server.utils import url_escape
import tornado


class DefaultHandler(ExtensionHandlerMixin, JupyterHandler):
    auth_resource = "jupjs9:default"

    @tornado.web.authenticated
    def get(self):
        # The name of the extension to which this handler is linked.
        self.log.info(f"Extension Name in {self.name} Default Handler: {self.name}")
        # A method for getting the url to static files (prefixed with /static/<name>).
        self.log.info(
            "Static URL for / in jupjs9 Default Handler: {}".format(self.static_url(path="/"))
        )
        self.write("<h1>Hello Simple 1 - I am the default...</h1>")
        self.write(f"Config in {self.name} Default Handler: {self.config}")

        
class ParameterHandler(ExtensionHandlerMixin, JupyterHandler):
    @tornado.web.authenticated
    def get(self, js9ID=None, *args, **kwargs):
        #var1 = self.get_argument("var1", default='None')
        components = [x for x in self.request.path.split("/") if x]
        self.write("<h1>Hello Simple App 1 from Handler.</h1>")
        self.write(f"<p>js9ID: {url_escape(js9ID)}</p>")
        #self.write(f"<p>var1: {url_escape(var1)}</p>")
        self.write(f"<p>components: {components}</p>")
        

class BaseTemplateHandler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler):
    pass


class TemplateHandler(BaseTemplateHandler):
    @tornado.web.authenticated
    def get(self, jid='JS9'):
        """Optionally, you can print(self.get_template('simple1.html'))"""
        self.write(self.render_template("index.html", jid=jid))