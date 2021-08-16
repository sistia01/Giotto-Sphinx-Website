.. _clusterSpatialCorGenes: 

####################################################
Cluster Genes Using Spatial Information 
####################################################

.. describe:: clusterSpatialCorGenes()

*Cluster based on spatially correlated genes.*

.. code-block::

	clusterSpatialCorGenes(
  		spatCorObject,
  		name = "spat_clus",
  		hclust_method = "ward.D",
  		k = 10,
  		return_obj = TRUE
	)

	
**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - spatCorObject	
	  - spatial correlation object
	* - name	
	  - name for spatial clustering results
	* - hclust_method	
	  - method for hierarchical clustering
	* - k	
	  - number of clusters to extract
	* - return_obj	
	  - return spatial correlation object (spatCorObject)


******************
Value 
******************
A ``spatCorObject`` or cluster result.

