
from setuptools import setup

setup (
    name = 'pip_install_test_wukunhuan', 
    version = '1.0', 
    description = 'Testing pip install from GitHub', 
    author = 'wukunhuan', 
    author_email = 'u3577163@connect.hku.hk', 
    url = 'https://github.com/WuKunhuan/pip_install_test_wukunhuan', 
    packages = [
        'pip_install_test_wukunhuan'
    ], 
    entry_points = {
        'entry': [
            'pip_install_test_wukunhuan = pip_install_test_wukunhuan.module:main'
        ]
    }, 
    install_requiries = [

    ]
)

