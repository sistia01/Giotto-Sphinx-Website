.. _combineCPG: 

#########################################################################
Combine ICG Scores (Pairwise)
#########################################################################

.. describe:: combineCPG()

*Combine ICG scores in a pairwise manner.*

.. code-block::

	combineCPG(...)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 1 


	* - ...
	  - Arguments passed on to `combineICG() <combineICG>`_
	* - **cpgObject**	
	  - ICG (interaction changed gene) score object
	* - **selected_ints**	
	  - subset of selected cell-cell interactions (optional)
	* - **selected_genes**	
	  - subset of selected genes (optional)
	* - **specific_genes_1**	
	  - specific geneset combo (need to position match specific_genes_2)
	* - **specific_genes_2**	
	  - specific geneset combo (need to position match specific_genes_1)
	* - **min_cells**	
	  - minimum number of target cell type
	* - **min_int_cells**	
	  - minimum number of interacting cell type
	* - **min_fdr**	
	  - minimum adjusted p-value
	* - **min_spat_diff**	
	  - minimum absolute spatial expression difference
	* - **min_log2_fc**	
	  - minimum absolute log2 fold-change
	* - **do_parallel**	
	  - run calculations in parallel with mclapply
	* - **cores**	
	  - number of cores to use if do_parallel = TRUE
	* - **verbose**	
	  - verbose

.. seealso::
	`combineICG() <combineICG>`_.
