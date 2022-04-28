.. _calculateMetaTableCells: 

########################################
Calculate the Average Metadata Values 
########################################

.. describe:: calculateMetaTableCells()

*Function to calculate the average gene expression for one or more (combined) annotation columns.*

.. code-block::

	calculateMetaTableCells(
  		gobject,
  		value_cols = NULL,
  		metadata_cols = NULL,
  		spat_enr_names = NULL
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **value_cols**	
	  - metadata or enrichment value columns to use
	* - **metadata_cols**	
	  - annotation columns found in pDataDT(gobject)
	* - **spat_enr_names**	
	  - which spatial enrichment results to include

******************
Value 
******************

A ``data.table`` with average metadata values per (combined) annotation

