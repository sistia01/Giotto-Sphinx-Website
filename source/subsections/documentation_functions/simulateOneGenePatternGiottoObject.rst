.. _simulateOneGenePatternGiottoObject: 

####################################################
Create Simulated Spatial Pattern
####################################################

.. describe:: simulateOneGenePatternGiottoObject()

*Create a simulated spatial pattern for one selected gene.*

.. code-block::

	simulateOneGenePatternGiottoObject(
  		gobject,
  		pattern_name = "pattern",
  		pattern_cell_ids = NULL,
  		gene_name = NULL,
  		spatial_prob = 0.95,
  		gradient_direction = NULL,
  		show_pattern = TRUE,
  		pattern_colors = c(`in` = "green", out = "red"),
  		...
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - gobject	
	  - giotto object
	* - pattern_name	
	  - name of spatial pattern
	* - pattern_cell_ids	
	  - cell ids that make up the spatial pattern
	* - gene_name	
	  - selected gene
	* - spatial_prob	
	  - probability for a high expressing gene value to be part of the spatial pattern
	* - gradient_direction	
	  - direction of gradient
	* - show_pattern	
	  - show the discrete spatial pattern
	* - pattern_colors	
	  - 2 color vector for the spatial pattern
	* - ...	
	  - additional parameters for (re-)normalizing




******************
Value 
******************

A reprocessed Giotto object for which one gene has a forced spatial pattern. 


