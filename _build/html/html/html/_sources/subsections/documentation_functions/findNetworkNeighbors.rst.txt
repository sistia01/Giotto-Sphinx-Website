.. _findNetworkNeighbors: 

#############################
Find Spatial Neighbors
#############################

.. describe:: findNetworkNeighbors()

*Find the spatial neighbors for a selected group of cells within the selected spatial network.*

.. code-block::

	findNetworkNeighbors(
  		gobject,
  		spatial_network_name,
  		source_cell_ids = NULL,
  		name = "nb_cells"
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - Giotto object
	* - **spatial_network_name**	
	  - name of spatial network
	* - **source_cell_ids**	
	  - cell ids for which you want to know the spatial neighbors
	* - **name**	
	  - name of the results

******************
Value 
******************

A data.table.

*****************
Examples
*****************

.. code-block::

	data(mini_giotto_single_cell)

	# get all cells
	all_cells = slot(mini_giotto_single_cell, 'cell_ID')

	# find all the spatial neighbours for the first 5 cells
	# within the Delaunay network
	findNetworkNeighbors(mini_giotto_single_cell,
                     spatial_network_name = 'Delaunay_network',
                     source_cell_ids = all_cells[1:5])
	#>      cell_ID nb_cells
	#>  1:   cell_2     both
	#>  2:   cell_7     both
	#>  3:  cell_12     both
	#>  4:  cell_15     both
	#>  5:  cell_17   source
	#>  6:  cell_30 neighbor
	#>  7:  cell_37   others
	#>  8:  cell_40   others
	#>  9:  cell_44   others
	#> 10:  cell_53   others
	#> 11:  cell_64   others
	#> 12:  cell_74   others
	#> 13:  cell_85 neighbor
	#> 14:  cell_86   others
	#> 15:  cell_90   others
	#> 16:  cell_95 neighbor
	#> 17:  cell_96 neighbor
	#> 18: cell_107 neighbor
	#> 19: cell_113 neighbor
	#> 20: cell_118   others
