import xadmin
from DjangoUeditor import settings
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from xadmin.views import BaseAdminPlugin, UpdateAdminView, CreateAdminView


class XadminUEditorWidget(UEditorWidget):
    """
    富文本组件
    """

    def __init__(self, **kwargs):
        self.ueditor_options = kwargs
        self.Media.js = None
        super().__init__(kwargs)


class UeditorPlugin(BaseAdminPlugin):
    """
    富文本插件
    """
    def get_field_style(self, attrs, db_field, style, **kwargs):
        if style == 'ueditor':
            if isinstance(db_field, UEditorField):
                widget = db_field.formfield().widget
                params = {}
                params.update(widget.ueditor_settings)
                params.update(widget.attrs)
                return {'widget': XadminUEditorWidget(**params)}
        return attrs

    def block_extra_head(self, context, nodes):
        js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")
        nodes.append(js)


xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)