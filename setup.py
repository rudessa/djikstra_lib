from setuptools import setup

setup(
   name='djikstra_lib000',
   version='1.1',
   description='about djikstra. github: https://github.com/rudessa/djikstra_lib',
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