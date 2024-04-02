from distutils.core import setup

REQUIRES = [
    'allure-pytest',
    'requests',
    'pydantic'

]

setup(
    name='dm_api_account',
    version='1.1.1',
    packages=['dm_api_account', 'dm_api_account.apis', 'dm_api_account.models'],
    url='https://github.com/katyakorsa/dm_api_account.git',
    license='MIT',
    author='Ekaterina Korsakova',
    author_email='',
    install_requires=REQUIRES,
    description='DM_API_Account service with logging and allure'
)
