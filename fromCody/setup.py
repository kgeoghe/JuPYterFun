from setuptools import setup
dependencies = 'numpy bokeh jupyter ipywidgets'.split()

setup(
    name='jupyter-bokeh-ipywidgets-examples',
    description='Examples of data visualization in a Jupyter notebook',
    install_requires=dependencies,
)
