.. _findMastMarkers_one_vs_all: 

#########################################################################
Identify Marker Genes Using MAST in One vs. All Manner
#########################################################################

.. describe:: findMastMarkers_one_vs_all()

*Identify marker genes for all clusters in a one vs all manner based on the MAST package.*

.. code-block::

	findMastMarkers_one_vs_all(
 	 	gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		subset_clusters = NULL,
  		adjust_columns = NULL,
  		pval = 0.001,
  		logFC = 1,
  		min_genes = 10,
  		verbose = TRUE,
  		...
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - expression_values	
	  - gene expression values to use
	* - cluster_column	
	  - clusters to use
	* - subset_clusters	
	  - selection of clusters to compare
	* - adjust_columns	
	  - column in pDataDT to adjust for (e.g. detection rate)
	* - pval	
	  - filter on minimal p-value
	* - logFC	
	  - filter on logFC
	* - min_genes	
	  - minimum genes to keep per cluster, overrides pval and logFC
	* - verbose	
	  - be verbose
	* - ...	
	  - additional parameters for the zlm function in MAST

*******************
Value
*******************

A data.table with marker genes

*******************
Details
*******************

`findMastMarkers <findMastMarkers>`_.



*******************
Examples
*******************

.. code-block::

	data(mini_giotto_single_cell)

	mast_markers = findMastMarkers_one_vs_all(gobject = mini_giotto_single_cell,
                                          cluster_column = 'leiden_clus')
	#> using 'MAST' to detect marker genes. If used in published research, please cite:
	#>   McDavid A, Finak G, Yajima M (2020).
	#>   MAST: Model-based Analysis of Single Cell Transcriptomics. R package version 1.14.0,
	#>   https://github.com/RGLab/MAST/.#> 
	#>  start with cluster  1 #> Assuming data assay in position 1, with name et is log-transformed.#> 
	#> Done!#> Combining coefficients and standard errors#> Calculating log-fold changes#> Calculating likelihood ratio tests#> Refitting on reduced model...#> 
	#> Done!#> 
	#>  start with cluster  2 #> Assuming data assay in position 1, with name et is log-transformed.#> 
	#> Done!#> Combining coefficients and standard errors#> Calculating log-fold changes#> Calculating likelihood ratio tests#> Refitting on reduced model...#> 
	#> Done!#> 
	#>  start with cluster  3 #> Assuming data assay in position 1, with name et is log-transformed.#> 
	#> Done!#> Combining coefficients and standard errors#> Calculating log-fold changes#> Calculating likelihood ratio tests#> Refitting on reduced model...#> 
	#> Done!


