.. _loadHMRF: 

####################################################
Load HMRF
####################################################

.. describe:: loadHMRF()

*Load previous Hidden Markov Random Field (HMRF) model.*

.. code-block::

	loadHMRF(
  		name_used = "test",
  		output_folder_used,
  		k_used = 10,
  		betas_used,
  		python_path_used
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **name_used**	
	  - name of HMRF that was run
	* - **output_folder_used**	
	  - output folder that was used
	* - **k_used**	
	  - number of HMRF domains that was tested
	* - **betas_used**	
	  - betas that were tested
	* - **python_path_used**	
	  - python path that was used


******************
Value 
******************
Reloads a previously run HMRF from `doHRMF(). <doHRMF>`_


******************
Details 
******************
Description of HMRF parameters ...




