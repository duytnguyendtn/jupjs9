import os

from traitlets import Unicode

from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin

from .handlers import (
    DefaultHandler,
    #ErrorHandler,
    ParameterHandler,
    #RedirectHandler,
    TemplateHandler,
    #TypescriptHandler,
)

DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "templates")
DEFAULT_TEMPLATE_FILES_PATH = os.path.join(os.path.dirname(__file__), "templates")


class JupJs9App(ExtensionAppJinjaMixin, ExtensionApp):

    # The name of the extension.
    name = "jupjs9"

    # The url that your extension will serve its homepage.
    extension_url = "/jupjs9/default"

    # Should your extension expose other server extensions when launched directly?
    load_other_extensions = True

    # Local path to static files directory.
    static_paths = [DEFAULT_STATIC_FILES_PATH]

    # Local path to templates directory.
    template_paths = [DEFAULT_TEMPLATE_FILES_PATH]

    def initialize_handlers(self):
        self.handlers.extend(
            [
                (rf"/{self.name}/?", DefaultHandler),
                (rf"/{self.name}/params/(.+)$", ParameterHandler),
                (rf"/{self.name}/t1/(.*)$", TemplateHandler),
                #(rf"/{self.name}/redirect", RedirectHandler),
                #(rf"/{self.name}/typescript/?", TypescriptHandler),
                #(rf"/{self.name}/(.*)", ErrorHandler),
            ]
        )

    def initialize_settings(self):
        self.log.info(f"Config {self.config}")
