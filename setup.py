from setuptools import setup
import os

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
  name = 'py-AutoCleanRe',         
  packages = ['AutoClean'],   
  version =  'v1.1.4',      
  license='MIT',        
  description = 'AutoClean - Python Package for Automated Preprocessing & Cleaning of Datasets', 
  long_description=long_description,
  long_description_content_type='text/markdown',
  keywords = ['automated', 'cleaning', 'preprocessing', "autoclean"],  
  install_requires=[          
          'scikit-learn',
          'numpy',
          'pandas',
          'loguru'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',   
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',    
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
