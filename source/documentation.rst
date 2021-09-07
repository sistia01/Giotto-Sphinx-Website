#########################
Function Documentation 
#########################

*************************
Giotto Object 
*************************

*Create and operate on Giotto Object*

.. toctree::
	:maxdepth: 2
	:hidden:

	createGiottoObject </subsections/documentation_functions/createGiottoObject.rst>
	createGiottoVisiumObject </subsections/documentation_functions/createGiottoVisiumObject.rst>
	filterGiotto </subsections/documentation_functions/filterGiotto.rst>
	subsetGiotto </subsections/documentation_functions/subsetGiotto.rst>
	subsetGiottoLocs </subsections/documentation_functions/subsetGiottoLocs.rst>

.. list-table::
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`createGiottoObject() <createGiottoObject>`
	  - Create a Giotto object 
	* - :ref:`createGiottoVisiumObject() <createGiottoVisiumObject>`
	  - Create a Visium Object
	* - :ref:`filterGiotto() <filterGiotto>`
	  - Filter Giotto 
	* - :ref:`subsetGiotto() <subsetGiotto>`
	  - Subset Giotto 
	* - :ref:`subsetGiottoLocs() <subsetGiottoLocs>`
	  - Subset Giotto Locs
 
	  
*************************
Giotto Environment  
*************************

*Work with Giotto Python Environment*

.. toctree::
	:maxdepth: 2
	:hidden:

	installGiottoEnvironment </subsections/documentation_functions/installGiottoEnvironmentFunction.rst>
	removeGiottoEnvironment </subsections/documentation_functions/removeGiottoEnvironment.rst>
	checkGiottoEnvironment </subsections/documentation_functions/checkGiottoEnvironment.rst>

.. list-table::
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`installGiottoEnvironment() <installGiottoEnvironmentFunction>`
	  - Install Giotto Environment 
	* - :ref:`removeGiottoEnvironment() <removeGiottoEnvironment>`
	  - Remove Giotto Environment 
	* - :ref:`checkGiottoEnvironment() <checkGiottoEnvironment>`
	  - Check Giotto Environment


***************************
Import Raw Data
***************************

*Functions to help to import raw spatial data.*

.. toctree::
	:maxdepth: 2
	:hidden:

	getSpatialDataset </subsections/documentation_functions/getSpatialDataset.rst>
	readExprMatrix </subsections/documentation_functions/readExprMatrix.rst>
	get10Xmatrix </subsections/documentation_functions/get10XMatrix.rst>
	get10Xmatrix_h5 </subsections/documentation_functions/get10XMatrix_h5.rst>
	stitchFieldCoordinates </subsections/documentation_functions/stitchFieldCoordinates.rst>
	stitchTileCoordinates </subsections/documentation_functions/stitchTileCoordinates.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description
	* - :ref:`getSpatialDataset() <getSpatialDataset>`
	  - Get The Spatial Data
	* - :ref:`readExprMatrix() <readExprMatrix>`
	  - Read The Expression Matrix
	* - :ref:`get10Xmatrix() <get10XMatrix>`
	  - Get An Expression Matrix From 10X Structure
	* - :ref:`get10Xmatrix_h5() <get10XMatrix_h5>`
	  - Get An Expression Matrix From 10X h5 Path 
	* - :ref:`stitchFieldCoordinates() <stitchFieldCoordinates>`
	  - Stitch Field Coordinates Together 
	* - :ref:`stitchTileCoordinates() <stitchTileCoordinates>`
	  - Stitch Tile Coordinates Together

***************************
Add Images
***************************

*Functions to work with images for a Giotto object.*

.. toctree::
	:maxdepth: 2
	:hidden:

	estimateImageBg </subsections/documentation_functions/estimateImageBg.rst>
	changeImageBg </subsections/documentation_functions/changeImageBg.rst>
	createGiottoImage </subsections/documentation_functions/createGiottoImage.rst>
	addGiottoImage </subsections/documentation_functions/addGiottoImage.rst>
	addGiottoImageToSpatPlot </subsections/documentation_functions/addGiottoImageToSpatPlot.rst>
	showGiottoImageNames </subsections/documentation_functions/showGiottoImageNames.rst>
	updateGiottoImage </subsections/documentation_functions/updateGiottoImage.rst>
	getGiottoImage </subsections/documentation_functions/getGiottoImage.rst>
	plotGiottoImage </subsections/documentation_functions/plotGiottoImage.rst>


.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function 
	  - Description
	* - :ref:`estimateImageBg() <estimateImageBg>`
	  - Estimate Background Color
	* - :ref:`changeImageBg() <changeImageBg>`
	  - Change Background Color
	* - :ref:`createGiottoImage() <createGiottoImage>`
	  - Create a Giotto Image
	* - :ref:`addGiottoImage() <addGiottoImage>`
	  - Add a Giotto Image to Giotto Object
	* - :ref:`addGiottoImageToSpatPlot() <addGiottoImageToSpatPlot>`
	  - Add Giotto Image to Spatial ggplot
	* - :ref:`showGiottoImageNames() <showGiottoImageNames>`
	  - Print Attached Giotto Image
	* - :ref:`updateGiottoImage() <updateGiottoImage>`
	  - Update Giotto Image Boundaries
	* - :ref:`getGiottoImage() <getGiottoImage>`
	  - Get Giotto Image From Giotto Object
	* - :ref:`plotGiottoImage() <plotGiottoImage>`
	  - Plot A Giotto Image From A Giotto Object


**************************
Giotto Instructions 
**************************

*Create or change Giotto instructions (e.g. defaults, plotting, saving, etc.)*

.. toctree::
	:maxdepth: 2
	:hidden:

	createGiottoInstructions </subsections/documentation_functions/createGiottoInstructions.rst>
	readGiottoInstructions </subsections/documentation_functions/readGiottoInstructions.rst>
	showGiottoInstructions </subsections/documentation_functions/showGiottoInstructions.rst>
	changeGiottoInstructions </subsections/documentation_functions/changeGiottoInstructions.rst>
	replaceGiottoInstructions </subsections/documentation_functions/replaceGiottoInstructions.rst>


.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function 
	  - Description 
	* - :ref:`createGiottoInstructions() <createGiottoInstructions>`
	  - Create Giotto Instructions
	* - :ref:`readGiottoInstructions() <readGiottoInstructions>`
	  - Read Giotto Instructions 
	* - :ref:`showGiottoInstructions() <showGiottoInstructions>`
 	  - Show Giotto Instructions 
	* - :ref:`changeGiottoInstructions() <changeGiottoInstructions>`
	  - Change Giotto Instructions 
	* - :ref:`replaceGiottoInstructions() <replaceGiottoInstructions>`
	  - Replace Giotto Instructions 

**************************	  
Giotto Helper Functions 
**************************
*Common functions to help working with Giotto objects*

.. toctree::
	:maxdepth: 2
	:hidden:

	pDataDT </subsections/documentation_functions/pDataDT.rst>
	fDataDT </subsections/documentation_functions/fDataDT.rst>
	showProcessingSteps </subsections/documentation_functions/showProcessingSteps.rst>
	calculateMetaTable </subsections/documentation_functions/calculateMetaTable.rst>
	calculateMetaTableCells </subsections/documentation_functions/calculateMetaTableCells.rst>
	combineMetadata </subsections/documentation_functions/combineMetadata.rst>
	createMetagenes </subsections/documentation_functions/createMetagenes.rst>
	findNetworkNeighbors </subsections/documentation_functions/findNetworkNeighbors.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function 
	  - Description 
	* - :ref:`pDataDT() <pDataDT>`
	  - Show Cell Metadata
	* - :ref:`fDataDT() <fDataDT>`
	  - Show Gene Metadata
	* - :ref:`showProcessingSteps() <showProcessingSteps>`
	  - Show Sequential Processing Steps
	* - :ref:`calculateMetaTable() <calculateMetaTable>`
	  - Calculate Average Gene Expression 
	* - :ref:`calculateMetaTableCells() <calculateMetaTableCells>`
	  - Calculate the Average Metadata Values 
	* - :ref:`combineMetadata() <combineMetadata>`
	  - Combine Cell Metadata
	* - :ref:`createMetagenes()<createMetagenes>`
	  - Create Average Metagene 
	* - :ref:`findNetworkNeighbors() <findNetworkNeighbors>`
	  - Find Spatial Neighbors 

*************************************	  
Giotto Processing Functions 
*************************************
*Functions that will (help to) add, update or change the Giotto object when processing spatial data.*

.. toctree::
	:maxdepth: 2
	:hidden:

	filterDistributions </subsections/documentation_functions/filterDistributions.rst>
	filterCombinations </subsections/documentation_functions/filterCombinations.rst>
	normalizeGiotto </subsections/documentation_functions/normalizeGiotto.rst>
	adjustGiottoMatrix </subsections/documentation_functions/adjustGiottoMatrix.rst>
	annotateGiotto </subsections/documentation_functions/annotateGiotto.rst>
	removeCellAnnotation </subsections/documentation_functions/removeCellAnnotation.rst>
	removeGeneAnnotation </subsections/documentation_functions/removeGeneAnnotation.rst>
	addCellMetadata </subsections/documentation_functions/addCellMetadata.rst>
	addGeneMetadata </subsections/documentation_functions/addGeneMetadata.rst>
	addGeneStatistics </subsections/documentation_functions/addGeneStatistics.rst>
	addCellStatistics </subsections/documentation_functions/addCellStatistics.rst>
	addStatistics </subsections/documentation_functions/addStatistics.rst>
	addGenesPerc </subsections/documentation_functions/addGenesPerc.rst>
	addCellIntMetadata </subsections/documentation_functions/addCellIntMetadata.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1
	
	* - Function 
	  - Description 
	* - :ref:`filterDistributions() <filterDistributions>`
	  - Show Gene Distributions
	* - :ref:`filterCombinations() <filterCombinations>`
	  - Show Gene/Cell Loss 
	* - :ref:`normalizeGiotto() <normalizeGiotto>`
	  - Normalize And/Or Scale Expression Values 
	* - :ref:`adjustGiottoMatrix() <adjustGiottoMatrix>`
	  - Adjust Expression Values 
	* - :ref:`annotateGiotto() <annotateGiotto>`
	  - Convert Cluster Results Into User Provided Annotation 
	* - :ref:`removeCellAnnotation() <removeCellAnnotation>`
	  - Remove Cell Annotation 
	* - :ref:`removeGeneAnnotation() <removeGeneAnnotation>`
	  - Remove Gene Annotation 
	* - :ref:`addCellMetadata() <addCellMetadata>`
	  - Add Cell Metadata
	* - :ref:`addGeneMetadata()<addGeneMetadata>`
	  - Add Gene Metadatat
	* - :ref:`addGeneStatistics() <addGeneStatistics>`
	  - Add Gene Statistics
	* - :ref:`addCellStatistics() <addCellStatistics>`
	  - Add Cell Statistics
	* - :ref:`addStatistics() <addStatistics>`
	  - Add Gene and Cell Statistics
	* - :ref:`addGenesPerc() <addGenesPerc>`
	  - Calculate Percent Counts
	* - :ref:`addCellIntMetadata() <addCellIntMetadata>`
	  - Add Cell Metadata Information Column 

******************************************
Dimension Reduction
******************************************
*Functions to reduce dimensions.*

.. toctree::
	:maxdepth: 2
	:hidden:

	calculateHVG </subsections/documentation_functions/calculateHVG.rst>
	signPCA </subsections/documentation_functions/signPCA.rst>
	screePlot </subsections/documentation_functions/screePlot.rst>
	jackstrawPlot </subsections/documentation_functions/jackstrawPlot.rst>
	runPCA </subsections/documentation_functions/runPCA.rst>
	runUMAP </subsections/documentation_functions/runUMAP.rst>
	runtSNE </subsections/documentation_functions/runtSNE.rst>


.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`calculateHVG() <calculateHVG>`
	  - Compute Highly Variable Genes
	* - :ref:`signPCA() <signPCA>`
	  - Identify PC's
	* - :ref:`screePlot() <screePlot>`
	  - Identify Significant PCs Via Screeplot
	* - :ref:`jackstrawPlot() <jackstrawPlot>`
	  - Identify Significant PCs Via JackstrawPlot
	* - :ref:`runPCA() <runPCA>`
	  - Run A PCA
	* - :ref:`runUMAP() <runUMAP>`
	  - Run A UMAP
	* - :ref:`runtSNE() <runtSNE>`
	  - Run a tSNE

*************************
Clustering
*************************
*Functions to cluster cells.*

.. toctree::
	:maxdepth: 2
	:hidden:

	createNearestNetwork </subsections/documentation_functions/createNearestNetwork.rst>
	addNetworkLayout </subsections/documentation_functions/addNetworkLayout.rst>
	extractNearestNetwork </subsections/documentation_functions/extractNearestNetwork.rst>
	clusterCells </subsections/documentation_functions/clusterCells.rst>
	doLeidenCluster </subsections/documentation_functions/doLeidenCluster.rst>
	doLouvainCluster </subsections/documentation_functions/doLouvainCluster.rst>
	doKmeans </subsections/documentation_functions/doKmeans.rst>
	doHclust </subsections/documentation_functions/doHclust.rst>
	subClusterCells </subsections/documentation_functions/subClusterCells.rst>
	doLeidenSubCluster </subsections/documentation_functions/doLeidenSubCluster.rst>
	doLouvainSubCluster </subsections/documentation_functions/doLouvainSubCluster.rst>
	getClusterSimilarity </subsections/documentation_functions/getClusterSimilarity.rst>
	mergeClusters </subsections/documentation_functions/mergeClusters.rst>
	getDendrogramSplits </subsections/documentation_functions/getDendrogramSplits.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 	
	* - :ref:`createNearestNetwork() <createNearestNetwork>`
	  - Create NN Network 
	* - :ref:`addNetworkLayout() <addNetworkLayout>`
	  - Add Network Layout
	* - :ref:`extractNearestNetwork() <extractNearestNetwork>`
	  - Calculate Gene Signature Enrichment Score
	* - :ref:`clusterCells() <clusterCells>`
	  - Cluster Cells 
	* - :ref:`doLeidenCluster() <doLeidenCluster>`
	  - Cluster Cells Using NN-Network
	* - :ref:`doLouvainCluster() <doLouvainCluster>`
	  - Cluster Cells Using NN-Network and Louvain Algorithm
	* - :ref:`doKmeans() <doKmeans>`
	  - Cluster Cells Using K-Means
	* - :ref:`doHclust() <doHclust>`
	  - Cluster Cells Using Hierarchical Clustering
	* - :ref:`subClusterCells() <subClusterCells>`
	  - Sub-Cluster Cells
	* - :ref:`doLeidenSubCluster() <doLeidenSubCluster>`
	  - Further Sub-Clustering of Cells Using NN-Network and Leiden Algorithm
	* - :ref:`doLouvainSubCluster() <doLouvainSubCluster>`
	  - Further Sub-Clustering of Cells Using NN-Network and Louvain Algorithm
	* - :ref:`getClusterSimilarity() <getClusterSimilarity>`
	  - Determine Pairwise Correlation Score
	* - :ref:`mergeClusters() <mergeClusters>`
	  - Merge Clusters
	* - :ref:`getDendrogramSplits() <getDendrogramSplits>`
	  - Split Dendrogram 

*************************
Marker Genes 
*************************
*Functions to detect cell type / cluster specific marker genes.*

.. toctree::
	:maxdepth: 2
	:hidden:

	findMarkers </subsections/documentation_functions/findMarkers.rst>
	findMarkers_one_vs_all </subsections/documentation_functions/findMarkers_one_vs_all.rst>
	findGiniMarkers </subsections/documentation_functions/findGiniMarkers.rst>
	findGiniMarkers_one_vs_all </subsections/documentation_functions/findGiniMarkers_one_vs_all.rst>
	findScranMarkers </subsections/documentation_functions/findScranMarkers.rst>
	findScranMarkers_one_vs_all </subsections/documentation_functions/findScranMarkers_one_vs_all.rst>
	findMastMarkers </subsections/documentation_functions/findMastMarkers.rst>
	findMastMarkers_one_vs_all </subsections/documentation_functions/findMastMarkers_one_vs_all.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1


	* - Function
	  - Description 
	* - :ref:`findMarkers() <findMarkersFunction>`
	  - Find Marker Genes
	* - :ref:`findMarkers_one_vs_all() <findMarkers_one_vs_all>`
	  - Find Marker Genes At Once
	* - :ref:`findGiniMarkers() <findGiniMarkers>`
	  - Find Gini Markers
	* - :ref:`findGiniMarkers_one_vs_all() <findGiniMarkers_one_vs_all>`
	  - Find Marker Genes Using Gini in One vs. All Manner
	* - :ref:`findScranMarkers() <findScranMarkers>`
	  - Identify Marker Genes Based on Scran
	* - :ref:`findScranMarkers_one_vs_all() <findScranMarkers_one_vs_all>`
	  - Identify Marker Genes in a One vs. All Manner
	* - :ref:`findMastMarkers() <findMastMarkers>`
	  - Identify Marker Genes Using MAST
	* - :ref:`findMastMarkers_one_vs_all() <findMastMarkers_one_vs_all>`
	  - Identify Marker Genes Using MAST in One vs. All Manner


*************************
Auxiliary Visualizations
*************************
*Functions for different visualization options to explore gene, cell or cluster characteristics.*

.. toctree::
	:maxdepth: 2
	:hidden:

	showClusterHeatmap </subsections/documentation_functions/showClusterHeatmap.rst>
	showClusterDendrogram </subsections/documentation_functions/showClusterDendrogram.rst>
	plotHeatmap </subsections/documentation_functions/plotHeatmap.rst>
	plotMetaDataHeatmap </subsections/documentation_functions/plotMetaDataHeatmap.rst>
	plotMetaDataCellsHeatmap </subsections/documentation_functions/plotMetaDataCellsHeatmap.rst>
	violinPlot </subsections/documentation_functions/violinPlot.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`showClusterHeatmap() <showClusterHeatmap>`
	  - Create Cluster Heatmap
	* - :ref:`showClusterDendrogram() <showClusterDendrogram>`
	  - Create Cluster Dendrogram 
	* - :ref:`plotHeatmap() <plotHeatmap>`
	  - Plot Heatmap
	* - :ref:`plotMetaDataHeatmap() <plotMetaDataHeatmap>`
	  - Plot Heatmap for Metadata
	* - :ref:`plotMetaDataCellsHeatmap() <plotMetaDataCellsHeatmap>`
	  - Plot Heatmap for Cell Metdata
	* - :ref:`violinPlot() <violinPlot>`
	  - Create Violin Plot 

***************************************
Spatial Enrichment & Deconvolution
***************************************
*Functions for algorithms to compute spatial enrichment of gene signatures or single-cell RNA-seq annotation.*

.. toctree::
	:maxdepth: 2
	:hidden:

	makeSignMatrixPAGE </subsections/documentation_functions/makeSignMatrixPAGE.rst>
	makeSignMatrixRank </subsections/documentation_functions/makeSignMatrixRank.rst>
	runSpatialEnrich </subsections/documentation_functions/runSpatialEnrich.rst>
	createSpatialEnrich </subsections/documentation_functions/createSpatialEnrich.rst>
	runPAGEEnrich </subsections/documentation_functions/runPAGEEnrich.rst>
	PAGEEnrich </subsections/documentation_functions/PAGEEnrich.rst>
	runRankEnrich </subsections/documentation_functions/runRankEnrich.rst>
	rankEnrich </subsections/documentation_functions/rankEnrich.rst>
	runHyperGeometricEnrich </subsections/documentation_functions/runHyperGeometricEnrich.rst>
	hyperGeometricEnrich </subsections/documentation_functions/hyperGeometricEnrich.rst>
	runSpatialDeconv </subsections/documentation_functions/runSpatialDeconv.rst>
	runDWLSDeconv </subsections/documentation_functions/runDWLSDeconv.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`makeSignMatrixPAGE() <makeSignMatrixPAGE>`
	  - Convert Gene Signature List To Binary Matrix 
	* - :ref:`makeSignMatrixRank() <makeSignMatrixRank>`
	  - Convert Single-Cell Matrix to Cluster
	* - :ref:`runSpatialEnrich() <runSpatialEnrich>`
	  - Calculate Gene Signature Enrichment Score With RANK
	* - :ref:`createSpatialEnrich() <createSpatialEnrich>`
	  - Calculate Gene Signature Enrichment Scores 
	* - :ref:`runPAGEEnrich() <runPAGEEnrich>`
	  - Calculate Position Gene Signature Enrichment With PAGE
	* - :ref:`PAGEEnrich() <PAGEEnrich>`
	  - Calculate Gene Signature  Enrichment With PAGE
	* - :ref:`runRankEnrich() <runRankEnrich>`
	  - Calculate Gene Signature Enrichment Using RANK
	* - :ref:`rankEnrich() <rankEnrich>`
	  - Calculate Gene Signature Enrichment Score With RANK
	* - :ref:`runHyperGeometricEnrich() <runHyperGeometricEnrich>`
	  - Calculate Gene Signature Enrichment Score With Hypergeometric Test
	* - :ref:`hyperGeometricEnrich() <hyperGeometricEnrich>`
	  - Calculate Gene Signature Enrichment Score With Hypergeometric Test
	* - :ref:`runSpatialDeconv() <runSpatialDeconv>`
	  - Perform Deconvolution 
	* - :ref:`runDWLSDeconv() <runDWLSDeconv>`
	  - Perform DWLS Deconvolution 

***************************************
Spatial Network Or Grid
***************************************
*Function to (help) create a spatial network or grid.*


.. toctree::
	:maxdepth: 2
	:hidden:

	spatNetwDistributionsDistance </subsections/documentation_functions/spatNetwDistributionsDistance.rst>
	spatNetwDistributionsKneighbors </subsections/documentation_functions/spatNetwDistributionsKneighbors.rst>
	spatNetwDistributions </subsections/documentation_functions/spatNetwDistributions.rst>
	createSpatialDelaunayNetwork </subsections/documentation_functions/createSpatialDelaunayNetwork.rst>
	plotStatDelaunayNetwork </subsections/documentation_functions/plotStatDelaunayNetwork.rst>
	createSpatialKNNnetwork </subsections/documentation_functions/createSpatialKNNnetwork.rst>
	createSpatialNetwork </subsections/documentation_functions/createSpatialNetwork.rst>
	annotateSpatialNetwork </subsections/documentation_functions/annotateSpatialNetwork.rst>
	annotateSpatialGrid </subsections/documentation_functions/annotateSpatialGrid.rst>
	createSpatialGrid </subsections/documentation_functions/createSpatialGrid.rst>
	showNetworks </subsections/documentation_functions/showNetworks.rst>
	showGrids </subsections/documentation_functions/showGrids.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1
	
	* - Function
	  - Description 
	* - :ref:`spatNetwDistributionsDistance() <spatNetwDistributionsDistance>`
	  - Distance Distribution for Spatial k-Neighbor
	* - :ref:`spatNetwDistributionsKneighbors() <spatNetwDistributionsKneighbors>`
	  - Distance Distribution for Spatial k-Neighbor
	* - :ref:`spatNetwDistributions() <spatNetwDistributions>`
	  - Histogram of Distance Distribution for Spatial k-Neighbors
	* - :ref:`createSpatialDelaunayNetwork() <createSpatialDelaunayNetwork>`
	  - Create Spatial Delaunay 
	* - :ref:`plotStatDelaunayNetwork() <plotStatDelaunayNetwork>`
	  - Plot Network Statistics for Delaunay Network 
	* - :ref:`createSpatialKNNnetwork() <createSpatialKNNnetwork>`
	  - Create Spatial KNN Network 
	* - :ref:`createSpatialNetwork() <createSpatialNetwork>`
	  - Create Spatial Network 
	* - :ref:`annotateSpatialNetwork() <annotateSpatialNetwork>`
	  - Annotate Spatial Network 
	* - :ref:`annotateSpatialGrid() <annotateSpatialGrid>`
	  - Annotate Spatial Grid 
	* - :ref:`createSpatialGrid() <createSpatialGrid>`
	  - Create Spatial Grid 
	* - :ref:`showNetworks() <showNetworks>`
	  - Print Available Spatial Networks 
	* - :ref:`showGrids() <showGrids>`
	  - Print Available Spatial Grids

***************************************
Spatial Genes
***************************************
*Functions to identify spatial genes.*

.. toctree::
	:maxdepth: 2
	:hidden:

	binSpect </subsections/documentation_functions/binSpect.rst>
	binSpectSingle </subsections/documentation_functions/binSpectSingle.rst>
	binSpectMulti </subsections/documentation_functions/binSpectMulti.rst>
	silhouetteRank </subsections/documentation_functions/silhouetteRank.rst>
	spatialDE </subsections/documentation_functions/spatialDE.rst>
	spatialAEH </subsections/documentation_functions/spatialAEH.rst>
	trendSceek </subsections/documentation_functions/trendSceek.rst>
	spark </subsections/documentation_functions/spark.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`binSpect() <binSpect>`
	  - Create BinSpect
	* - :ref:`binSpectSingle() <binSpectSingle>`
	  - Create binSpect For Single Network 
	* - :ref:`binSpectMulti() <binSpectMulti>`
	  - binSpect for Multiple KNN Networks 
	* - :ref:`silhouetteRank() <silhouetteRank>`
	  - Create binSpect For Single Network 
	* - :ref:`spatialDE() <spatialDE>`
	  - Compute Spatial Variables With SpatialDE Method 
	* - :ref:`spatialAEH() <spatialAEH>`
	  - Compute Spatial Variables With SpatialAEH Method 
	* - :ref:`trendSceek() <trendSceek>`
	  - Compute Spatially Variable Genes With Trendsceek
	* - :ref:`spark() <spark>`
	  - Compute Spatially Variable Genes With SPARK

***************************************
Spatial Gene Simulation
***************************************
*Functions to simulate a gene expression pattern.*

.. toctree::
	:maxdepth: 2
	:hidden:

	simulateOneGenePatternGiottoObject </subsections/documentation_functions/simulateOneGenePatternGiottoObject.rst>
	runPatternSimulation </subsections/documentation_functions/runPatternSimulation.rst>


.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`simulateOneGenePatternGiottoObject() <simulateOneGenePatternGiottoObject>`
	  - Create Simulated Spatial Pattern
	* - :ref:`runPatternSimulation() <runPatternSimulation>`
	  - Create Known Spatial Pattern for Selected Genes

***************************************
Spatial Co-Expression Patterns/Modules
***************************************
*Functions to identify spatial co-expression patterns.*

.. toctree::
	:maxdepth: 2
	:hidden:

	clusterSpatialCorGenes </subsections/documentation_functions/clusterSpatialCorGenes.rst>
	detectSpatialCorGenes </subsections/documentation_functions/detectSpatialCorGenes.rst>
	heatmSpatialCorGenes </subsections/documentation_functions/heatmSpatialCorGenes.rst>
	showSpatialCorGenes </subsections/documentation_functions/showSpatialCorGenes.rst>
	rankSpatialCorGroups </subsections/documentation_functions/rankSpatialCorGroups.rst>


.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`clusterSpatialCorGenes() <clusterSpatialCorGenes>`
	  - Cluster Genes Using Spatial Information 
	* - :ref:`detectSpatialCorGenes() <detectSpatialCorGenes>`
	  - Detect Genes Using Spatial Correlation 
	* - :ref:`heatmSpatialCorGenes() <heatmSpatialCorGenes>`
	  - Create Heatmap of Spatial Correlation
	* - :ref:`showSpatialCorGenes() <showSpatialCorGenes>`
	  - Show Spatially Correlated Genes 
	* - :ref:`rankSpatialCorGroups() <rankSpatialCorGroups>`
	  - Rank Spatially Correlated Gene Clusters 

***************************************
Hidden Markov Random Field (HMRF) 
***************************************
*Functions to identify spatial domains with HMRF.*

.. toctree::
	:maxdepth: 2
	:hidden:

	doHMRF </subsections/documentation_functions/doHMRF.rst>
	loadHMRF </subsections/documentation_functions/loadHMRF.rst>
	viewHMRFresults </subsections/documentation_functions/viewHMRFresults.rst>
	writeHMRFresults </subsections/documentation_functions/writeHMRFresults.rst>
	addHMRF </subsections/documentation_functions/addHMRF.rst>
	viewHMRFresults2D </subsections/documentation_functions/viewHMRFresults2D.rst>
	viewHMRFresults3D </subsections/documentation_functions/viewHMRFresults3D.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`doHMRF() <doHMRF>`
	  - Rank Spatially Correlated Gene Clusters 
	* - :ref:`loadHMRF() <loadHMRF>`
	  - Load HMRF
	* - :ref:`viewHMRFresults() <viewHMRFresults>`
	  - View HMRF Results
	* - :ref:`writeHMRFresults() <writeHMRFresults>`
	  - Write `doHMRF() <doHMRF>`__ Results
	* - :ref:`addHMRF() <addHMRF>`
	  - Add `doHMRF() <doHMRF>`__ Results
	* - :ref:`viewHMRFresults2D() <viewHMRFresults2D>`
	  - View HMRF Results
	* - :ref:`viewHMRFresults3D() <viewHMRFresults3D>`
	  - View HMRF Results

***************************************
2D Visualization In Expression Space
***************************************
*Visualization of expression space (e.g. UMAP) in 2D.*

.. toctree::
	:maxdepth: 2
	:hidden:

	dimPlot </subsections/documentation_functions/dimPlot.rst>
	plotUMAP </subsections/documentation_functions/plotUMAP.rst>
	plotTSNE </subsections/documentation_functions/plotTSNE.rst>
	plotPCA </subsections/documentation_functions/plotPCA.rst>
	dimGenePlot </subsections/documentation_functions/dimGenePlot.rst>
	dimCellPlot </subsections/documentation_functions/dimCellPlot.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`dimPlot() <dimPlot>`
	  - Visualize Cells By Coordinates
	* - :ref:`plotUMAP() <plotUMAP>`
	  - UMAP Wrapper
	* - :ref:`plotTSNE() <plotTSNE>`
	  - tSNE Wrapper
	* - :ref:`plotPCA() <plotPCA>`
	  - PCA Wrapper
	* - :ref:`dimGenePlot() <dimGenePlot>`
	  - Visualize Gene Expression By Dimension Coordinates
	* - :ref:`dimCellPlot() <dimCellPlot>`
	  - Visualize Cells Expression By Dimension Coordinates

***************************************
2D Visualization In Spatial Space
***************************************
*Visualization of expression space (e.g. UMAP) in 2D.*

.. toctree::
	:maxdepth: 2
	:hidden:

	spatPlot </subsections/documentation_functions/spatPlot.rst>
	spatPlot2D </subsections/documentation_functions/spatPlot2D.rst>
	spatGenePlot </subsections/documentation_functions/spatGenePlot.rst>
	spatGenePlot3D </subsections/documentation_functions/spatGenePlot3D.rst>
	spatCellPlot </subsections/documentation_functions/spatCellPlot.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`spatPlot() <spatPlot>`
	  - Visualize Cells By Spatial Coordinates
	* - :ref:`spatGenePlot() <spatGenePlot>`
	  - Visualize Cells and Genes By Spatial Coordinates
	* - :ref:`spatCellPlot() <spatCellPlot>`
	  - Visualize Cells By Spatial Coordinates

****************************************************
2D Visualization In Spatial And Expression Space
****************************************************
*Visualization in both 2D spatial and expression space.*

.. toctree::
	:maxdepth: 2
	:hidden:

	spatDimPlot </subsections/documentation_functions/spatDimPlot.rst>
	spatDimPlot3D </subsections/documentation_functions/spatDimPlot3D.rst>
	spatDimGenePlot </subsections/documentation_functions/spatDimGenePlot.rst>
	spatDimCellPlot </subsections/documentation_functions/spatDimCellPlot.rst>
	spatDimCellPlot2D </subsections/documentation_functions/spatDimCellPlot2D.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`spatDimPlot() <spatDimPlot>`
	  - Visualize Cells By Spatial and Dimensional Coordinates
	* - :ref:`spatDimGenePlot() <spatDimGenePlot>`
	  - Visualize Genes By Spatial and Dimension Coordinates Via ggplot
	* - :ref:`spatDimCellPlot() <spatDimCellPlot>`
	  - Visualize Cells By Spatial And Dimension Coordinates in 2D

****************************************************
3D Dimension Reduction Visualization
****************************************************
*Visualization in both 2D spatial and expression space.*

.. toctree::
	:maxdepth: 2
	:hidden:

	dimPlot2D </subsections/documentation_functions/dimPlot2D.rst>
	dimPlot3D </subsections/documentation_functions/dimPlot3D.rst>
	plotUMAP_3D </subsections/documentation_functions/plotUMAP_3D.rst>
	plotTSNE_3D </subsections/documentation_functions/plotTSNE_3D.rst>
	plotPCA_3D </subsections/documentation_functions/plotPCA_3D.rst>
	dimGenePlot3D </subsections/documentation_functions/dimGenePlot3D.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description
  	* - :ref:`dimPlot2D() <dimPlot2D>`
	  - Visualize Cells By Spatial Coordinates in 2D 
	* - :ref:`dimPlot3D() <dimPlot3D>`
	  - Visualize Cells By Spatial Coordinates in 3D
	* - :ref:`plotUMAP_3D() <plotUMAP_3D>`
	  - Visualize Cells By Spatial Coordinates in 3D
	* - :ref:`plotTSNE_3D() <plotTSNE_3D>`
	  - Visualize Cells By Dimension Reduction Coordinates in 3D
	* - :ref:`plotPCA_3D() <plotPCA_3D>`
	  - Visualize Cells By 3D PCA Dimension Reduction 
	* - :ref:`dimGenePlot3D() <dimGenePlot3D>`
	  - Visualize Cells And Gene Expression By Dimension Reduction 

****************************************************
3D Visualization In Spatial Space
****************************************************
*Visualization in both 2D spatial and expression space.*

.. toctree::
	:maxdepth: 2
	:hidden:

	spatPlot3D </subsections/documentation_functions/spatPlot3D.rst>
	spatDimGenePlot3D </subsections/documentation_functions/spatDimGenePlot3D.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`spatPlot3D() <spatPlot3D>`
	  - Visualize Cells By Spatial and Dimensional Coordinates in 3D
	* - :ref:`spatDimGenePlot3D() <spatDimGenePlot3D>`
	  - Visualize Cells By Spatial and Dimensional Coordinates Using Plotly

****************************************************
In Silico Cross Sections
****************************************************
*Functions to create an in silico 2D cross sections from 3D data.*

.. toctree::
	:maxdepth: 2
	:hidden:

	createCrossSection </subsections/documentation_functions/createCrossSection.rst>
	crossSectionGenePlot </subsections/documentation_functions/crossSectionGenePlot.rst>
	crossSectionPlot </subsections/documentation_functions/crossSectionPlot.rst>
	crossSectionGenePlot3D </subsections/documentation_functions/crossSectionGenePlot3D.rst>
	crossSectionPlot3D </subsections/documentation_functions/crossSectionPlot3D.rst>
	insertCrossSectionSpatPlot3D </subsections/documentation_functions/insertCrossSectionSpatPlot3D.rst>
	insertCrossSectionGenePlot3D </subsections/documentation_functions/insertCrossSectionGenePlot3D.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`createCrossSection() <createCrossSection>`
	  - Create a Virtual Cross Section 
	* - :ref:`crossSectionGenePlot() <crossSectionGenePlot>`
	  - Visualize Cells And Gene Expression Virtually
	* - :ref:`crossSectionPlot() <crossSectionPlot>`
	  - Visualize Cells In Virtual Cross Section
	* - :ref:`crossSectionGenePlot3D() <crossSectionGenePlot3D>`
	  - Visualize Cells And Gene Expression Virtually (3D)
	* - :ref:`crossSectionPlot3D() <crossSectionPlot3D>`
	  - Visualize Cells In A Virtual Cross Section (3D)
	* - :ref:`insertCrossSectionSpatPlot3D() <insertCrossSectionSpatPlot3D>`
	  - Visualize Mesh-Grid Lines With Cells
	* - :ref:`insertCrossSectionGenePlot3D() <insertCrossSectionGenePlot3D>`
	  - Visualize Cells And Gene Expression In A Virtual Cross Section 

**************************************************************
Cell Neighborhood: Cell-Type/Cell-Type Enrichment
**************************************************************
*Functions to calculate and visualize cell-type/cell-type spatial enrichment or depletion.*

.. toctree::
	:maxdepth: 2
	:hidden:

	cellProximityEnrichment </subsections/documentation_functions/cellProximityEnrichment.rst>
	cellProximityBarplot </subsections/documentation_functions/cellProximityBarplot.rst>
	cellProximityHeatmap </subsections/documentation_functions/cellProximityHeatmap.rst>
	cellProximityNetwork </subsections/documentation_functions/cellProximityNetwork.rst>
	cellProximitySpatPlot </subsections/documentation_functions/cellProximitySpatPlot.rst>
	cellProximitySpatPlot3D </subsections/documentation_functions/cellProximitySpatPlot3D.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`cellProximityEnrichment() <cellProximityEnrichment>`
	  - Calculate Cell-Cell Interaction Enrichment
	* - :ref:`cellProximityBarplot() <cellProximityBarplot>`
	  - Create Barplot from Cell-Cell Proximity Score
	* - :ref:`cellProximityHeatmap() <cellProximityHeatmap>`
	  - Create Heatmap from Cell-Cell Proximity Score
	* - :ref:`cellProximityNetwork() <cellProximityNetwork>`
	  - Create Network from Cell-Cell Proximity Score
	* - :ref:`cellProximitySpatPlot() <cellProximitySpatPlot>`
	  - Visualize Cell-Cell Interactions (2D)
	* - :ref:`cellProximitySpatPlot3D() <cellProximitySpatPlot3D>`
	  - Visualize Cell-Cell Interactions (3D)

**************************************************************
Cell Neighborhood: Spatial Interaction Changed Genes (ICG)
**************************************************************
*Identify and visualize genes that change in a source cell type due to interaction with another neighboring cell type.*

.. toctree::
	:maxdepth: 2
	:hidden:

	findInteractionChangedGenes </subsections/documentation_functions/findInteractionChangedGenes.rst>
	findICG </subsections/documentation_functions/findICG.rst>
	findCellProximityGenes </subsections/documentation_functions/findCellProximityGenes.rst>
	findCPG </subsections/documentation_functions/findCPG.rst>
	filterCellProximityGenes </subsections/documentation_functions/filterCellProximityGenes.rst>
	filterInteractionChangedGenes </subsections/documentation_functions/filterInteractionChangedGenes.rst>
	filterICG </subsections/documentation_functions/filterICG.rst>
	filterCPG </subsections/documentation_functions/filterCPG.rst>
	combineInteractionChangedGenes </subsections/documentation_functions/combineInteractionChangedGenes.rst>
	combineICG </subsections/documentation_functions/combineICG.rst>
	combineCellProximityGenes </subsections/documentation_functions/combineCellProximityGenes.rst>
	combineCPG </subsections/documentation_functions/combineCPG.rst>
	plotInteractionChangedGenes </subsections/documentation_functions/plotInteractionChangedGenes.rst>
	plotICG </subsections/documentation_functions/plotICG.rst>
	plotCellProximityGenes </subsections/documentation_functions/plotCellProximityGenes.rst>
	plotCPG </subsections/documentation_functions/plotCPG.rst>
	plotCombineInteractionChangedGenes </subsections/documentation_functions/plotCombineInteractionChangedGenes.rst>
	plotCombineICG </subsections/documentation_functions/plotCombineICG.rst>
	plotCombineCellProximityGenes </subsections/documentation_functions/plotCombineCellProximityGenes.rst>
	plotCombineCPG </subsections/documentation_functions/plotCombineCPG.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`findInteractionChangedGenes() <findInteractionChangedGenes>`
	  - Identify Cell-Cell Interaction Changed Genes (ICGs)
	* - :ref:`findICG() <findICG>`
	  - Identify Cell-Cell Interaction Changed Genes (ICGs)
	* - :ref:`findCellProximityGenes() <findCellProximityGenes>`
	  - Identify Cell-Cell Interaction Changed Genes (ICGs)
	* - :ref:`findCPG() <findCPG>`
	  - Identify Cell-Cell Interaction Changed Genes (ICGs)
	* - :ref:`filterCellProximityGenes() <filterCellProximityGenes>`
	  - Identify Cell-Cell Interaction Changed Genes (ICGs)
	* - :ref:`filterInteractionChangedGenes() <filterInteractionChangedGenes>`
	  - Filter The Identified Cell-Cell Interaction Changed Genes (ICGs)
	* - :ref:`filterICG() <filterICG>`
	  - Filter ICGs
	* - :ref:`filterCPG() <filterCPG>`
	  - Filter ICGs
	* - :ref:`combineInteractionChangedGenes() <combineInteractionChangedGenes>`
	  - Combine ICG Scores (Pairwise)
	* - :ref:`combineICG() <combineICG>`
	  - Combine ICG Scores (Pairwise)
	* - :ref:`combineCellProximityGenes() <combineCellProximityGenes>`
	  - Combine ICG Scores (Pairwise)
	* - :ref:`combineCPG() <combineCPG>`
	  - Combine ICG Scores (Pairwise)
	* - :ref:`plotInteractionChangedGenes() <plotInteractionChangedGenes>`
	  - Visualize ICGs via Barplot
	* - :ref:`plotICG() <plotICG>`
	  - Visualize ICGs via Barplot
	* - :ref:`plotCellProximityGenes() <plotCellProximityGenes>`
	  - Visualize Cell Proximity Gene Scores
	* - :ref:`plotCPG() <plotCPG>`
	  - Visualize Cell Proximity Gene Scores
	* - :ref:`plotCombineInteractionChangedGenes() <plotCombineInteractionChangedGenes>`
	  - Visualize Combined ICG Scores 
	* - :ref:`plotCombineICG() <plotCombineICG>`
	  - Visualize Combined ICG Scores 
	* - :ref:`plotCombineCellProximityGenes() <plotCombineCellProximityGenes>`
	  - Visualize Combined ICG Scores 
	* - :ref:`plotCombineCPG() <plotCombineCPG>`
	  - Visualize Combined ICG Scores 

******************************************************
Cell Neighborhood: Ligand-Receptor Cell Communication
******************************************************
*Functions to calculate and visualize cell-type/cell-type spatial enrichment or depletion.*

.. toctree::
	:maxdepth: 2
	:hidden:

	exprCellCellcom </subsections/documentation_functions/exprCellCellcom.rst>
	spatCellCellcom </subsections/documentation_functions/spatCellCellcom.rst>
	plotCCcomDotplot </subsections/documentation_functions/plotCCcomDotplot.rst>
	plotRankSpatvsExpr </subsections/documentation_functions/plotRankSpatvsExpr.rst>
	plotRecovery </subsections/documentation_functions/plotRecovery.rst>


.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`exprCellCellcom() <exprCellCellcom>`
	  - Calculate Cell-Cell Communication Scores
	* - :ref:`spatCellCellcom() <spatCellCellcom>`
	  - Calculate Spatial Cell-Cell Communication Scores
	* - :ref:`plotCCcomDotplot() <plotCCcomDotplot>`
	  - Plot Ligand-Receptor Communication Scores 
	* - :ref:`plotRankSpatvsExpr() <plotRankSpatvsExpr>`
	  - Plot Comparison of Ligand-Receptor Rankings
	* - :ref:`plotRecovery() <plotRecovery>`
	  - Plot Comparison of Ligand-Receptor Rankings 

****************************************************
Export From Giotto Analyzer To Viewer
****************************************************
*Export selected annotations to a folder that can be used as input for Giotto Viewer.*

.. toctree::
	:maxdepth: 2
	:hidden:

	exportGiottoViewer </subsections/documentation_functions/exportGiottoViewer.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`exportGiottoViewer() <exportGiottoViewer>`
	  - Compute Highly Variable Genes 

****************************************************
Interoperability
****************************************************
*Convert other type of objects into a Giotto object.*

.. toctree::
	:maxdepth: 2
	:hidden:

	anndataToGiotto </subsections/documentation_functions/anndataToGiotto.rst>

.. list-table:: 
	:widths: 100 100 
	:header-rows: 1

	* - Function
	  - Description 
	* - :ref:`anndataToGiotto() <anndataToGiotto>`
	  - Compute Highly Variable Genes 

 