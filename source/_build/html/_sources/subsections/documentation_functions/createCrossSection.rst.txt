.. _createCrossSection: 

##############################################################
Create a Virtual Cross Section 
##############################################################

.. describe:: createCrossSection()

*Create a virtual 2D cross section.*

.. code-block::

	createCrossSection(
  		gobject,
  		name = "cross_section",
  		spatial_network_name = "Delaunay_network",
  		thickness_unit = c("cell", "natural"),
  		slice_thickness = 2,
  		cell_distance_estimate_method = "mean",
  		extend_ratio = 0.2,
  		method = c("equation", "3 points", "point and norm vector",
    			"point and two plane vectors"),
  		equation = NULL,
  		point1 = NULL,
  		point2 = NULL,
  		point3 = NULL,
  		normVector = NULL,
  		planeVector1 = NULL,
  		planeVector2 = NULL,
  		mesh_grid_n = 20,
  		return_gobject = TRUE
	)


.. _arguments_createCrossSection:
	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 


	* - **gobject**	
	  - giotto object
	* - **name**	
	  - name of cress section object. (default = cross_sectino)
	* - **spatial_network_name**	
	  - name of spatial network object. (default = Delaunay_network)
	* - **thickness_unit**	
	  - unit of the virtual section thickness. If "cell", average size of the observed cells is used as length unit. If "natural", the unit of cell location coordinates is used.(default = cell	
	* - **slice_thickness**	
	  - thickness of slice. default = 2
	* - **cell_distance_estimate_method**	
	  - method to estimate average distance between neighboring cells. (default = mean)
	* - **extend_ratio**	
	  - deciding the span of the cross section mesh-grid, as a ratio of extension compared to the borders of the virtual tissue section. (default = 0.2)
	* - **method**	
	  - method to define the cross section plane. If equation, the plane is defined by a four element numerical vector (equation) in the form of c(A,B,C,D), corresponding to a plane with equation Ax+By+Cz=D. If 3 points, the plane is define by the coordinates of 3 points, as given by point1, point2, and point3. If point and norm vector, the plane is defined by the coordinates of one point (point1) in the plane and the coordinates of one norm vector (normVector) to the plane. If point and two plane vector, the plane is defined by the coordinates of one point (point1) in the plane and the coordinates of two vectors (planeVector1, planeVector2) in the plane. (default = equation)
	* - **equation**	
	  - equation required by method "equation".equations needs to be a numerical vector of length 4, in the form of c(A,B,C,D), which defines plane Ax+By+Cz=D.
	* - **point1**	
	  - coordinates of the first point required by method "3 points","point and norm vector", and "point and two plane vectors".
	* - **point2**	
	  - coordinates of the second point required by method "3 points"
	* - **point3**	
	  - coordinates of the third point required by method "3 points"
	* - **normVector**	
	  - coordinates of the norm vector required by method "point and norm vector"
	* - **planeVector1**	
	  - coordinates of the first plane vector required by method "point and two plane vectors"
	* - **planeVector2**	
	  - coordinates of the second plane vector required by method "point and two plane vectors"
	* - **mesh_grid_n**	
	  - number of mesh-grid lines to generate along both directions for the cross section plane.
	* - **return_gobject**	
	  - boolean: return Giotto object (default = TRUE)


******************
Value 
******************
A giotto object with updated spatial network slot.

******************
Details 
******************
Creates a virtual 2D cross section object for a given spatial network object. The users need to provide the definition of the cross section plane (See method in `Arguments Section <arguments_createCrossSection>`_ for more information).
