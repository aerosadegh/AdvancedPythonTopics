from setuptools import setup, find_packages  # type: ignore


setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(),
    # CLI
    entry_points = {
        'console_scripts': [
            'foo = mypackage.main:main',
        ],
    }
)
