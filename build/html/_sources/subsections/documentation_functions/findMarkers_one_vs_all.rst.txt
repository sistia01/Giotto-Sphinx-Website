.. _findMarkers_one_vs_all: 

#########################################################################
Find Marker Genes At Once
#########################################################################

.. describe:: findMarkers_one_vs_all()

*Identify marker genes for all clusters in a one vs all manner.*

.. code-block::

	findMarkers_one_vs_all(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		cluster_column,
  		subset_clusters = NULL,
  		method = c("scran", "gini", "mast"),
  		pval = 0.01,
  		logFC = 0.5,
  		min_genes = 10,
  		min_expr_gini_score = 0.5,
  		min_det_gini_score = 0.5,
  		detection_threshold = 0,
  		rank_score = 1,
  		adjust_columns = NULL,
  		verbose = TRUE,
  		...
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
	  - gene expression values to use
	* - **cluster_column**	
	  - clusters to use
	* - **subset_clusters**	
	  - selection of clusters to compare
	* - **method**	
	  - method to use to detect differentially expressed genes
	* - **pval**	
	  - scran & mast: filter on minimal p-value
	* - **logFC**	
	  - scan & mast: filter on logFC
	* - **min_genes**	
	  - minimum genes to keep per cluster, overrides pval and logFC
	* - **min_expr_gini_score**	
	  - gini: filter on minimum gini coefficient for expression
	* - **min_det_gini_score**	
	  - gini: filter minimum gini coefficient for detection
	* - **detection_threshold**	
	  - gini: detection threshold for gene expression
	* - **rank_score**	
	  - gini: rank scores to include
	* - **adjust_columns**	
	  - mast: column in pDataDT to adjust for (e.g. detection rate)
	* - **verbose**	
	  - be verbose
	* - **...**	
	  - additional parameters for the findMarkers function in scran or zlm function in MAST

*******************
Value
*******************
A data.table with marker genes

*******************
Details
*******************
Wrapper for all one vs all functions to detect marker genes for clusters.

.. seealso::
	`findScranMarkers_one_vs_all <findScranMarkers_one_vs_all>`_, `findGiniMarkers_one_vs_all <findGiniMarkers_one_vs_all>`_, and `findMastMarkers_one_vs_all <findMastMarkers_one_vs_all>`_.


