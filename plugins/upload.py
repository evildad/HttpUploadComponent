from sleekxmpp.xmlstream import ElementBase, ET, JID, register_stanza_plugin
from sleekxmpp import Iq
from sleekxmpp.plugins.base import base_plugin
from sleekxmpp.xmlstream.handler.callback import Callback
from sleekxmpp.xmlstream.matcher.xpath import MatchXPath

class upload(base_plugin):

    def plugin_init(self):
        self.description = "upload files via http"
        self.xep = "0999"
        self.xmpp['xep_0030'].add_feature("eu:siacs:conversations:http:upload")
        self.xmpp.register_handler(
            Callback('Upload request',
                MatchXPath('{%s}iq/{eu:siacs:conversations:http:upload}request' % self.xmpp.default_ns),
                self._handleUpload))
        register_stanza_plugin(Iq, UploadRequest)
        register_stanza_plugin(Iq, UploadSlot)


    def _handleUpload(self, iq):
        if iq['type'] == 'get':
            self.xmpp.event('request_upload_slot',iq)


class UploadRequest(ElementBase):
    namespace = "eu:siacs:conversations:http:upload"
    name = "request"
    plugin_attrib = "request"
    interfaces = set(('size','filename'))
    sub_interfaces = interfaces

class UploadSlot(ElementBase):
    namespace = "eu:siacs:conversations:http:upload"
    name = "slot"
    plugin_attrib = "slot"
    interfaces = set(('put','get'))
    sub_interfaces = interfaces
