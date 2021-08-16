.. _filterGiotto: 

#############################
Filter Giotto
#############################

.. describe:: filterGiotto()

*Filter Giotto object based on expression threshold.*

.. code-block::

	createGiottoVisiumObject(
  		visium_dir = NULL,
 		 expr_data = c("raw", "filter"),
  		gene_column_index = 1,
  		h5_visium_path = NULL,
  		h5_gene_ids = c("symbols", "ensembl"),
  		h5_tissue_positions_path = NULL,
  		h5_image_png_path = NULL,
  		png_name = NULL,
  		xmax_adj = 0,
  		xmin_adj = 0,
  		ymax_adj = 0,
  		ymin_adj = 0,
  		instructions = NULL,
 		cores = NA,
  		verbose = TRUE
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **expression_values**	
	  - expression values to use
	* - **expression_threshold**	
	  - threshold to consider a gene expressed
	* - **gene_det_in_min_cells**	
	  - minimum # of cells that need to express a gene
	* - **min_det_genes_per_cell**	
	  - minimum # of genes that need to be detected in a cell
	* - **verbose**	
	  - verbose

******************
Value 
******************
Giotto Object

************************
Details
************************
The function `filterCombinations <filterCombinations>`_ can be used to explore the effect of different parameter values.

************************
Examples
************************

.. code-block::
	
	data(mini_giotto_single_cell)

	filtered_gobject = filterGiotto(mini_giotto_single_cell,
                                gene_det_in_min_cells = 10,
                                min_det_genes_per_cell = 10)



