.. _viewHMRFresults3D: 

####################################################
View HMRF Results
####################################################

.. describe:: viewHMRFresults3D()

*View results from `doHMRF() <doHMRF>`_.*

.. code-block::

	viewHMRFresults3D(
		gobject, 
		HMRFoutput, 
		k = NULL, 
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
	  - additional parameters to `spatPlot3D() <spatPlot3D>_





******************
Value 
******************

Spatial plots with HMRF domains.



.. seealso::
	`spatPlot3D() <spatPlot3D>`_.



