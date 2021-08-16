.. _filterInteractionChangedGenes: 

#########################################################################
Filter ICGs
#########################################################################

.. describe:: filterInteractionChangedGenes()

*Filter Interaction Changed Genes' (ICGs) Scores .*

.. code-block::

	filterInteractionChangedGenes(
  		cpgObject,
  		min_cells = 4,
  		min_cells_expr = 1,
  		min_int_cells = 4,
  		min_int_cells_expr = 1,
  		min_fdr = 0.1,
  		min_spat_diff = 0.2,
  		min_log2_fc = 0.2,
  		min_zscore = 2,
  		zscores_column = c("cell_type", "genes"),
  		direction = c("both", "up", "down")
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **cpgObject**	
	  - ICG (interaction changed gene) score object
	* - **min_cells**	
	  - minimum number of source cell type
	* - **min_cells_expr**	
	  - minimum expression level for source cell type
	* - **min_int_cells**	
	  - minimum number of interacting neighbor cell type
	* - **min_int_cells_expr**	
	  - minimum expression level for interacting neighbor cell type
	* - **min_fdr**	
	  - minimum adjusted p-value
	* - **min_spat_diff**	
	  - minimum absolute spatial expression difference
	* - **min_log2_fc**	
	  - minimum log2 fold-change
	* - **min_zscore**	
	  - minimum z-score change
	* - **zscores_column**	
	  - calculate z-scores over cell types or genes
	* - **direction**	
	  - differential expression directions to keep


**************
Value
**************
A cpgObject that contains the Interaction Changed Genes' differential scores.

