.. _createGiottoInstructions: 

#############################
Create Giotto Instructions
#############################

.. describe:: createGiottoInstructions()

*Function to set global instructions for Giotto functions.*

.. code-block::

	createGiottoInstructions(
 		python_path = NULL,
  		show_plot = NULL,
  		return_plot = NULL,
  		save_plot = NULL,
  		save_dir = NULL,
  		plot_format = NULL,
  		dpi = NULL,
  		units = NULL,
  		height = NULL,
  		width = NULL,
  		is_docker = FALSE
	)

**********************
Arguements
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **python_path**	
	  - path to python binary to use
	* - **show_plot**	
	  - print plot to console, default = TRUE
	* - **return_plot**	
	  - return plot as object, default = TRUE
	* - **save_plot**	
	  - automatically save plot, dafault = FALSE
	* - **save_dir**	
	  - path to directory where to save plots
	* - **plot_format**	
	  - format of plots (defaults to png)
	* - **dpi**	
	  - resolution for raster images
	* - **units**	
	  - units of format (defaults to in)
	* - **height**	
	  - height of plots
	* - **width**	
	  - width of plots
	* - **is_docker**	
 	  - using docker implementation of Giotto (defaults to FALSE)

******************
Value 
******************
Named vector with Giotto instructions


.. seealso::

	More information can be found here in `"How to Visualize and Save Plots in Giotto" <visualize-data>`__.

