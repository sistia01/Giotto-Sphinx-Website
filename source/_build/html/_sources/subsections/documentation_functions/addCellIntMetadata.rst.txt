.. _addCellIntMetadata: 

#######################################
Add Cell Metadata Information Column 
#######################################

.. describe:: addCellIntMetadata()

*Creates an additional metadata column with information about interacting and non-interacting cell types of the selected cell-cell interaction..*

.. code-block::

	addCellIntMetadata(
  		gobject,
  		spatial_network = "spatial_network",
  		cluster_column,
  		cell_interaction,
  		name = "select_int",
  		return_gobject = TRUE
	)


**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **spatial_network**	
	  - name of spatial network to use
	* - **cluster_column**	
	  - column of cell types
	* - **cell_interaction**	
	  - cell-cell interaction to use
	* - **name**	
	  - name for the new metadata column
	* - **return_gobject**	
	  - return an updated giotto object


******************
Value 
******************
Giotto Object

************************
Details
************************

This function will create an additional metadata column which selects interacting cell types for a specific cell-cell interaction. For example, if you want to color interacting astrocytes and oligodendrocytes it will create a new metadata column with the values "select_astrocytes", "select_oligodendrocytes", "other_astrocytes", "other_oligodendroyctes" and "other". Where "other" is all other cell types found within the selected cell type column.
