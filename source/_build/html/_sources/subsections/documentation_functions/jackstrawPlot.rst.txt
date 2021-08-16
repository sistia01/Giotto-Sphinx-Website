.. _jackstrawPlot: 

###########################################
Identify Significant PCs 
###########################################

.. describe:: jackstrawPlot()

*Identify significant principal components (PCs).*


.. code-block::

	jackstrawPlot(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		reduction = c("cells", "genes"),
  		genes_to_use = NULL,
  		center = FALSE,
  		scale_unit = FALSE,
  		ncp = 20,
  		ylim = c(0, 1),
  		iter = 10,
  		threshold = 0.01,
  		verbose = TRUE,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "jackstrawPlot"
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
	* - **reduction**	
	  - cells or genes
	* - **genes_to_use**	
	  - subset of genes to use for PCA
	* - **center**	
	  - center data before PCA
	* - **scale_unit**	
	  - scale features before PCA
	* - **ncp**	
	  - number of principal components to calculate
	* - **ylim**	
	  - y-axis limits on jackstraw plot
	* - **iter**	
	  - number of interactions for jackstraw
	* - **threshold**	
	  - p-value threshold to call a PC significant
	* - **verbose**	
	  - show progress of jackstraw method
	* - **show_plot**	
	  - show plot
	* - **return_plot**	
	  - return ggplot object
	* - **save_plot**
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters from `all_plots_save_function() <all_plots_save_function>`_
	* - **default_save_name**	
	  - default save name for saving, don't change, change ``save_name`` in ``save_param``


******************
Value 
******************
ggplot object for jackstraw method.

************************
Details
************************
The Jackstraw method uses the `permutationPA() <permutationPA>`_ function. By systematically permuting genes it identifies robust, and thus significant, PCs. 


***********************
Examples
***********************
.. important:: 
	
	**When using 'jackstraw' to identify significant PCs:** If used in published research, please cite: Neo Christopher Chung and John D. Storey (2014). 'Statistical significance of variables driving systematic variation in high-dimensional data. Bioinformatics

.. code-block::

	# \donttest{

	data(mini_giotto_single_cell)

	# jackstraw package is required to run
	jackstrawPlot(mini_giotto_single_cell, ncp = 10)

	#> Estimating a number of significant principal component: #> 1  2  3  4  5  6  7  8  9  10  number of estimated significant components:  0 
	# }


**ADD IMAGE**

