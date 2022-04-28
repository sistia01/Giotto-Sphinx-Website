.. _filterCPG: 

#########################################################################
Filter ICGs
#########################################################################

.. describe:: filterCPG()

*Filter Interaction Changed Genes' (ICGs) Scores .*

.. code-block::

	filterCPG(...)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 1

	* - ... 
	  - Arguments passed on to `filterICG() <filterICG>`_
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


.. seealso::
	`filterICG() <filterICG>`_.

