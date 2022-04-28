.. _addHMRF: 

####################################################
Add doHMRF Results
####################################################

.. describe:: addHMRF()

*Add selected results from `doHMRF() <doHMRF>`_ to the Giotto object*

.. code-block::

	addHMRF(
		gobject, 
		HMRFoutput, 
		k = NULL, 
		betas_to_add = NULL, 
		hmrf_name = NULL
	)


	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **HMRFoutput**	
	  - HMRF output from doHMRF
	* - **k**	
	  - k to write results for
	* - **betas_to_view**	
	  - results from different betas that you want to view
	* - **print_command**	
	  - see the python command


******************
Value 
******************

A Giotto object. 



