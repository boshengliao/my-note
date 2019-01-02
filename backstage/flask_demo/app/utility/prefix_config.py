# -*- coding: utf-8 -*-

from werkzeug.wsgi import DispatcherMiddleware


class PrefixConfig(object):
    """url前缀的配置
    """
    def init_app(self, app):
        """根据app.config['APP_URL_PREFIX']设置url前缀.
        """
        prefix = app.config.get('APP_URL_PREFIX', '')
        if not prefix:
            return None
        app.config["APPLICATION_ROOT"] = prefix
        v0 = self._simple
        v1 = {prefix: app.wsgi_app}
        app.wsgi_app = DispatcherMiddleware(v0, v1)
        return None

    def _simple(self, env, resp):
        resp('200 OK', [('Content-Type', 'text/plain')])
        return [b'Hello WSGI World']
