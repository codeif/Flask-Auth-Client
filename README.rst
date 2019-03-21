HttpBaseAuth client extension for Flask.
===========================================

对requests库的包装，自动组装base_url, HttpBasicAuth。


安装
------

.. code-block:: sh

    pip install Flask-Auth-Client

使用
------


First init::

    from flask_auth_client import AuthClient
    auth_client = AuthClient()
    auth_client.init_app(app)

API
----

需要注意的是 url = base_url + path，所以base_url和path需要用户自己做好处理。

.. code-block::

    params = {}
    resp = auth_client.request('GET', '/users/', params=params)
    resp = auth_client.get('/users', params=params)



配置项
------

可以在构造方法修改配置前缀，默认为 AUTH_CLIENT

.. code-block:: py

    auth_client = AuthClient(config_prefix='CUSTOM_PREFIX')


=====================   ================================================
配置项                  说明
=====================   ================================================
AUTH_CLIENT_BASE_URL     api的url_prefix
AUTH_CLIENT_USERNAME     BasicAuth的username
AUTH_CLIENT_PASSWORD     BasicAuth的password
AUTH_CLIENT_VERIFY       requests的verfy配置，可以是自定义证书的路径
=====================   ================================================
