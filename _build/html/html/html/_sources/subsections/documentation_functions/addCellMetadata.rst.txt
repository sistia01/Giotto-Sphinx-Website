.. _addCellMetadata: 

#############################
Add Cell Metadata
#############################

.. describe:: addCellMetadata()

*Adds cell metadata to the Giotto Object.*

.. code-block::

	addCellMetadata(
  		gobject,
  		new_metadata,
  		vector_name = NULL,
  		by_column = FALSE,
  		column_cell_ID = NULL
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **new_metadata**	
	  - new cell metadata to use (data.table, data.frame, etc.)
	* - **vector_name**	
	  - Optional: custom name if you provide a single vector
	* - **by_column**	
	  - merge metadata based on ``cell_ID`` column in ``pDataDT(default = FALSE)``
	* - **column_cell_ID**	
	  - column name of new metadata to use if ``by_column = TRUE``

******************
Value 
******************
Giotto Object

************************
Details
************************

You can add additional cell metadata in two manners: 

1. Provide a ``data.table`` or ``data.frame`` with gene annotations in the same order as the gene_ID column in ``fDataDT(gobject)``.
2. Provide a ``data.table`` or ``data.frame`` with gene annotations and specify which column contains the gene IDs. These gene IDs need to match with the gene_ID column in ``fDataDT(gobject)``. 
