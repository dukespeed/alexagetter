from setuptools import setup

setup(
    name='Danielinator',
    version='0.0.2',
    packages=['venv.Lib.site-packages.pip', 'venv.Lib.site-packages.pip._vendor',
              'venv.Lib.site-packages.pip._vendor.idna', 'venv.Lib.site-packages.pip._vendor.pep517',
              'venv.Lib.site-packages.pip._vendor.pytoml', 'venv.Lib.site-packages.pip._vendor.certifi',
              'venv.Lib.site-packages.pip._vendor.chardet', 'venv.Lib.site-packages.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip._vendor.distlib', 'venv.Lib.site-packages.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip._vendor.msgpack', 'venv.Lib.site-packages.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip._vendor.urllib3.util', 'venv.Lib.site-packages.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.rfc3986',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip._vendor.colorama', 'venv.Lib.site-packages.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treebuilders', 'venv.Lib.site-packages.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip._vendor.progress', 'venv.Lib.site-packages.pip._vendor.requests',
              'venv.Lib.site-packages.pip._vendor.packaging', 'venv.Lib.site-packages.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip._vendor.webencodings', 'venv.Lib.site-packages.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip._internal', 'venv.Lib.site-packages.pip._internal.cli',
              'venv.Lib.site-packages.pip._internal.req', 'venv.Lib.site-packages.pip._internal.vcs',
              'venv.Lib.site-packages.pip._internal.utils', 'venv.Lib.site-packages.pip._internal.models',
              'venv.Lib.site-packages.pip._internal.commands', 'venv.Lib.site-packages.pip._internal.operations',
              'venv.Lib.site-packages.pip._internal.distributions', 'venv.Lib.site-packages.PyQt5',
              'venv.Lib.site-packages.PyQt5.uic', 'venv.Lib.site-packages.PyQt5.uic.Loader',
              'venv.Lib.site-packages.PyQt5.uic.port_v2', 'venv.Lib.site-packages.PyQt5.uic.port_v3',
              'venv.Lib.site-packages.PyQt5.uic.Compiler', 'venv.Lib.site-packages.urllib3',
              'venv.Lib.site-packages.urllib3.util', 'venv.Lib.site-packages.urllib3.contrib',
              'venv.Lib.site-packages.urllib3.contrib._securetransport', 'venv.Lib.site-packages.urllib3.packages',
              'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.selenium',
              'venv.Lib.site-packages.selenium.common', 'venv.Lib.site-packages.selenium.webdriver',
              'venv.Lib.site-packages.selenium.webdriver.ie', 'venv.Lib.site-packages.selenium.webdriver.edge',
              'venv.Lib.site-packages.selenium.webdriver.opera', 'venv.Lib.site-packages.selenium.webdriver.chrome',
              'venv.Lib.site-packages.selenium.webdriver.common',
              'venv.Lib.site-packages.selenium.webdriver.common.html5',
              'venv.Lib.site-packages.selenium.webdriver.common.actions',
              'venv.Lib.site-packages.selenium.webdriver.remote', 'venv.Lib.site-packages.selenium.webdriver.safari',
              'venv.Lib.site-packages.selenium.webdriver.android', 'venv.Lib.site-packages.selenium.webdriver.firefox',
              'venv.Lib.site-packages.selenium.webdriver.support',
              'venv.Lib.site-packages.selenium.webdriver.phantomjs',
              'venv.Lib.site-packages.selenium.webdriver.webkitgtk',
              'venv.Lib.site-packages.selenium.webdriver.blackberry', 'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.idna',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.certifi',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.req',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.vcs',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.utils',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.models',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.commands',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.operations'],
    url='https://github.com/dukespeed/alexagetter',
    license='',
    author='Duke Speed',
    author_email='',
    description='Attempts to get commands from alexa through a web browser.'
)