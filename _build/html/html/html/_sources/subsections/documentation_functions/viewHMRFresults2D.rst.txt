.. _viewHMRFresults2D: 

####################################################
View HMRF Results
####################################################

.. describe:: viewHMRFresults2D()

*View results from `doHMRF() <doHMRF>`_.*

.. code-block::

	viewHMRFresults2D(
		gobject, 
		HMRFoutput, k = NULL, 
		betas_to_view = NULL, 
		...
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
	  - number of HMRF domains
	* - betas_to_view	
	  - results from different betas that you want to view
	* - ...	
	  - additional parameters to spatPlot2D()



******************
Value 
******************

Spatial plots with HMRF domains.



.. seealso::
	`spatPlot2D() <spatPlot2D>`_.



