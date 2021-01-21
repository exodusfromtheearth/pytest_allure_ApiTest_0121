conftest.py文件写在了根目录，
(1）放置了配置参数的方法pytest_addoption（2）登录方法和获取Token的方法

pytest.ini文件是一些基础参数配置，
通过pytestconfig可以全局调用，例如：
def test(pytestconfig):
    # 读取ini配置信息
    host_url = pytestconfig.getini('host_url')
   