.. _findCPG: 

#########################################################################
Identify Cell-Cell Interaction Changed Genes (ICGs)
#########################################################################

.. describe:: findCPG()

*Identifies cell-to-cell Interaction Changed Genes (ICG), i.e. genes that are differentially expressed due to proximity to other cell types.*

.. code-block::

	findCPG(...)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 1 

	* - ... 
	  - Arguments passed on to `findICG() <findICG>`_
	* - **gobject**	
	  - giotto object
	* - **expression_values**	
	  - expression values to use
	* - **selected_genes**	
	  - subset of selected genes (optional)
	* - **cluster_column**	
	  - name of column to use for cell types
	* - **spatial_network_name**	
	  - name of spatial network to use
	* - **minimum_unique_cells**	
	  - minimum number of target cells required
	* - **minimum_unique_int_cells**	
	  - minimum number of interacting cells required
	* - **diff_test**	
	  - which differential expression test
	* - **mean_method**	
	  - method to use to calculate the mean
	* - **offset**	
	  - offset value to use when calculating log2 ratio
	* - **adjust_method**	
	  - which method to adjust p-values
	* - **nr_permutations**	
	  - number of permutations if diff_test = permutation
	* - **exclude_selected_cells_from_test**	
	  - exclude interacting cells other cells
	* - **do_parallel**	
	  - run calculations in parallel with mclapply
	* - **cores**	
	  - number of cores to use if do_parallel = TRUE
	* - **set_seed**	
	  - set a seed for reproducibility
	* - **seed_number**	
	  - seed number


.. seealso:: 
	`findICG() <findICG>`_.

