.. _plotICG: 

#########################################################################
Visualize ICGs via Barplot
#########################################################################

.. describe:: plotICG()

*Create barplot to visualize interaction changed genes.*

.. code-block::

	plotInteractionChangedGenes(
  		gobject,
  		cpgObject,
  		source_type,
  		source_markers,
  		ICG_genes,
  		cell_color_code = NULL,
  		show_plot = NA,
  		return_plot = NA,
  		save_plot = NA,
  		save_param = list(),
  		default_save_name = "plotICG"
	)


**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 


	* - **gobject**	
	  - giotto object
	* - **cpgObject**	
	  - ICG (interaction changed gene) score object
	* - **source_type**	
	  - cell type of the source cell
	* - **source_markers**	
	  - markers for the source cell type
	* - **ICG_genes**	
	  - named character vector of ICG genes
	* - **cell_color_code**	
	  - cell color code for the interacting cell types
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


#########
Value
#########
A plot.
