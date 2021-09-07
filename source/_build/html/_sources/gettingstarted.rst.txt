.. _gettingstartedpage: 

#######################
Getting Started 
#######################
*************
Description 
*************

- Giotto provides a flexible framework for common single-cell processing steps such as:
   
  - Quality control
  - Normalization
  - Dimension reduction
  - Clustering and cell type annotation

* To facilitate the analysis of recently emerging high-throughput, but lower-resolution spatial transcriptomic technologies, such as 10X Genomics Visium and Slide-seq, Giotto has 3 implemented algorithms for estimating the spatial enrichment of different cell types by integration of known gene signatures or single-cell RNAseq expression and annotation data.
* Spatial information is retained through the formation of a spatial grid and/or a spatial proximity network, which is used to:
  
  * Identify spatial genes
  * Extract continuous spatial-expression patterns
  * Identify discrete spatial domains using HMRF
  * Explore cell-type/cell-type spatial interaction enrichment or depletion
  * Calculate spatially increased ligand-receptor expression in cells of interacting cell type pairs
  * Find interaction changed genes (ICG): genes that change expression in one cell type due to interaction with a neighboring cell type

* Giotto provides a number of options to visualize both 2D and 3D data and the outcome of Giotto can be interactively explored using `Giotto Viewer`_, which allows you to overlay the obtained results with raw or additional images of the profiled tissue section(s).

.. _Giotto Viewer: http://spatial.rc.fas.harvard.edu/spatialgiotto/giotto.install.native.html

Make sure to check out the `Datasets <datasets>`_ section to see examples of the Giotto workflow.

*************
Requirements
*************
* R (>= 3.5.1)
* Python (>= 3.0)
* `Windows, MacOS or Linux specific installation tools.`_

.. _Windows, MacOS or Linux specific installation tools.: https://support.rstudio.com/hc/en-us/articles/200486498-Package-Development-Prerequisites


*************
Installation
*************
Giotto must be installed in both Python and R. Below, you will find the instructions for both Giotto Installation (which is done in R) and installation of Python Modules. Please make sure that your system has satisfied all of the requirements needed to sucessfully install Giotto.
In addition, we have provided a way for users to automatically install all of the necessary python modules via R (See: **Automatic Installation** below). 
Checkout our :ref:`Errors and FAQs Section <faqs>` for more information and troubleshooting tips on some common installation issues.  

Giotto Installation Workflow
==============================
This workflow image is designed to help with Giotto Installation. Users should follow any of the three potential paths aimed to guide them through the installation process. 

.. image:: images/Giotto_Installation_Workflow.png
    :width: 600
    :alt: Image of Giotto Installation Workflow
    :align: center

.. _R_Installation: 

R Installation 
==================
If this is your first time installing an R Package please proceed to **First Time R Package Installation.** If you are already familiar with installing R packages please proceed to **First Time Giotto Installation**.

.. _FirstTimeR:

First Time R Package Installation 
------------------------------------
*Package Development Requirements*

If this is the first time you build and install an R package you can follow `this link <https://support.rstudio.com/hc/en-us/articles/200486498-Package-Development-Prerequisites>`_, which has simple installation instructions for Windows, Mac OSX and Linux.

To specifically install the command-line tools of Xcode for Mac OSX you might also need to run this line **in terminal**:

.. code-block: 

  xcode-select -- install 

.. _FirstTimeGiotto: 

First Time Giotto Installation 
--------------------------------
You can install Giotto with (~1-5 mins)

**This version requires C Compilation**

.. code-block::

	library(devtools) # If not installed: install.packages('devtools')
	library(remotes)  #If not installed: install.packages('remotes')
	remotes::install_github("RubD/Giotto") 

.. warning:: 	
	If you are having compilation (gfortran) problems check goftran.

**This version does not require C Compliation**	

.. code-block::

	remotes::install_github("RubD/Giotto@cless") 


.. _Python_Installation:

Python Installation 
=========================
To perform all potential steps and analysis in the Giotto spatial toolbox the user needs to have a number of python modules installed. 
To make this process as flexible and easy as possible two different strategies can be used

Required Modules
--------------------------
These are necessary to run all available analyses, but can be installed automatically (see **Automatic Installation**) or manually (see **Manual Installation**):

* pandas
* python-igraph (igraph)
* networkx
* leidenalg
* python-louvain (community)
* smfishHmrf
* python.app (**OSX only**)
* scikit-learn

First Time Python Module Installation 
---------------------------------------
Information on how to install a Python package can be found `here <https://packaging.python.org/tutorials/installing-packages/>`__. 

.. _manualinstallation:

Manual Installation
---------------------
There are two methods thorugh which users can install the necessary Python modules manually with **(1) Pip in Python3** or **(2) Conda**.

.. warning:: 
	With either ONE of the **Manual Installation** options (**Install with Pip in Python3** or **Install with Conda**) the user will have to provide the python path to :ref:`createGiottoInstructions <createGiottoInstructions>`. 
	If this is not done, Giotto will not be able to use the installed python modules.
	
*Note:* If pip install does not work, try installing the modules within a `conda environment <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands>`_. For more inforomation on vitual environments with conda visit this `page <https://heartbeat.fritz.ai/creating-python-virtual-environments-with-conda-why-and-how-180ebd02d1db>`_.

.. dropdown:: **1. Install with Pip in Python3**

	*For OSX, Windows, or Linux:* 

	.. code-block:: 

		pip3 install pandas python-igraph networkx python-louvain leidenalg scikit-learn smfishHmrf

.. dropdown:: **2. Install with Conda**

    1. Create yaml file (e.g. environment.yml) with the following information:

		.. code-block:: 

			name: giotto_env
			channels:
			— defaults
			dependencies:
			— pip=3.4
			— pandas
			— networkx
			- python-igraph
			- leidenalg
			- python-louvain
			- python.app (!!only for OSX!!)
			- scikit-learn
			prefix: /Users/your_username/anaconda3/envs/giotto_env

    2. Create Conda Environment Based on yaml File: 

    	.. code-block:: 

    		conda env create -f environment.yml
      
    3. Use the path to this environment when you create the Giotto instructions or Giotto object

		.. dropdown:: For OSX
		
			.. code-block::
			
				/Users/your_username/anaconda3/envs/giotto_env/bin/pythonw


		.. dropdown:: For Windows
		
			.. code-block:: 
			
				/Users/your_username/anaconda3/envs/giotto_env/python.exe


		.. dropdown:: For Linux
		
			.. code-block:: 
			
				/Users/your_username/anaconda3/envs/giotto_env/bin/python


Specify Python Path After Manual Installation 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
With the Manual Installation option, once the user has installed all of the necessary modules, via either of the methods above (e.g. :ref:`Conda <InstallWithConda>`), the path to their python environment can be provided as an instruction in R.

.. code-block::
		
		# Within R
	
		library(Giotto)
		my_instructions = createGiottoInstructions(python_path = 'your/python/path')
		my_giotto_object = createGiottoObject(
			raw_exprs = '...',
			spatial_locs = '...', 
			instructions = my_instructions)

.. _automaticinstallation:

Automatic Installation
----------------------------
The python modules will be installed automatically in a miniconda environment when installing Giotto. However, it will ask you whether you want to install them and you can opt out and select your preferred python path. In that case you need to do a manual installation of the python modules.

To perform all potential steps and analysis in the Giotto spatial toolbox the user needs to have a number of python modules installed. `Installation of the Giotto Environment <InstallGiottoEnvironment>`__  allows users to install the required Python environment via MiniConda without specifying their python path. 

.. _InstallGiottoEnvironment: 

Installation of Giotto Environment 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
With this option, the user can just install a Giotto python environment using r-miniconda. This is done after installatio of the Giotto package (via R).  

.. code-block::

	library(Giotto)

.. dropdown:: Install Giotto Environment 

	.. code-block::

		installGiottoEnvironmnt()

.. dropdown:: Re-Install the Giotto environment

	.. code-block::

		installGiottoEnvironment(force_environment = TRUE)

.. dropdown:: Re-install mini-conda and environment

	.. code-block::
		
		installGiottoEnvironment(force_miniconda = TRUE)
	
.. dropdown:: Remove Giotto Environment

	.. code-block::

		removeGiottoEnvironment()

.. note::
	With the automatic installation option, the user **DOES NOT** have to specify a python path. 

.. _howtolabel:

*******
HowTos
*******
Giotto provides a lot of analyses, visualizations and other options to facilitate your spatial dataset analysis. We are working on providing easy-to-understand examples or tutorials, but if anything is not clear or if there is something you would like to see in particular, then do not hesitate to `contact us.`_
In addition to our HowTos we have also created a way for users to test out Giotto via `Binder <BinderInformation>`_ and `Docker <DockerInformation>`_ (see: `Try Giotto <TryGiotto>`_)

.. _contact us.: https://github.com/RubD/Giotto/issues

:doc:`Giotto Workflow Analyses Steps </giottoworkflowanalyses>`
================================================================

*Optional*: Install a Giotto Environment

#. :ref:`Create a Giotto Object <create-a-giotto-object>`
#. :ref:`Process and Filter a Giotto Object <process-and-filter-a-giotto-object>` 
#. :ref:`Dimension Reduction <dimension-reduction>`  
#. :ref:`Cluster cells or spots <cluster_cells-or-spots>`
#. :ref:`Identify differentially expressed genes <identify-differentially-expressed-genes>`
#. :ref:`Annotate clusters <annotate-clusters>`
#. :ref:`Cell-type enrichment or deconvolution per spot <cell-type-enrichment-or-deconvolution-per-spot>`
#. :ref:`Create a Spatial grid or Network <spatial-grid-or-network>`
#. :ref:`Find genes with a spatially coherent gene expression pattern <spatially-coherent-gene-expression-pattern>`
#. :ref:`Identify genes that are spatially co-expressed <spatially-coexpressed-genes>`
#. :ref:`Explore spatial domains with HMRF <spatial-domains-with-HMRF>`
#. :ref:`Calculate spatial cell-cell interaction enrichment <calculate-spatial-cell-cell-interaction>`
#. :ref:`Find cell-cell interaction changed genes (ICG) <find-cell-cell-interactions-changed-genes>`
#. :ref:`Identify enriched or depleted ligand-receptor interactions in hetero and homo-typic cell interactions <enriched-or-depleted-ligand-receptor-interactions>`
#. :ref:`Export Giotto results to use in Giotto viewer <giotto-viewer-export>`
 
Giotto Analyzer and Viewer interaction [work in progress]
===========================================================

* How to switch between Giotto Analyzer and Viewer?

Tips and Tricks
============================================================

* :ref:`Different ways of subsetting Giotto results? <ways-of-subsetting>`
* :ref:`How to create global instructions and show or save your created plots? <global-instructions-and-save-plots>`
* :ref:`Different ways to visualize your spatial data? <visualize-data>`
* :ref:`How to test and store multiple parameters or analyses? <test-and-store>`
* :ref:`Visualize spatial data with voronoi plots <voronoi-plots>`
* :ref:`Working with the Giotto class <giotto-class>`
* :ref:`Adding and Working with Images in Giotto <working-with-giotto-images>`


.. seealso:: 
	:ref:`FAQs <faqs>` for more information
