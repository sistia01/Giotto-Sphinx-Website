.. _removeCellAnnotation: 

####################################################
Remove Cell Annotation 
####################################################

.. describe:: removeCellAnnotation()

*Removes cell annotation of Giotto object.*

.. code-block::

	removeCellAnnotation(gobject, columns = NULL, return_gobject = TRUE)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - columns	
	  - names of columns to remove
	* - return_gobject	
	  - boolean: return Giotto object (default = TRUE)


******************
Value 
******************

A Giotto object. 

******************
Details
******************
If ``return_gobject = FALSE``, it will return the cell metadata


******************
Examples
******************

.. code-block::
	
	
	data(mini_giotto_single_cell) # load full mini giotto object

	# show cell metadata
	pDataDT(mini_giotto_single_cell)
	#>      cell_ID nr_genes perc_genes total_expr leiden_clus cell_types
	#>  1:   cell_2       13         65  111.98320           3     cell C
	#>  2:   cell_7       15         75  115.73030           3     cell C
	#>  3:  cell_12       11         55   95.49802           1     cell A
	#>  4:  cell_15       12         60   99.94782           3     cell C
	#>  5:  cell_17       13         65  111.32963           2     cell B
	#>  6:  cell_30       11         55   96.64302           3     cell C
	#>  7:  cell_37        6         30   57.77777           2     cell B
	#>  8:  cell_40        9         45   82.84693           2     cell B
	#>  9:  cell_44        9         45   79.93838           2     cell B
	#> 10:  cell_53        9         45   82.40747           1     cell A
	#> 11:  cell_64        8         40   73.06345           1     cell A
	#> 12:  cell_74       11         55   93.04295           3     cell C
	#> 13:  cell_85        8         40   73.72574           1     cell A
	#> 14:  cell_86       14         70  115.75186           1     cell A
	#> 15:  cell_90       11         55   93.02181           1     cell A
	#> 16:  cell_95        6         30   59.55714           1     cell A
	#> 17:  cell_96       10         50   88.31757           1     cell A
	#> 18: cell_107       16         80  130.62640           1     cell A
	#> 19: cell_113       12         60   99.83100           2     cell B
	#> 20: cell_118       14         70  117.63523           2     cell B
	# remove cell_types column
	mini_giotto_single_cell = removeCellAnnotation(mini_giotto_single_cell,
                                               columns = 'cell_types')




