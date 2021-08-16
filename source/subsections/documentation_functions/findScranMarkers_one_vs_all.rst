.. _findScranMarkers_one_vs_all: 

###################################################
Identify Marker Genes in a One vs All Manner
###################################################

.. describe:: findScranMarkers_one_vs_all()

*Identify marker genes for all clusters in a one vs all manner based on scran's implementation of `findMarkers <findMarkers>`_.*

.. code-block::

	findScranMarkers_one_vs_all(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		subset_clusters = NULL,
  		pval = 0.01,
  		logFC = 0.5,
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
	  - subset of clusters to use
	* - pval	
	  - filter on minimal p-value
	* - logFC	
	  - filter on logFC
	* - min_genes	
	  - minimum genes to keep per cluster, overrides pval and logFC
	* - verbose	
	  - be verbose
	* - ...	
	  - additional parameters for the findMarkers function in scran


******************
Value 
******************
A data.table with marker genes.

..seealso::
	`findScranMarkers <findScranMarkers>`_.



******************
Examples
******************

.. note:: 
	When  'Scran' to detect marker genes. If used in published research, please cite: `Lun, A. T., McCarthy, D. J., & Marioni, J. C. (2016). A step-by-step workflow for low-level analysis of single-cell RNA-seq data with Bioconductor. F1000Research, 5. <https://www.ncbi.nlm.nih.gov/pmc/articles/pmc5112579/>`_
	
	data(mini_giotto_single_cell)

	scran_markers = findScranMarkers_one_vs_all(gobject = mini_giotto_single_cell,
                                            cluster_column = 'leiden_clus')

	#>   F1000Res., 5, 2122. doi: 10.12688/f1000research.9501.2. #> 
	#>  start with cluster  1 
	#> 
	#>  start with cluster  2 
	#> 
	#>  start with cluster  3 


