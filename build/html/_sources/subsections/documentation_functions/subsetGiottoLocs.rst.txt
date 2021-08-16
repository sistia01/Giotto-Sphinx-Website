.. _subsetGiottoLocs: 

#############################
Subset Giotto Locations
#############################

.. describe:: subsetGiottoLocs()

*Subsets Giotto object based on spatial locations.*

.. code-block::

	subsetGiottoLocs(
  		gobject,
  		x_max = NULL,
 		 x_min = NULL,
  		y_max = NULL,
  		y_min = NULL,
  		z_max = NULL,
  		z_min = NULL,
  		return_gobject = T,
  		verbose = FALSE
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **x_max**	
	  - maximum x-coordinate
	* - **x_min**	
	  - minimum x-coordinate
	* - **y_max**	
	  - maximum y-coordinate
	* - **y_min**	
	  - minimum y-coordinate
	* - **z_max**	
	  - maximum z-coordinate
	* - **z_min**	
	  - minimum z-coordinate
	* - **return_gobject**	
	  - return Giotto object
	* - **verbose**	
	  - be verbose

******************
Value 
******************

Giotto Object

***************
Details
***************

If ``return_gobject = FALSE``, then a filtered combined metadata ``data.table`` will be returned

************************
Examples
************************

.. code-block::
	
	# \donttest{

	data(mini_giotto_single_cell)

	# spatial plot
	spatPlot(mini_giotto_single_cell)



.. image:: /images/documentation/subsetGiottoLocs-1.png
	:width: 500
	:alt: subsetGiottoLocs

.. image:: /images/documentation/subsetGiottoLocs-2.png
	:width: 500
	:alt: subsetGiottoLocs

.. code-block::

	# subset giotto object based on spatial locations
	subset_obj = subsetGiottoLocs(mini_giotto_single_cell,
	x_max = 1500, x_min = 1000,
	y_max = -500, y_min = -1000)
	# spatial plot of subset giotto object
	spatPlot(subset_obj)
	# }


.. image:: /images/documentation/subsetGiottoLocs-3.png
	:width: 500
	:alt: subsetGiottoLocs 


.. image:: /images/documentation/subsetGiottoLocs-4.png
	:width: 500
	:alt: subsetGiottoLocs




