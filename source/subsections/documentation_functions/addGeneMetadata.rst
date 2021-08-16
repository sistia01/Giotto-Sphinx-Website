.. _addGeneMetadata: 

#############################
Add Gene Metadata
#############################

.. describe:: addGeneMetadata()

*Adds gene metadata to the Giotto Object.*

.. code-block::

	addGeneMetadata(
		gobject, 
		new_metadata, 
		by_column = F, 
		column_gene_ID = NULL
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
	  - new metadata to use
	* - **by_column**	
	  - merge metadata based on gene_ID column in fDataDT
	* - **column_gene_ID**	
	  - column name of new metadata to use if by_column = TRUE

******************
Value 
******************
Giotto Object

************************
Details
************************

You can add additional gene metadata in two manners: 

1. Provide a ``data.table`` or ``data.frame`` with gene annotations in the same order as the gene_ID column in ``fDataDT(gobject)``. +*9 
2. Provide a ``data.table`` or ``data.frame`` with gene annotations and specify which column contains the gene IDs. These gene IDs need to match with the gene_ID column in ``fDataDT(gobject)``. 
