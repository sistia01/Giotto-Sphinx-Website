.. _spatialDE: 

####################################################
Compute Spatial Variables With SpatialDE Method 
####################################################

.. describe:: spatialDE()

*Compute spatial variable genes with spatialDE method*

.. code-block::

	spatialDE(
  		gobject = NULL,
  		expression_values = c("raw", "normalized", "scaled", "custom"),
  		size = c(4, 2, 1),
  		color = c("blue", "green", "red"),
  		sig_alpha = 0.5,
  		unsig_alpha = 0.5,
  		python_path = NULL,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "SpatialDE"
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - Giotto object
	* - expression_values	
	  - gene expression values to use
	* - size	
	  - size of plot
	* - color	
	  - low/medium/high color scheme for plot
	* - sig_alpha	
	  - alpha value for significance
	* - unsig_alpha	
	  - alpha value for insignificance
	* - python_path	
	  - specify specific path to python if required
	* - show_plot	
	  - show plot
	* - return_plot	
	  - return ggplot object
	* - save_plot	
	  - directly save the plot [boolean]
	* - save_param	
	  - list of saving parameters, see `showSaveParameters() <showSaveParameters>`_
	* - default_save_name	
	  - default save name for saving, don't change, change save_name in save_param


******************
Value 
******************

A list of data.frames with results and plot (optional). There are 3 fields reported per gene: LLR, pval, qval. LLR is log-likelihood of model, useful for creating a whole ranking of genes unambiguously. 
P-val, Q-val are useful for cut-off based approach to filtering the spatial genes.

******************
Details 
******************

This is one of methods that Giotto supports to search for spatially variable genes. This function is a wrapper for the SpatialDE method implemented in the `SpatialDE function <https://www.nature.com/articles/nmeth.4636>`_. The input is a gene expression matrix. 
There are 4 version of expression matrix (indicated by expression_values). 
Raw version (in counts) is recommended. SpatialDE performs library size normalization (by default) if raw expression is used. Otherwise, one can also use “normalized” and skip SpatialDE normalization step.

There are no other parameters required. The parameters color, sig_alpha, unsig_alpha are used for plotting the Fraction spatial variance vs Adj. P-value `SpatialDE GitHub <https://github.com/teichlab/spatialde>`__, and is optional. 
To disable this FSV vs. Adj P-value plot, show_plot is set to NA (default). 
The parameters return_plot, save_plot, save_param are for saving the results automatically to disk (default values are NA). They are attached to every function (see CreateGiottoInstructions()).



