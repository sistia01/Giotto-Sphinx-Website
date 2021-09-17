.. _doHMRF: 

####################################################
Rank Spatially Correlated Gene Clusters 
####################################################

.. describe:: doHMRF()

*Rank spatial correlated clusters according to correlation structure.*

.. code-block::

	doHMRF(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		spatial_network_name = "Delaunay_network",
  		spatial_genes = NULL,
  		spatial_dimensions = c("sdimx", "sdimy", "sdimz"),
  		dim_reduction_to_use = NULL,
  		dim_reduction_name = "pca",
  		dimensions_to_use = 1:10,
  		seed = 100,
  		name = "test",
  		k = 10,
  		betas = c(0, 2, 50),
  		tolerance = 1e-10,
  		zscore = c("none", "rowcol", "colrow"),
  		numinit = 100,
  		python_path = NULL,
  		output_folder = NULL,
  		overwrite_output = TRUE
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
	* - **spatial_network_name**	
	  - name of spatial network to use for HMRF
	* - **spatial_genes**	
	  - spatial genes to use for HMRF
	* - **spatial_dimensions**	
	  - select spatial dimensions to use, default is all possible dimensions
	* - **dim_reduction_to_use**	
	  - use another dimension reduction set as input
	* - **dim_reduction_name**	
	  - name of dimension reduction set to use
	* - **dimensions_to_use**	
	  - number of dimensions to use as input
	* - **seed**	
	  - seed to fix random number generator (for creating initialization of HMRF) (-1 if no fixing)
	* - **name**	
	  - name of HMRF run
	* - **k**	
	  - number of HMRF domains
	* - **betas**	
	  - betas to test for. three numbers: start_beta, beta_increment, num_betas e.g. c(0, 2.0, 50)
	* - **tolerance**	
	  - tolerance
	* - **zscore**	
	  - zscore
	* - **numinit**	
	  - number of initializations
	* - **python_path**	
	  - python path to use
	* - **output_folder**	
	  - output folder to save results
	* - **overwrite_output**	
	  - overwrite output folder

******************
Value 
******************
Creates a directory with results that can be viewed with `viewHMRFresults() <viewHMRFresults>`_.

Returns a list type object with the following fields:

* name: name used
* output_data: output path
* k: k used,
* betas: betas used,
* python_path: python_path_used


******************
Details 
******************
Previously we have published a paper that describes the hidden markov random field (HMRF) method for identifying spatial patterns from spatial gene expression data. 
Unlike typical clustering techniques, HMRF integrates both spatial locations and the gene expression to find groups of cells that are both spatially adjacent and which are similar to each other in expression space.

A general guideline for choosing k is to use the gap-statistics by Tibshrani. The elbow point of the gap size vs. k plot usually indicates choices of k. 
To decide which beta one should use, the current state of algorithm repeats HMRF for a number of betas. Here are some guidelines:

* if the number of genes is from 10 to 50, the recommended range is 0 to 10 at increment of 0.5. E.g. c(0,0.5,20)
* if the number of genes is below 50, the recommended range is 0 to 15 at increment of 1. E.g. c(0,1,15)
* if the number of genes is between 50 to 100, the range is 0 to 50 at increment of 2. E.g. c(0, 2, 25)
* if the number of genes is between 100 and 500, the range is 0 to 100 at increment of 5. E.g. c(0, 5, 20)

Within the range of beta, we recommend selecting the best beta by the Bayes information criterion. 
This requires first performing randomization of spatial positions to generate the null distribution of log-likelihood scores for randomly distributed cells for the same range of betas. 
Then find the beta where the difference between the observed and the null log-likelihood is maximized. See the HMRF tutorial from the Chapter.

After running HMRF, one can further view the HMRF spatial clusters (viewHMRFresults2D), and add HMRF annotation to pDataDT table (addHMRF).


The main steps are:

1. Create neighborhood network based on spatial positions
2. Define genes of interest
3. Call HMRF routine to find spatial clusters


******************
Example
******************

.. code-block::
	
	#from seqfish+ dataset
	#100 spatial genes
	HMRF_spatial_genes = doHMRF(gobject = VC_test, expression_values = 'scaled', spatial_genes = my_spatial_genes, spatial_network_name = 'Delaunay_network', k = 9, betas = c(0,1,50), output_folder = paste0(hmrf_folder, '/', 'Spatial_genes/SG_top100_k9_scaled'))
	## view results of HMRF
	for(i in seq(0, 50, by = 1)) {
	viewHMRFresults2D(gobject = VC_test,HMRFoutput = HMRF_spatial_genes,k = 9, betas_to_view = i,point_size = 2)
	}
	## add HMRF of interest to giotto object
	VC_test = addHMRF(gobject = VC_test,HMRFoutput = HMRF_spatial_genes, k = 9, betas_to_add = c(28), hmrf_name = 'HMRF_2')



