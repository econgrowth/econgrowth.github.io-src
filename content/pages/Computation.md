Title: Computation
Slug: Computation
Category: Computation, Dynamic Programming, IPython
date: 2016-12-29 13:53
Tags: Computation, IPython
Author: Ömer Özak

We will be using (I)Python as our programming language and QGIS for basic GIS exploration. In order to use some of the material available on this website and to share your material with others you should create a [<i class="fa fa-github fa-1x"></i>GitHub](http://github.com/) account for yourself. This will be useful to you in the future to keep track of changes when you are writing papers. I also recommend creating a [<i class="fa fa-bitbucket fa-1x"></i>Bitbucket](https://bitbucket.org/) account, which has similar functionality, but allows you to have unlimited private repositories for personal use. Additionally, I suggest you read [Gentzkow & Shapiro's *Code and Data for the Social Sciences: A Practitioner’s Guide*](https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf) to familiarize yourself with good practices in coding and statistical analysis. We will cover additional topics in class.

---
#MacOS
###Homebrew
On ``MacOS`` you can use [Homebrew](https://brew.sh/), which is an excellent tool for installing all kinds of open source software. First, download and install XCode (from the Apple store) and command line tools (option within XCode or in a terminal execute ``xcode-select --install``). Second, install ``Homebrew``

	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	
Third, install some of the software we will use, including ``qgis``, ``MacTeX``, ``R``, ``Rstudio``

	brew tap osgeo/osgeo4mac
	brew cask install qgis
	brew cask install mactex
	brew install r
	brew cask install rstudio

There are many tools that can be installed via ``Homebrew`` whenever needed. Try it out!

###iTerm2
I highly recommend using [iTerm2](https://www.iterm2.com/) instead of the terminal that comes with ``OSX``. It is custumizable and very powerful. 

---
#Installing QGIS
Download and install QGIS from their [website](https://qgis.org/en/site/forusers/download.html). 

---
#Text Editor

You should have a good text editor, which hopefully has syntax highlighting for various languages, especially for ``python``, ``R`` and ``Stata``. I personally recommend [atom](https://atom.io/), which is free, custimizable and very flexible.

---
#LaTeX/LyX

Install the ``LaTeX`` distribution for your system from the [LaTeX website](https://www.latex-project.org/get/#tex-distributions). If ``LyX`` is not installed with your distribution and you want to use a WSIWYG front for ``LaTeX``, download and install [LyX here](https://www.lyx.org/Download).

---
#Stata Packages

It is useful to keep a list your Stata packages in case you need to reinstall or replicate your environment somewhere else. For this you can use ``adolist``

	net install adolist, from(http://fmwww.bc.edu/RePEc/bocode/a)
	
To create a list of your packages

	 adolist store mystatapacks_latest.pkl
	 
To install the packages from the list

	adolist install mystatapacks_latest.pkl
	
You can update an existing list by

	 adolist update mystatapacks_latest.pkl
	 
[Here](https://www.dropbox.com/s/ryrskg415wkvyj5/mystatapacks_latest.pkl?dl=0) is my latest ``mystatapacks_latest.pkl`` in case you want to have some useful packges installed.

---
#Installing (I)Python & Jupyter
The easiest and most convenient way to install a working version of IPython with all the required packages and tools is using [Continuum's Anaconda Distribution](https://www.anaconda.com/distribution/). You can install following the instructions in that website, or if you can just run [this script (Mac/Linux)](https://www.dropbox.com/s/6st528ethbkmvv2/CondaInstall.sh?dl=0). After installing the latest version of Anaconda, add the ``Anaconda/bin`` directory to your ``PATH`` variable. 

In Windows you may need to install [Visual C++ 9.0](https://www.microsoft.com/en-us/download/details.aspx?id=44266), [Visual C++ 14](https://msdn.microsoft.com/en-us/library/hh567368.aspx) and [Microsoft MPI6](https://www.microsoft.com/en-us/download/details.aspx?id=47259). 

In ``MACOS`` download and install XCode (from the Apple store) and command line tools (option within XCode or in a terminal execute ``xcode-select --install``).

Since the basic installation may not have all the packages you need and it is always best to keep an environment for your work, after installation:

A. **(Recommended)** In a terminal window execute

	conda create --name GeoPython37env -c conda-forge -c numba -c rapidsai -c mro -c r -c defaults python=3.7 asciitree autopep8 babel basemap beautifulsoup4 blas blaze bokeh bzip2 cartopy colorcet curl cython cytoolz dask dask-core datashader datashape descartes dill docutils earthengine-api fiona gcc gensim geographiclib geopandas geoplot geopy geotiff google-api-python-client google-auth google-auth-httplib2 georasters imageio imagesize ipykernel ipyparallel ipython ipython_genutils ipywidgets jupyter jupyterlab kiwisolver matplotlib markdown networkx nose numba numpy openpyxl pandas pandas-datareader pandasql pandoc pandocfilters pandana pelican pycountry pymc3 pysal python.app urbanaccess r rstudio r-irkernel  statsmodels sympy rpy2 rasterio r-tidyr r-tibble r-dplyr rise seaborn scikit-allel scikit-bio scikit-image scikit-learn scipy seaborn swifter theano unidecode urllib3 wikipedia xlrd jupyter_contrib_nbextensions

	conda activate GeoPython37env
	pip install linearmodels isounidecode geonamescache geocoder git+https://github.com/jeetsukumaran/DendroPy.git git+https://github.com/dmsul/econtools ecopy facebook-business facebook-sdk fontawesome-markdown geocoder geonamescache googledrivedownloader googletrans ipystata isodate isounidecode latexcodec ldpred linearmodels lingpy mccabe ordered-set plinkio pyarrow pybtex pycldf pycountry pydocstyle pyface pyflakes pylatex pyparsing pyreadstat pytest-cov python-jsonrpc-server python-language-server pytrends quilt ratelim readme-renderer rfc3986 rope simpledbf simplejson smartypants snowballstemmer snuggs stata-kernel tabulate tex2ipy texsoup toolz traits traitsui twine typogrify uritemplate w3lib webencodings wrapt xlwt yapf modin stargazer covid COVID19Py
	
	python -m stata_kernel.install
	conda install -c conda-forge nodejs -y
	jupyter labextension install jupyterlab-stata-highlight
	ipcluster nbextension enable
	jupyter contrib nbextension install --sys-prefix
	jupyter nbextension enable nbTranslate/main

This should create an environment with most of the packages we need. We can always install others down the road.

B. **(Not recommended)** download one of the following scripts 

* [Latest](https://www.dropbox.com/s/xousjyaegz8px9c/latest_conda_env.yml?dl=0)
* [GeoPython35env](https://www.dropbox.com/s/d79ahsu3xz4632g/GeoPython3env2019B_nobuilds.yml?dl=0) (older Python 3.5 environment)
* [GeoPython3env old](https://www.dropbox.com/s/38a7mcaziyzmovj/GeoPython3env.yml?dl=0)  (older Python 3 environment)
* [GeoPython2env](https://www.dropbox.com/s/mrr9qwyz7t6s2uu/GeoPython2env.yml?dl=0) (older Python 2 environment)

and execute

    conda update conda
    conda-env create -f GeoPython3env2019B_nobuilds.yml
    # Or uncomment one of these if you want to install the older versions
    #conda-env create -f GeoPython2env.yml
    #conda-env create -f GeoPython3env.yml

####MacOS
Instead of the previous options, you can download [this file](https://www.dropbox.com/s/8hz368xsh48390i/GeoPython3env-spec-file.txt?dl=0) and execute

	conda create --name GeoPython3env --file GeoPython3env-spec-file.txt
    
###After Installation is complete

This should create an environment with all the packages you will require for this course (and more!). 

To start using one of the environment you will need to exectute the following command

    source activate GeoPython37env

or for ``Python 2.x``

    source activate GeoPython2env

I would suggest using ``GeoPython37env``, since it is the latest and most up-to-date version (I'll try to keep adding new versions as time passes).

##Parallel Computing
One of the advantages of ``Jupyter Notebooks`` is that they allow you to work (very easily) with multiple processors using ``ipyparallel``. Once you have ``ipyparallel`` installed (automatically done for you with the scritps above), you will need to execute the following code once

    ipcluster nbextension enable

## Stata Kernel
We can use ``Stata`` within Jupyter Notebooks with the [Stata kernel](https://kylebarron.dev/stata_kernel/). I recommend you make sure it is installed and you have highlighting. To install (in case you do not use the ``YAML`` environment file above), execute

	pip install stata_kernel
	python -m stata_kernel.install

and then 

	conda install -c conda-forge nodejs -y
	jupyter labextension install jupyterlab-stata-highlight

## R kernel
We can also use ``R`` within Jupyter Notebooks with the [R kernel](https://irkernel.github.io/). The best way to install it (in case you do not use the ``YAML`` environment file above) is to use ``conda`` by executing

	conda install -c conda-forge -c r r-irkernel 

You can also install ``R`` and ``R`` packages by using ``conda``. Simply execute

	conda install -c conda-forge -c r r
	conda install -c conda-forge -c r r-PACKAGE_NAME

## Running Stata or R in Python
We can also use ``Stata`` or ``R`` directly within ``Python``. You only need to use the ``%magic`` for each after installing the required packages. For example for ``Stata`` you need  [``ipystata``](https://github.com/TiesdeKok/ipystata). Install by executing

	pip install ipystata
	
Then in ``jupyter`` execute

	import ipystata 
	from ipystata.config import config_stata
	config_stata('Path to your Stata executable')  

Once configured you can use the ``%%stata`` magic. E.g.

	In[1]: import ipystata  
	In[2]: %%stata  
   		    display "Hello, I am printed in Stata."  
	

More info in the [``ipystata`` website](https://github.com/TiesdeKok/ipystata).

Similarly, we can use ``R`` using [``rpy2``](https://rpy2.bitbucket.io/). Install by executing

	conda install -c conda-forge -c r rpy2
	
Then in jupyter execute

	In [1]: %load_ext rpy2.ipython
	In [2]: %%R

			R.version

More info in the [``rpy2`` website](https://rpy2.bitbucket.io/).

---
#Notebooks

* Notebook 1: Introduction [(html)](/IntroPython.html) [(ipynb)](/notebooks/IntroPython.ipynb)
* Notebook 2: Dynamic Programming in Python [(html)](/Dynamic Programming.html) [(ipynb)](/notebooks/DynamicProgramming.ipynb)
* Notebook 3: Faster Dynamic Programming with Numba [(html)](/Dynamic Programming Numba.html) [ipynb](Faster Computation with Numba.ipynb)
* Notebook 4: Economic Data Analysis [(html)](/Economic Data Analysis.html) [(ipynb)](/notebooks/EconomicDataAnalysis.ipynb)
* Notebook 5: GIS with QGIS [(html)](/GIS with QGIS.html) [(ipynb)](/notebooks/GIS.ipynb)
* Notebook 6: GIS with Python [(html)](/GIS with Python.html) [(ipynb)](/notebooks/GIS with Python.ipynb)
* Notebook 7: 
