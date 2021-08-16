.. _addNetworkLayout: 

#############################
Add Network Layout
#############################

.. describe:: addNetworkLayout()

*Add a network layout for a selected nearest neighbor network.*

.. code-block::

	caddNetworkLayout(
  		gobject,
  		nn_network_to_use = "sNN",
  		network_name = "sNN.pca",
  		layout_type = c("drl"),
  		options_list = NULL,
  		layout_name = "layout",
  		return_gobject = TRUE
	)


**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **nn_network_to_use**	
	  - kNN or sNN
	* - **network_name**	
	  - name of NN network to be used
	* - **layout_type**	
	  - layout algorithm to use
	* - **options_list**	
	  - list of options for selected layout
	* - **layout_name**	
	  - name for layout
	* - **return_gobject**	
	  - boolean: return giotto object (``default = TRUE``)

******************
Value 
******************

Giotto object with updated layout for selected NN network


************************
Details
************************

This function creates layout coordinates based on the provided kNN or sNN. Currently only the force-directed graph layout "drl", see `layout_with_drl <https://rdrr.io/cran/igraph/man/layout_with_drl.html>`_, is implemented. This provides an alternative to tSNE or UMAP based visualizations.