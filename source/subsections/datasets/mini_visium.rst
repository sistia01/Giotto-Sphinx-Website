.. _mini_visium:

####################
mini Visium  
####################

.. code-block:: 

    library(Giotto)

************************
Install Python Modules
************************

To run this vignette you need to install **all** of the necessary Python modules. 

.. important::
	
	Python module installation can be done either **automatically** via our installation tool (from within R) (see step 2.2A) or **manually** (see step 2.2B). 

	:octicon:`eye` See :ref:`Part 2.2 Giotto-Specific Python Packages <part2_python_giotto_requirements>` of our Giotto Installation section for step-by-step instructions. 

***************************************
*Optional: Set Giotto Instructions*
***************************************

.. code-block::

    # to automatically save figures in save_dir set save_plot to TRUE
    temp_dir = getwd()
    temp_dir = '~/Temp/'
    myinstructions = createGiottoInstructions(save_dir = temp_dir,
                                          save_plot = TRUE, 
                                          show_plot = FALSE)

*******************************
1. Working with Giotto Object
*******************************

1.1 Create Giotto Object 
===========================

Minimum Requirements: 
--------------------------
- Matrix with expression information (or path to)
- x,y(,z) coordinates for cells or spots (or path to)

.. code-block:: 

    # giotto object 
	expr_path = system.file("extdata", "visium_DG_expr.txt.gz", package = 'Giotto')
	loc_path = system.file("extdata", "visium_DG_locs.txt", package = 'Giotto')
	mini_visium <- createGiottoObject(raw_exprs = expr_path,
                                   	spatial_locs = loc_path,
                                   	instructions = myinstructions)

How to work with Giotto instructions that are part of your Giotto object:

- Show the instructions associated with your Giotto object with **showGiottoInstructions**
- Change one or more instructions with **changeGiottoInstructions**
- Replace all instructions at once with **replaceGiottoInstructions**
- Read or get a specific giotto instruction with **readGiottoInstructions**

*Note: The python path can only be set once in an R session. See the **reticulate package** for more information.*


.. code-block::

	# show instructions associated with giotto object (mini_visium)
	showGiottoInstructions(mini_visium)

1.2 Add Image
==================

.. code-block::

	## 1. read image
	png_path = system.file("extdata", "deg_image.png", package = 'Giotto')
	mg_img = magick::image_read(png_path)

	## 2. test and modify image alignment
	mypl = spatPlot(mini_visium, return_plot = T, point_alpha = 0.8)
	orig_png = createGiottoImage(gobject = mini_visium, mg_object = mg_img, name = 'image',
                             	xmax_adj = 450, xmin_adj = 550,
                             	ymax_adj = 200, ymin_adj = 200)
	mypl_image = addGiottoImageToSpatPlot(mypl, orig_png)
	mypl_image

	## 3. add images to Giotto object ##
	image_list = list(orig_png)
	mini_visium = addGiottoImage(gobject = mini_visium,
                             	images = image_list)
	showGiottoImageNames(mini_visium)

*********************
2. Processing Steps
*********************

* Filter genes and cells based on detection frequencies
* Normalize expression matrix (log transformation, scaling factor and/or z-scores)
* Add cell and gene statistics (optional)
* Adjust expression matrix for technical covariates or batches (optional). These results will be stored in the custom slot.

.. code-block::

	# explore gene and cell distribution
	filterDistributions(mini_visium, detection = 'genes')
	filterDistributions(mini_visium, detection = 'cells')
	filterCombinations(mini_visium,
                   	expression_thresholds = c(1),
                   	gene_det_in_min_cells = c(20, 20, 50, 50),
                   	min_det_genes_per_cell = c(100, 200, 100, 200))

	# filter and normalize
	mini_visium <- filterGiotto(gobject = mini_visium,
                            	expression_threshold = 1,
                            	gene_det_in_min_cells = 50,
                            	min_det_genes_per_cell = 100,
                            	expression_values = c('raw'),
                            	verbose = T)
	mini_visium <- normalizeGiotto(gobject = mini_visium, scalefactor = 6000, verbose = T)
	mini_visium <- addStatistics(gobject = mini_visium)


*************************************
3. Dimension Reduction 
*************************************

* Identify highly variable genes (HVG)
* Perform PCA
* Identify number of significant prinicipal components (PCs)
* Run UMAP and/or TSNE on PCs (or directly on matrix)

.. code-block::

	mini_visium <- calculateHVG(gobject = mini_visium)

	mini_visium <- runPCA(gobject = mini_visium)
	screePlot(mini_visium, ncp = 30)
	plotPCA(gobject = mini_visium)

	mini_visium <- runUMAP(mini_visium, dimensions_to_use = 1:10)
	plotUMAP(gobject = mini_visium)
	mini_visium <- runtSNE(mini_visium, dimensions_to_use = 1:10)
	plotTSNE(gobject = mini_visium)


*********************************
4. Clustering 
*********************************

* Create a shared (default) nearest network in PCA space (or directly on matrix)
* Cluster on nearest network with Leiden or Louvan (kmeans and hclust are alternatives)

.. code-block::

	mini_visium <- createNearestNetwork(gobject = mini_visium, dimensions_to_use = 1:10, k = 15)
	mini_visium <- doLeidenCluster(gobject = mini_visium, resolution = 0.4, n_iterations = 1000)

	pDataDT(mini_visium)

	# visualize UMAP cluster results
	plotUMAP(gobject = mini_visium, cell_color = 'leiden_clus', show_NN_network = T, point_size = 2.5)

	# visualize UMAP and spatial results
	spatDimPlot(gobject = mini_visium, cell_color = 'leiden_clus', spat_point_shape = 'voronoi')

	# heatmap and dendrogram
	showClusterHeatmap(gobject = mini_visium, cluster_column = 'leiden_clus')
	showClusterDendrogram(mini_visium, h = 0.5, rotate = T, cluster_column = 'leiden_clus')

*********************************
5. Differential Expression 
*********************************

.. code-block::

	scran_markers = findMarkers_one_vs_all(gobject = mini_visium,
                                       	method = 'scran',
                                       	expression_values = 'normalized',
                                       	cluster_column = 'leiden_clus')
	# violinplot
	topgenes_scran = scran_markers[, head(.SD, 2), by = 'cluster']$genes
	violinPlot(mini_visium, genes = topgenes_scran, cluster_column = 'leiden_clus',
           	strip_text = 10, strip_position = 'right')

	# metadata heatmap
	topgenes_scran = scran_markers[, head(.SD, 6), by = 'cluster']$genes
	plotMetaDataHeatmap(mini_visium, selected_genes = topgenes_scran,
                    	metadata_cols = c('leiden_clus'))

*********************************
6. Cell Type Annotation 
*********************************

.. code-block::

	
	clusters_cell_types = c('Gfap_cells', 'Tbr1_cells', 'Tcf7l2_cells', 'Wfs1_cells', 'Nptxr_cells')
	names(clusters_cell_types) = 1:5
	mini_visium = annotateGiotto(gobject = mini_visium, annotation_vector = clusters_cell_types,
                             	cluster_column = 'leiden_clus', name = 'cell_types')

	# check new cell metadata
	pDataDT(mini_visium)

	# visualize annotations
	spatDimPlot(gobject = mini_visium, cell_color = 'cell_types', spat_point_size = 3, dim_point_size = 3)

*****************************
7. Spatial Grid
*****************************
7.1 Create a Spatial Grid
==========================

 
Create a grid based on defined stepsizes in the x,y(,z) axes.

.. code-block::

	mini_visium <- createSpatialGrid(gobject = mini_visium,
                                 sdimx_stepsize = 300,
                                 sdimy_stepsize = 300,
                                 minimum_padding = 50)
	showGrids(mini_visium)
	spatPlot(gobject = mini_visium, show_grid = T, point_size = 1.5)

	# extract grid and associated metadata spots
	annotated_grid = annotateSpatialGrid(mini_visium)
	annotated_grid_metadata = annotateSpatialGrid(mini_visium,
                                              cluster_columns = c('leiden_clus', 'cell_types', 'nr_genes'))


7.2 Spatial Enrichment: Cell-Type Distribution 
================================================
Here we will use known markers for different mouse brain cell types to identify which cell types are enriched in the individual spots or identified clusters.

`Paper: eisel, A. et al. Molecular Architecture of the Mouse Nervous System. Cell 174, 999-1014.e22 (2018). <https://www.biorxiv.org/content/10.1101/294918v2>`_

.. code-block::

	## cell type signatures ##
	## combination of all marker genes identified in Zeisel et al
	sign_matrix_path = system.file("extdata", "sig_matrix.txt", package = 'Giotto')
	brain_sc_markers = data.table::fread(sign_matrix_path) # file don't exist in data folder
	sig_matrix = as.matrix(brain_sc_markers[,-1]); rownames(sig_matrix) = brain_sc_markers$Event

	## enrichment tests
	mini_visium = runSpatialEnrich(mini_visium, 
                               	sign_matrix = sig_matrix, 
                               	enrich_method = 'PAGE') #default = 'PAGE'

	## heatmap of enrichment versus annotation (e.g. clustering result)
	cell_types = colnames(sig_matrix)
	plotMetaDataCellsHeatmap(gobject = mini_visium,
                         	metadata_cols = 'leiden_clus',
                         	value_cols = cell_types,
                         	spat_enr_names = 'PAGE',
                         	x_text_size = 8, y_text_size = 8)


	enrichment_results = mini_visium@spatial_enrichment$PAGE
	enrich_cell_types = colnames(enrichment_results)
	enrich_cell_types = enrich_cell_types[enrich_cell_types != 'cell_ID']

	## spatplot
	spatCellPlot(gobject = mini_visium, spat_enr_names = 'PAGE',
             	cell_annotation_values = enrich_cell_types,
             	cow_n_col = 3,coord_fix_ratio = NULL, point_size = 1)

*********************
8. Spatial Network 
*********************

* Visualize information about the default Delaunay network
* Create a spatial Delaunay network (default)
* Create a spatial kNN network

.. code-block::

	
	plotStatDelaunayNetwork(gobject = mini_visium, maximum_distance = 300)
	mini_visium = createSpatialNetwork(gobject = mini_visium, minimum_k = 2, maximum_distance_delaunay = 400)
	mini_visium = createSpatialNetwork(gobject = mini_visium, minimum_k = 2, method = 'kNN', k = 10)
	showNetworks(mini_visium)

	# visualize the two different spatial networks  
	spatPlot(gobject = mini_visium, show_network = T,
         	network_color = 'blue', spatial_network_name = 'Delaunay_network',
         	point_size = 2.5, cell_color = 'leiden_clus')

	spatPlot(gobject = mini_visium, show_network = T,
         	network_color = 'blue', spatial_network_name = 'kNN_network',
         	point_size = 2.5, cell_color = 'leiden_clus')

***********************
9. Spatial Genes 
***********************

Identify spatial genes with 3 different methods:

- binSpect with kmeans binarization (default)
- binSpect with rank binarization
- silhouetteRank

Visualize top 4 genes per method.

.. code-block::

	km_spatialgenes = binSpect(mini_visium)
	spatGenePlot(mini_visium, expression_values = 'scaled', 
             	genes = km_spatialgenes[1:4]$genes,
             	point_shape = 'border', point_border_stroke = 0.1,
             	show_network = F, network_color = 'lightgrey', point_size = 2.5,
             	cow_n_col = 2)

	rank_spatialgenes = binSpect(mini_visium, bin_method = 'rank')
	spatGenePlot(mini_visium, expression_values = 'scaled', 
             	genes = rank_spatialgenes[1:4]$genes,
             	point_shape = 'border', point_border_stroke = 0.1,
             	show_network = F, network_color = 'lightgrey', point_size = 2.5,
             	cow_n_col = 2)


	silh_spatialgenes = silhouetteRank(gobject = mini_visium) # TODO: suppress print output
	spatGenePlot(mini_visium, expression_values = 'scaled', 
             	genes = silh_spatialgenes[1:4]$genes,
             	point_shape = 'border', point_border_stroke = 0.1,
             	show_network = F, network_color = 'lightgrey', point_size = 2.5,
             	cow_n_col = 2)


***********************************
10. Spatial Co-Expression Patterns
***********************************

Identify robust spatial co-expression patterns using the spatial network or grid and a subset of individual spatial genes.

10.1 Calculate Spatial Correlation Scores
===============================================

.. code-block::

	# 1. calculate spatial correlation scores 
	ext_spatial_genes = km_spatialgenes[1:100]$genes
	spat_cor_netw_DT = detectSpatialCorGenes(mini_visium,
                                         	method = 'network', spatial_network_name = 'Delaunay_network',
                                         	subset_genes = ext_spatial_genes)


10.2 Cluster Correlation Scores
===============================================

.. code-block::

	# 2. cluster correlation scores
	spat_cor_netw_DT = clusterSpatialCorGenes(spat_cor_netw_DT, name = 'spat_netw_clus', k = 8)
	heatmSpatialCorGenes(mini_visium, spatCorObject = spat_cor_netw_DT, use_clus_name = 'spat_netw_clus')


	netw_ranks = rankSpatialCorGroups(mini_visium, spatCorObject = spat_cor_netw_DT, use_clus_name = 'spat_netw_clus')
	top_netw_spat_cluster = showSpatialCorGenes(spat_cor_netw_DT, use_clus_name = 'spat_netw_clus',
                                            selected_clusters = 6, show_top_genes = 1)

	cluster_genes_DT = showSpatialCorGenes(spat_cor_netw_DT, use_clus_name = 'spat_netw_clus', show_top_genes = 1)
	cluster_genes = cluster_genes_DT$clus; names(cluster_genes) = cluster_genes_DT$gene_ID

	mini_visium = createMetagenes(mini_visium, gene_clusters = cluster_genes, name = 'cluster_metagene')
		spatCellPlot(mini_visium,
             	spat_enr_names = 'cluster_metagene',
             	cell_annotation_values = netw_ranks$clusters,
             	point_size = 1.5, cow_n_col = 3)


****************************
11. Spatial HMRF Domains
****************************

.. code-block::

	hmrf_folder = paste0(temp_dir,'/','11_HMRF/')
	if(!file.exists(hmrf_folder)) dir.create(hmrf_folder, recursive = T)

	# perform hmrf
	my_spatial_genes = km_spatialgenes[1:100]$genes
	HMRF_spatial_genes = doHMRF(gobject = mini_visium,
                            	expression_values = 'scaled',
                            	spatial_genes = my_spatial_genes,
                            	spatial_network_name = 'Delaunay_network',
                            	k = 8,
                            	betas = c(28,2,2),
                            	output_folder = paste0(hmrf_folder, '/', 'Spatial_genes_brain/SG_top100_k8_scaled'))

	# check and select hmrf
	for(i in seq(28, 30, by = 2)) {
  	viewHMRFresults2D(gobject = mini_visium,
                    	HMRFoutput = HMRF_spatial_genes,
                    	k = 8, betas_to_view = i,
                    	point_size = 2)
	}

	mini_visium = addHMRF(gobject = mini_visium,
                      	HMRFoutput = HMRF_spatial_genes,
                      	k = 8, betas_to_add = c(28),
                      	hmrf_name = 'HMRF')

	giotto_colors = getDistinctColors(8)
	names(giotto_colors) = 1:8
	spatPlot(gobject = mini_visium, cell_color = 'HMRF_k8_b.28',
         	point_size = 3, coord_fix_ratio = 1, cell_color_code = giotto_colors)



12. Export Giotto Analyzer to Viewer 
=======================================

.. code-block::

	viewer_folder = paste0(temp_dir, '/', 'Mouse_cortex_viewer')

	# select annotations, reductions and expression values to view in Giotto Viewer
	exportGiottoViewer(gobject = mini_visium, output_directory = viewer_folder,
                   	factor_annotations = c('cell_types',
                                          'leiden_clus',
                                          'HMRF_k8_b.28'),
                   	numeric_annotations = 'total_expr',
                  	dim_reductions = c('umap'),
                   	dim_reduction_names = c('umap'),
                   	expression_values = 'scaled',
                   	expression_rounding = 3,
                   	overwrite_dir = T)
