from setuptools import setup

setup(
   name='djikstra_liben',
   version='1.0',
   description='about djikstra.',
   long_description=' github: https://github.com/rudessa/djikstra_lib',
   license='MIT',
   author='Svetlana Rudova',
   author_email='rudovasvetlana570@gmail.com',
   url='https://github.com/rudessa/djikstra_lib',
   packages=['djikstra'],
   install_requires=[], 
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)