from setuptools import setup

setup(
    name = 'mango-cli',
    version = '0.0.1',
    packages = ['cli', 'cli.commands'],
    include_package_data = True,
    install_requires = [
        'click',
    ],
    entry_points = """
        [console_scripts]
        mangoctl=cli.cli:cli
        """,
)
