.. _writeHMRFresults: 

####################################################
Write `doHMRF() <doHMRF>`_ Results
####################################################

.. describe:: writeHMRFresults()

*Write results from doHMRF to a data.table.*

.. code-block::

	writeHMRFresults(
  		gobject,
  		HMRFoutput,
  		k = NULL,
  		betas_to_view = NULL,
  		print_command = F
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - HMRFoutput	
	  - HMRF output from doHMRF
	* - k	
	  - k to write results for
	* - betas_to_view	
	  - results from different betas that you want to view
	* - print_command	
	  - see the python command





******************
Value 
******************

A data.table with HMRF results for each b and the selected k. 



