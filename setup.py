from setuptools import setup

setup(
    name='shop',
    version='0.1',
    packages=['shop'],
    include_package_data=True,
    install_requires=[
        'flask>=0.12',
        'Flask-SQLAlchemy>=2.3',
        'Flask-Migrate',
        'psycopg2',
        'passlib',
        'itsdangerous',
        'Flask-HTTPAuth',
        'flask-cors',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest>=3.4',
        'selenium',
    ],
)
