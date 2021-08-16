.. _plotCombineCPG: 

#########################################################################
Visualize Combined ICG Scores 
#########################################################################

.. describe:: plotCombineCPG()

*Create visualization for combined (pairwise) ICG scores.*

.. code-block::

	plotCombineCPG(...)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 1 


	* - ... 
	  - Arguments passed on to `plotCombineICG() <plotCombineICG>`_
	* - **gobject**	
	  - giotto object
	* - **combCpgObject**	
	  - ICGscores, output from combineInteractionChangedGenes()
	* - **selected_interactions**	
	  - interactions to show
	* - **selected_gene_to_gene**	
	  - pairwise gene combinations to show
	* - **detail_plot**	
	  - show detailed info in both interacting cell types
	* - **simple_plot**	
	  - show a simplified plot
	* - **simple_plot_facet**	
	  - facet on interactions or genes with simple plot
	* - **facet_scales**	
	  - ggplot facet scales paramter
	* - **facet_ncol**	
	  - ggplot facet ncol parameter
	* - **facet_nrow**	
	  - ggplot facet nrow parameter
	* - **colors**	
	  - vector with two colors to use
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

.. seealso::
	`plotCombineICG() <plotCombineICG>`_.
