.. _spatCellCellcom: 

#############################################################
Calculate Spatial Cell-Cell Communication Scores
############################################################

.. describe:: spatCellCellcom()

*Spatial Cell-Cell communication scores based on spatial expression of interacting cells.*

.. code-block::

	spatCellCellcom(
  		gobject,
  		spatial_network_name = "Delaunay_network",
  		cluster_column = "cell_types",
  		random_iter = 1000,
  		gene_set_1,
  		gene_set_2,
  		log2FC_addendum = 0.1,
  		min_observations = 2,
  		detailed = FALSE,
  		adjust_method = c("fdr", "bonferroni", "BH", "holm", "hochberg", "hommel", "BY",
    			"none"),
  		adjust_target = c("genes", "cells"),
  		do_parallel = TRUE,
  		cores = NA,
  		set_seed = TRUE,
  		seed_number = 1234,
  		verbose = c("a little", "a lot", "none")
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object to use
	* - spatial_network_name	
	  - spatial network to use for identifying interacting cells
	* - cluster_column	
	  - cluster column with cell type information
	* - random_iter	
	  - number of iterations
	* - gene_set_1	
	  - first specific gene set from gene pairs
	* - gene_set_2	
	  - second specific gene set from gene pairs
	* - log2FC_addendum	
	  - addendum to add when calculating log2FC
	* - min_observations	
	  - minimum number of interactions needed to be considered
	* - detailed	
	  - provide more detailed information (random variance and z-score)
	* - adjust_method	
	  - which method to adjust p-values
	* - adjust_target	
	  - adjust multiple hypotheses at the cell or gene level
	* - do_parallel	
	  - run calculations in parallel with mclapply
	* - cores	
	  - number of cores to use if do_parallel = TRUE
	* - set_seed	
	  - set a seed for reproducibility
	* - seed_number	
	  - seed number
	* - verbose	
	  - verbose


******************
Value 
******************
A cell-Cell communication score for gene pairs based on expression only.


************************
Details
************************
Statistical framework to identify if pairs of genes (such as ligand-receptor combinations) are expressed at higher levels than expected based on a reshuffled null distribution of gene expression values in cells that are spatially in proximity to each other.

* LR_comb:Pair of ligand and receptor
* lig_cell_type: cell type to assess expression level of ligand
* lig_expr: average expression of ligand in lig_cell_type
* ligand: ligand name
* rec_cell_type: cell type to assess expression level of receptor
* rec_expr: average expression of receptor in rec_cell_type
* receptor: receptor name
* LR_expr: combined average ligand and receptor expression
* lig_nr: total number of cells from lig_cell_type that spatially interact with cells from rec_cell_type
* rec_nr: total number of cells from rec_cell_type that spatially interact with cells from lig_cell_type
* rand_expr: average combined ligand and receptor expression from random spatial permutations
* av_diff: average difference between LR_expr and rand_expr over all random spatial permutations
* sd_diff: (optional) standard deviation of the difference between LR_expr and rand_expr over all random spatial permutations
* z_score: (optinal) z-score
* log2fc: log2 fold-change (LR_expr/rand_expr)
* pvalue: p-value
* LR_cell_comb: cell type pair combination
* p.adj: adjusted p-value
* PI: significance score: log2fc * -log10(p.adj)

