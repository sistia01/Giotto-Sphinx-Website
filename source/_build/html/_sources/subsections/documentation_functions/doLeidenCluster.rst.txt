.. _doLeidenCluster: 

#################################################
Cluster Cells Using NN-Network
#################################################

.. describe:: doLeidenCluster()

*Cluster cells using a NN-network and the Leiden community detection algorithm.*

.. code-block::

	doLeidenCluster(
  		gobject,
  		name = "leiden_clus",
  		nn_network_to_use = "sNN",
  		network_name = "sNN.pca",
  		python_path = NULL,
  		resolution = 1,
  		weight_col = "weight",
  		partition_type = c("RBConfigurationVertexPartition", "ModularityVertexPartition"),
  		init_membership = NULL,
  		n_iterations = 1000,
  		return_gobject = TRUE,
  		set_seed = T,
  		seed_number = 1234
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **name**	
	  - name for cluster
	* - **nn_network_to_use**	
	  - type of NN network to use (kNN vs sNN)
	* - **network_name**	
	  - name of NN network to use
	* - **python_path**	
	  - specify specific path to python if required
	* - **resolution**	
	  - resolution
	* - **weight_col**	
	  - weight column to use for edges
	* - **partition_type**	
	  - The type of partition to use for optimisation.
	* - **init_membership**	
	  - initial membership of cells for the partition
	* - **n_iterations**	
	  - number of interations to run the Leiden algorithm. If the number of iterations is negative, the Leiden algorithm is run until an iteration in which there was no improvement.
	* - **return_gobject**	
	  - boolean: return giotto object (default = TRUE)
	* - **set_seed**	
	  - set seed
	* - **seed_number**	
	  - number for seed


*******************
Value
*******************
Giotto object with new clusters appended to cell metadata


*******************
Details
*******************

This function is a wrapper for the Leiden algorithm implemented in python, which can detect communities in graphs of millions of nodes (cells), as long as they can fit in memory. See the `leidenalg Github page <https://github.com/vtraag/leidenalg>`_ or the `leidenalg readthedocs page <https://leidenalg.readthedocs.io/en/stable/index.html>`_ for more information.

Partition types available and information:

* RBConfigurationVertexPartition: Implements Reichardt and Bornholdt’s Potts model with a configuration null model. This quality function is well-defined only for positive edge weights. This quality function uses a linear resolution parameter.
* ModularityVertexPartition: Implements modularity. This quality function is well-defined only for positive edge weights. It does not use the resolution parameter

Set ``weight_col = NULL`` to give equal weight (=1) to each edge.