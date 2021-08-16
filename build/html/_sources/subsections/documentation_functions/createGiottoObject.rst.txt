.. _createGiottoObject: 

#######################
Create a Giotto Object 
#######################

.. describe:: createGiottoObject()

*Function to create a Giotto Object.*

.. code-block::

	createGiottoObject(
  		raw_exprs,
  		spatial_locs = NULL,
  		norm_expr = NULL,
  		norm_scaled_expr = NULL,
  		custom_expr = NULL,
  		cell_metadata = NULL,
  		gene_metadata = NULL,
  		spatial_network = NULL,
  		spatial_network_name = NULL,
  		spatial_grid = NULL,
  		spatial_grid_name = NULL,
  		spatial_enrichment = NULL,
  		spatial_enrichment_name = NULL,
  		dimension_reduction = NULL,
  		nn_network = NULL,
  		images = NULL,
  		offset_file = NULL,
  		instructions = NULL,
  		cores = NA
	)

**********************
Arguements
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **raw_exprs**
	  - matrix with raw expression counts [required]
	* - **spatial_locs**	
	  - data.table or data.frame with coordinates for cell centroids
	* - **norm_expr**	
	  - normalized expression values
	* - **norm_scaled_expr**	
	  - scaled expression values
	* - **custom_expr**	
	  - custom expression values
	* - **cell_metadata**	
	  - cell annotation metadata
	* - **gene_metadata**	
	  - gene annotation metadata
	* - **spatial_network**	
	  - list of spatial network(s)
	* - **spatial_network_name**	
	  - list of spatial network name(s)
	* - **spatial_grid**	
	  - list of spatial grid(s)
	* - **spatial_grid_name**	
	  - list of spatial grid name(s)
	* - **spatial_enrichment**	
	  - list of spatial enrichment score(s) for each spatial region
	* - **spatial_enrichment_name**	
	  - list of spatial enrichment name(s)
	* - **dimension_reduction**	
	  - list of dimension reduction(s)
	* - **nn_network**	
	  - list of nearest neighbor network(s)
	* - **images**	
	  - list of images
	* - **offset_file**	
	  - file used to stitch fields together (optional)
	* - **instructions**	
	  - list of instructions or output result from `createGiottoInstructions <createGiottoInstructions>`_
	* - **cores**	
	  - how many cores or threads to use to read data if paths are provided

******************
Value 
******************
Giotto Object 

************************
Details
************************

[**Requirements**] To create a giotto object you need to provide at least a matrix with genes as row names and cells as column names. This matrix can be provided as a base matrix, sparse Matrix, data.frame, data.table or as a path to any of those. To include spatial information about cells (or regions) you need to provide a matrix, data.table or data.frame (or path to them) with coordinates for all spatial dimensions. This can be 2D (x and y) or 3D (x, y, x). The row order for the cell coordinates should be the same as the column order for the provided expression data.

[**Instructions**] Additionally an instruction file, generated manually or with `createGiottoInstructions <createGiottoInstructions>`_ can be provided to instructions, if not a default instruction file will be created for the Giotto object.

[**Multiple fields**] In case a dataset consists of multiple fields, like seqFISH+ for example, an offset file can be provided to stitch the different fields together. `stitchFieldCoordinates <stitchFieldCoordinates>`_ can be used to generate such an offset file.

[**Processed data**] Processed count data, such as normalized data, can be provided using one of the different expression slots (norm_expr, norm_scaled_expr, custom_expr).

[**Metadata**] Cell and gene metadata can be provided using the cell and gene metadata slots. This data can also be added afterwards using the `addGeneMetadata <addGeneMetadata>`_ or `addCellMetadata <addCellMetadata>`_ functions.

[**Other Information**] Additional information can be provided through the appropriate slots:

* Spatial networks
* Spatial girds
* Spatial enrichments
* Dimensions reductions
* Nearest neighbours networks
* Images
