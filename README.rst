Flask插件for HttpBasicAuth client
==================================

对requests库的包装，自动组装base_url, HttpBasicAuth


安装
------

.. code-block:: sh

    pip install Flask-Auth-Client

Usage
-----


First init::

    from flask_auth_client import AuthClient
    auth_client = AuthClient()
    auth_client.init_app(app)

API
---

.. code-block::

    params = {}
    resp = auth_client.request('GET', '/users/', params=params)
    resp = auth_client.get('/users', params=params)



配置项
------

====================    ================================================
配置项                  说明
====================    ================================================
AUTH_CIENT_BASE_URL     api的url_prefix
AUTH_CIENT_USERNAME     BasicAuth的username
AUTH_CIENT_PASSWORD     BasicAuth的password
AUTH_CIENT_VERIFY       requests的verfy配置，可以是自定义证书的路径
====================    ================================================
