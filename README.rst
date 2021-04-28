====================================
openclean - Data Cleaning for Python
====================================

.. image:: https://img.shields.io/pypi/pyversions/openclean.svg
    :target: https://pypi.org/pypi/openclean

.. image:: https://badge.fury.io/py/openclean.svg
    :target: https://badge.fury.io/py/openclean

.. image:: https://img.shields.io/badge/License-BSD-green.svg
    :target: https://github.com/VIDA-NYU/openclean/blob/master/LICENSE


.. figure:: https://github.com/VIDA-NYU/openclean/blob/master/docs/graphics/logo.png
    :align: center
    :alt: openclean Logo


About
=====

**openclean** is a Python library for data profiling and data cleaning. The project is motivated by the fact that data preparation is still a major bottleneck for many data science projects. Data preparation requires profiling to gain an understanding of data quality issues, and data manipulation to transform the data into a form that is fit for the intended purpose.

While a large number of different tools and techniques have previously been developed for profiling and cleaning data, one main issue that we see with these tools is the lack of access to them in a single (unified) framework. Existing tools may be implemented in different programming languages and require significant effort to install and interface with. In other cases, promising data cleaning methods have been published in the scientific literature but there is no suitable codebase available for them. We believe that the lack of seamless access to existing work is a major contributor to why data preparation is so time consuming.

The goal of **openclean** is to bring together data cleaning tools in a single environment that is easy and intuitive to use for a data scientist. **openclean** allows users to compose and execute cleaning pipelines that are built using a variety of different tools. We aim for **openclean** to be flexible and extensible to allow easy integration of new functionality. To this end, we define a set of primitives and API’s for the different types of operators (actors) in **openclean** pipelines.


Features
========
openclean has many features that make the data wrangling experience straightforward. It shines particularly in these areas:

Data Profiling
--------------
openclean comes with a profiler to provide users actionable metrics about their data's quality. It allows users to detect possible problems early on by providing various statistical measures of the data from min-max frequencies, to uniqueness and entropy calculations. The interface is easy to implement and can be extended by python savvy users to cater their needs.

Data Cleaning & Wrangling
-------------------------
openclean's operators have been created specifically to handle data janitorial tasks. They help identify and present statistical anomalies, fix functional dependency violations, locate and update spelling mistakes, and handle missing values gracefully. As openclean is growing fast, so is this list of operators!

Data Enrichment
---------------
openclean seamlessly integrates with `Socrata <https://dev.socrata.com/data/>`_ and `Reference Data Repository <https://github.com/VIDA-NYU/reference-data-repository>`_ to provide it's users master datasets which can be incorporated in the data cleaning process.

Data Provenance
---------------
openclean comes with a mini-version control engine that allows users to maintain versions of their datasets and at any point commit, checkout or rollback changes. Not only this, users can register custom functions inside the openclean engine and apply them effortlessly across different datasets/notebooks.


Installation
==============

Install **openclean** from PyPI using ``pip`` with:

.. code-block:: bash

    pip install openclean

You can also install the different openclean extensions ``openclean-geo``, ``openclean-metanome``, ``openclean-notebook``, and ``openclean-pattern``, or install openclean with all the extensions:

.. code-block:: bash

    pip install openclean[full]


**Note**: See the *Demo* section below for instructions to run the `example notebooks <https://github.com/VIDA-NYU/openclean/tree/master/examples/notebooks>`_ in this repository.

Usage
=====

We include several example notebooks in this repository that demonstrate possible use cases for **openclean**. We recommend starting with the `documentation <http://openclean.readthedocs.io/>`_ or the New York City Restaurant Inspection Results notebook. In that example our goal is to reproduce a previous `study from 2014 that looks at the distribution of restaurant inspection grades in New York City <https://iquantny.tumblr.com/post/76928412519/think-nyc-restaurant-grading-is-flawed-heres>`_. For our study, we use data that was downloaded in Sept. 2019. The example is split into two different Jupyter notebooks:

- `Data Profiling <https://github.com/VIDA-NYU/openclean-core/blob/master/examples/notebooks/NYCRestaurantInspections/NYC%20Restaurant%20Inspections%20-%20Profiling.ipynb>`_
- `Data Cleaning <https://github.com/VIDA-NYU/openclean-core/blob/master/examples/notebooks/NYCRestaurantInspections/NYC%20Restaurant%20Inspections%20-%20Cleaning.ipynb>`_

Other examples along with the datasets are located in `the examples' folder <https://github.com/VIDA-NYU/openclean-core/tree/master/examples/notebooks>`_


Demo
====

Use the following steps to setup and run the `example notebooks <https://github.com/VIDA-NYU/openclean/tree/master/examples/notebooks>`_ in this repository. We recommend using a virtual environment. Below are two examples for setting up a virtual environment

.. code-block:: bash

    # -- Create a new virtual environment
    virtualenv venv
    # -- Activate the virtual environment
    source venv/bin/activate

If you are using the Python distribution from `Anaconda <https://www.anaconda.com/>`_, you can setup an environment like this:

.. code-block:: bash

    # -- Create a new virtual environment
    conda create -n openclean pip
    # -- Activate the virtual environment
    conda activate openclean


After activating your virtual environment, follow these steps to setup and run the notebook examples :

.. code-block:: bash

    # Clone the openclean repository into your current working directory.
    git clone git@github.com:VIDA-NYU/openclean.git
    # Change working directory to the cloned repository.
    cd openclean
    # Install openclean and dependencies required for the demo
    pip install .[demo]
    # Run Jupyter (the navigate to the notebooks in folder `examples/notebooks`)
    jupyter notebook

Demo Video
==========

Want to see **openclean** in action? Check out our video demo: https://youtu.be/HNmNB6YMgHk

Documentation
=============
The official documentation is hosted on readthedocs: http://openclean.readthedocs.io/

You can also read more about openclean in this blog post (on `GitHub <https://github.com/VIDA-NYU/openclean/blob/master/docs/blog/blog.md>`_ and `Towards Data Science <https://towardsdatascience.com/the-openclean-open-source-data-cleaning-library-9c6b8540794f>`_).

Contributing
============
We welcome all contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas.

A detailed overview on how to contribute can be found `here <https://openclean.readthedocs.io/source/contribute.html>`_.
