.. _subsetGiotto: 

#############################
Subset Giotto
#############################

.. describe:: subsetGiotto()

*Subsets Giotto object including previous analyses.*

.. code-block::

	subsetGiotto(gobject, cell_ids = NULL, gene_ids = NULL, verbose = FALSE)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **cell_ids**	
	  - cell IDs to keep
	* - **gene_ids**	
	  - gene IDs to keep
	* - **verbose**	
	  - be verbose

******************
Value 
******************

Giotto Object

************************
Examples
************************

.. code-block::
	
	# \donttest{

	data(mini_giotto_single_cell)

	random_cells = sample(slot(mini_giotto_single_cell, 'cell_ID'), 10)
	random_genes = sample(slot(mini_giotto_single_cell, 'gene_ID'), 10)

	subset_obj = subsetGiotto(mini_giotto_single_cell,
                         cell_ids = random_cells,
                         gene_ids = random_genes)

	# }

