.. _fDataDT: 

#############################
Show Gene Metadata
#############################

.. describe:: fDataDT()

*Show cell metadata.*

.. code-block::

	fDataDT(gobject)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object

******************
Value 
******************
A data.table` with gene metadata.

*********************
Examples
*********************
.. code-block::
		
	data(mini_giotto_single_cell) # loads existing Giotto object
	fDataDT(mini_giotto_single_cell)
	#>     gene_ID nr_cells perc_cells total_expr mean_expr mean_expr_det hvg
	#>  1:   Cldn5        6         30   48.92244  2.446122      8.153740 yes
	#>  2:   Rtn4r       13         65  110.74429  5.537215      8.518792 yes
	#>  3:     Vgf       15         75  132.75484  6.637742      8.850322  no
	#>  4:  Lingo1       15         75  147.21239  7.360619      9.814159  no
	#>  5: Slc17a7       17         85  170.21651  8.510826     10.012736  no
	#>  6:   Lynx1       10         50   78.57677  3.928838      7.857677  no
	#>  7:  Atp1a1       17         85  165.49466  8.274733      9.734980  no
	#>  8:    Scg3       10         50   83.22481  4.161240      8.322481 yes
	#>  9:    Myh9        9         45   74.30740  3.715370      8.256378  no
	#> 10:  Pcp4l1       11         55   89.43319  4.471660      8.130290  no
	#> 11:    Pygb       11         55   93.51979  4.675990      8.501799  no
	#> 12:  Col4a2       10         50   82.04459  4.102229      8.204459 yes
	#> 13:    Sdc4       10         50   83.86661  4.193330      8.386661 yes
	#> 14:   Csf1r        9         45   68.17674  3.408837      7.575193  no
	#> 15:  Mtss1l       12         60   97.81416  4.890708      8.151180 yes
		#> 16: Slc32a1        5         25   45.07783  2.253892      9.015567 yes
	#> 17:  Adarb2        6         30   44.55620  2.227810      7.426034 yes
	#> 18:   Abtb2        7         35   51.22157  2.561079      7.317368  no
	#> 19:   Htra1       10         50   83.31959  4.165979      8.331959 yes
	#> 20:   Cplx1       15         75  128.19130  6.409565      8.546087  no
