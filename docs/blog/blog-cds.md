# The openclean Open-Source Data Cleaning Library
## A unified framework for data wrangling

*Joint work by Heiko Müller, Sonia Castelo, Munaf Qazi, and Juliana Freire*

Data preparation is still a major bottleneck for many data science projects. A [frequently cited survey in 2016](https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says) found that data scientists spend 60% of their time on data cleaning and organizing data. In the same survey, 57% of the data scientists also stated that they consider data cleaning and organizing data as the least enjoyable task of their job.

Over the years, many tools for profiling, preparing, and cleaning data have been developed, both in academia and industry. These approaches were developed in isolation and in different programming languages with no standardized interfaces. Thus, it is difficult for data scientists to combine existing tools and re-use them in their data processing pipelines.

Inspired by the wide adoption of generic machine learning frameworks such as [scikit-learn](https://scikit-learn.org/stable/), [TensorFlow](https://www.tensorflow.org/), and [PyTorch](https://pytorch.org/), we are currently developing **openclean**, an open-source Python library for data profiling and data cleaning. The source code for **openclean** is [available on GitHub](https://github.com/VIDA-NYU/openclean).

Our goals for openclean are twofold. First, we aim to provide a unified framework for practitioners that brings together open-source data profiling and data cleaning tools into an easy-to-use environment.  By making existing tools available to a large user-community, and through the integration with the rich Python ecosystem, openclean has the potential to simplify data cleaning tasks. Second, by  providing a structured, extensible framework, openclean can serve as a platform to which researchers and developers can contribute their techniques.  We hope that by bringing together a community of users, developers, and researchers, we will be in a better position to attack the many challenges in dealing with data quality.

**openclean** has many features that make the data wrangling experience straightforward. It shines particularly in these areas:

*Data Profiling*: **openclean** comes with a profiler to provide users actionable metrics about data quality. It allows users to detect possible problems early on by providing various statistical measures of the data from min-max frequencies, to uniqueness and entropy calculations.

*Data Cleaning & Wrangling*: **openclean**'s operators have been created specifically to handle data janitorial tasks. They help identify and present statistical anomalies, fix functional dependency violations, locate and update spelling mistakes, and handle missing values gracefully.

*Data Enrichment*: **openclean** seamlessly integrates with the Socrata Open Data API and the Reference Data Repository giving users easy access to standard datasets which can be incorporated in the data cleaning process.

![openclean code cell example](https://raw.githubusercontent.com/VIDA-NYU/openclean/master/docs/blog/graphics/code-cell.png)

**Figure 1** shows an example of using **openclean**. We first select three columns from the NYC Parking Violations dataset (jt7v-77mi) and convert the vehicle color values to uppercase. Then, we identify potential misspellings and abbreviations of vehicle colors as violations of the functional dependency that uses Plate ID and registrations state to uniquely identify vehicles. To resolve these conflicts, we apply a conflict resolution strategy that eliminates violations caused by common abbreviations like BLK and WH for BLACK and WHITE.

*Data Provenance*: **openclean** comes with a mini-version control engine that allows users to maintain versions of their datasets and at any point commit, checkout or rollback changes.

*GUI - Integration with Jupyter Notebooks*: Data profiling and  cleaning are inherently exploratory tasks. In many scenarios the user needs to visualize data and profiling results (statistics) to get a better understanding of data properties and existing quality issues. In addition to the ability to leverage existing Python libraries for data visualization, **openclean** provides a spreadsheet-like GUI which enables users to visualize and interact with the data from a Jupyter Notebook.

![openclean Jupyter Notebook GUI](https://raw.githubusercontent.com/VIDA-NYU/openclean/master/docs/blog/graphics/blog-ui-gif-annotated.gif)

**Figure 2** shows the Jupyter Notebook GUI for **openclean** that allows users to inspect and manipulate the contents of a dataset in a spreadsheet view.

To read more about openclean, please have a look at our extended blog (on [GitHub](https://github.com/VIDA-NYU/openclean/blob/master/docs/blog/blog.md) and [Towards Data Science](https://towardsdatascience.com/the-openclean-open-source-data-cleaning-library-9c6b8540794f)) or try out the example notebooks in the [GitHub repository](https://github.com/VIDA-NYU/openclean).
