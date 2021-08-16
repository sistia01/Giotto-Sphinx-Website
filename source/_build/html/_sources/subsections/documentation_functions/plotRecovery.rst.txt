.. _plotRecovery: 

############################################################
Plot Comparison of Ligand-Receptor Rankings 
############################################################

.. describe:: plotRecovery()

*Plots recovery plot to compare ligand-receptor rankings from spatial and expression information.*

.. code-block::

	plotRecovery(
  		gobject,
  		combCC,
  		expr_rnk_column = "exprPI_rnk",
  		spat_rnk_column = "spatPI_rnk",
  		ground_truth = c("spatial", "expression"),
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "plotRecovery"
	)
	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **combCC**	
	  - combined communication scores from `combCCcom() <combCCcom>`_
	* - **expr_rnk_column**	
	  - column with expression rank information to use
	* - **spat_rnk_column**	
	  - column with spatial rank information to use
	* - **ground_truth**	
	  - what to consider as ground truth (default: spatial)
	* - **show_plot**	
	  - show plots
	* - **return_plot**	
	  - return plotting object
	* - **save_plot**	
	  - directly save the plot [boolean]
	* - **save_param**	
	  - list of saving parameters from `all_plots_save_function() <all_plots_save_function>`_
	* - **default_save_name**	
	  - default save name for saving, don't change, change ``save_name`` in ``save_param``

******************
Value 
******************
A ggplot.

