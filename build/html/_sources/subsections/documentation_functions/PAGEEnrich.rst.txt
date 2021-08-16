.. _PAGEEnrich: 

################################################################
Calculate Gene Signature  Enrichment With PAGE
################################################################

.. describe:: PAGEEnrich()

*Function to calculate gene signature enrichment scores per spatial position using PAGE..*

.. code-block::

	PAGEEnrich()

**********************
Arguments
**********************
.. note:: 
	Arguments passed on to `runPAGEEnrich() <runPAGEEnrich> `_


.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**
	  - Giotto object
	* - **sign_matrix**
	  - Matrix of signature genes for each cell type / process
	* - **expression_values**
	  - expression values to use
	* - **min_overlap_genes**
	  - minimum number of overlapping genes in sign_matrix required to calculate enrichment
	* - **reverse_log_scale**
	  - reverse expression values from log scale
	* - **logbase**
	  - log base to use if reverse_log_scale = TRUE
	* - **output_enrichment**
	  - how to return enrichment output
	* - **p_value**
	  - calculate p-values (boolean, default = FALSE)
	* - **include_depletion**
	  - calculate both enrichment and depletion
	* - **n_times**
	  - number of permutations to calculate for p_value
	* - **max_block**
	  - number of lines to process together (default = 20e6)
	* - **name**
	  - to give to spatial enrichment results, default = PAGE
	* - **verbose**
	  - be verbose
	* - **return_gobject**
	  - return giotto object

.. seealso::
	`runPAGEEnrich() <runPAGEEnrich>`_





