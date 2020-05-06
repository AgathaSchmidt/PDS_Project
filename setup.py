from setuptools import setup

setup(
    name='pds',
    version='0.0.1dev1', install_requires=['pandas', 'scikit-learn', 'Click'],
    description='Programming Data Science',
    author='Agatha Schmidt',
    author_email='agatha.schmidt@hotmail.de',
    packages=['pds', 'data'],
    install_requirements=['conda'],
    #entry_points='''
     #   [console_scripts]
      #  model=pds.model:cli:main
       # prepare=pds.prepare:cli:column_info
    
   # ''',

     entry_points={
     'console_scripts': ['pds=pds.cli:main']
     }
)
