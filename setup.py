import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='md-toc-creator',  
     version='1.4',
     author="Michael Connor Buchan",
     author_email="mikeybuchan@hotmail.co.uk",
     description="Generates a table of contents for a markdown document in markdown.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/mcb2003/md-toc-creator",
     packages=setuptools.find_packages(),
     entry_points={
         "console_scripts": [
             "md-toc = mdtoc:main"
             ]
         },
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GPL License",
         "Operating System :: OS Independent",
     ],
 )
