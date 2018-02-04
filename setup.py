from setuptools import setup

setup(
    name='shop',
    packages=['shop'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-Alchemy',
        'Flask-Migrate',
        'psycopg2',
        'flask-login',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
