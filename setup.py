
from os import path
import setuptools, datetime
from setuptools import find_packages
NAME = "dplc"
today = datetime.date.today().strftime("%b-%d-%Y")
with open(path.join('dplc', '_date.py'), 'w') as fp :
    fp.write('date = \'%s\'' % today)
install_requires=["pytest", "pytest-xdist"]

def setup(scm=None):
    packages = find_packages()

    setuptools.setup(
        name=NAME,
        use_scm_version=scm,
        setup_requires=['setuptools_scm'],
        author="Yuzhi Zhang, et al.",
        author_email="zhangyz@dp.tech",
        description="Algorithm Engineering tutorial for the DPLC team.",
        url="https://github.com/AnguseZhang/AlgorithmEngineering",
        python_requires="~=3.8",
        packages=packages,
        keywords='AlgorithmEngineering',
        install_requires=install_requires,
        entry_points={'console_scripts': ['dplc= dplc.main:main']}
    )
try:
    setup(scm={'write_to': 'dplc/_version.py'})
except:
    setup(scm=None)

