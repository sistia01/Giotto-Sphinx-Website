.. _viewHMRFresults: 

####################################################
View HMRF Results
####################################################

.. describe:: viewHMRFresults()

*View results from `doHMRF() <doHMRF>`_.*

.. code-block::

	viewHMRFresults(
  		gobject,
  		HMRFoutput,
  		k = NULL,
  		betas_to_view = NULL,
  		third_dim = FALSE,
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
	* - third_dim	
	  - 3D data (boolean)
	* - ...	
	  - additional parameters (see `Details <viewHMRFresultsDeails>`_)



******************
Value 
******************

Reloads a previously run HMRF from `doHRMF(). <doHRMF>`_ It has spatial plots with HMRF domains. 

.. _viewHMRFresultsDeails:

******************
Details 
******************

See `doHMRF <doHMRF>`__ for more information. 

.. seealso::
	`spatPlot2D() <spatPlot2D>`_ and `spatPlot3D() <spatPlot3D>`_.

******************
Examples 
******************

.. code-block::

	viewHMRFresults(gobject)