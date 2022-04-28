.. _combineMetadata: 

#############################
Combine Cell Metadata
#############################

.. describe:: combineMetadata()

*This function combines the cell metadata with spatial locations and enrichment results from `runSpatialEnrich <runSpatialEnrich>`_.*

.. code-block::

	combineMetadata(gobject, spat_enr_names = NULL)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - Giotto object
	* - **spat_enr_names**	
	  - names of spatial enrichment results to include

******************
Value 
******************
Extended cell metadata in ``data.table`` format.
