.. _installGiottoEnvironmentFunction: 

#############################
Install Giotto Environment
#############################

.. describe:: installGiottoEnvironment()

*Installs a Giotto environment*

.. code-block::

	installGiottoEnvironment(
  		packages_to_install = c("pandas", "networkx", "python-igraph", "leidenalg",
    			"python-louvain", "python.app", "scikit-learn"),
  		force_miniconda = FALSE,
  		force_environment = FALSE,
  		verbose = TRUE
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **packages_to_install**	
	  - all python modules (packages) that should be installed for Giotto to work
	* - **force_miniconda**	
	  - force reinstallation of miniconda
	* - **force_environment**	
	  - force reinstallation of the giotto environment
	* - **verbose**	
	  - be verbose

******************
Value 
******************
Installs a Giotto environment using the reticulate miniconda system


***************
Details
***************
This function will install a local giotto environment using the miniconda system as implemented by reticulate. 
Once this giotto environment is installed it will be automatically detected when you run the Giotto toolbox. If you want to use your own python path then you can set the ``python_path`` in the `createGiottoInstructions <createGiottoInstructions>`_ and provide the instructions to the `createGiottoObject <createGiottoObject>`_ function.

************************
Examples
************************
This command will install an r-miniconda and a Giotto environment with all of the necessary python modules.

.. code-block::

	if (FALSE) {installGiottoEnvironment()}




