#######################
What is Giotto?
#######################

Giotto is a comprehensive and open-source toolbox for spatial data analysis and visualization. 
The analysis module provides end-to-end analysis by implementing a wide range of algorithms for 
characterizing tissue composition, spatial expression patterns, and cellular interactions. 
Furthermore, single-cell RNAseq data can be integrated for spatial cell-type enrichment analysis.
The visualization module allows users to interactively visualize analysis outputs and imaging features. 
Giotto is applicable to a wide range of spatial technologies and platforms.

.. image:: images/overview_datasets.png
    :width: 400
    :alt: Image showing the overview of Spatial Giotto
    :align: center

*************
Description 
*************

* Giotto provides a flexible framework for common single-cell processing steps such as:
   
  * Quality control
  * Normalization
  * Dimension reduction
  * Clustering and cell type annotation
  
* To facilitate the analysis of recently emerging high-throughput, but lower-resolution spatial transcriptomic technologies, such as 10X Genomics Visium and Slide-seq, Giotto has 3 implemented algorithms for estimating the spatial enrichment of different cell types by integration of known gene signatures or single-cell RNAseq expression and annotation data.
* Spatial information is retained through the formation of a spatial grid and/or a spatial proximity network, which is used to:
  
  * Identify spatial genes
  * Extract continuous spatial-expression patterns
  * Identify discrete spatial domains using HMRF
  * Explore cell-type/cell-type spatial interaction enrichment or depletion
  * Calculate spatially increased ligand-receptor expression in cells of interacting cell type pairs
  * Find interaction changed genes (ICG): genes that change expression in one cell type due to interaction with a neighboring cell type

* Giotto provides a number of options to visualize both 2D and 3D data and the outcome of Giotto can be interactively explored using :bdg-link-success:`Giotto Viewer <http://spatial.rc.fas.harvard.edu/giotto-viewer/>` which allows you to overlay the obtained results with raw or additional images of the profiled tissue section(s).

.. _Giotto Viewer: http://spatial.rc.fas.harvard.edu/spatialgiotto/giotto.install.native.html


**********************
Cite Giotto
**********************

`Dries, R., Zhu, Q., Dong, R., Eng, C. H. L., Li, H., Liu, K., ... & Yuan, G. C. (2021). Giotto: a toolbox for integrative analysis and visualization of spatial expression data. Genome biology, 22(1), 1-31. <https://pubmed.ncbi.nlm.nih.gov/33685491/>`


*******************************
License
*******************************

.. github-shield:: 
    :username: RubD
    :repository: Giotto
    :license: 

****************************
Authors and Developers 
****************************

+---------------+---------------------+
|`Ruben Dries`_ |*Author, Maintainer* | 
+---------------+---------------------+
| Qian Zhu      |*Author*             |
+---------------+---------------------+
| Huipeng Li    |*Author*             |
+---------------+---------------------+
| Rui Dong      |*Author*             |
+---------------+---------------------+
| Guo-Cheng Yuan|*Author*             |
+---------------+---------------------+

.. _Ruben Dries: https://www.drieslab.com

***********
References
***********
#. `Han X, Wang R, Zhou Y, Fei L, Sun H, Lai S, et al. Mapping the mouse cell atlas by microwell-Seq. Cell. 2018;173:1307. doi: 10.1016/j.cell.2018.05.012. <https://pubmed.ncbi.nlm.nih.gov/29775597/>`_
#. `Tabula Muris Consortium, overall coordination, logistical coordination, organ collection and processing, library preparation and sequencing, Computational data analysis, et al. Single-cell transcriptomics of 20 mouse organs creates a Tabula Muris. Nature. 2018;562:367–72.`_
#. `Lubeck E, Coskun AF, Zhiyentayev T, Ahmad M, Cai L. Single-cell in situ RNA profiling by sequential hybridization. Nat. Methods. 2014. p. 360–361.`_
#. `Chen KH, Boettiger AN, Moffitt JR, Wang S, Zhuang X. RNA imaging. Spatially resolved, highly multiplexed RNA profiling in single cells. Science. 2015;348:aaa6090. doi: 10.1126/science.aaa6090. <https://pubmed.ncbi.nlm.nih.gov/25858977/>`_
#. `Ståhl PL, Salmén F, Vickovic S, Lundmark A, Navarro JF, Magnusson J, et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science. 2016;353:78–82. doi: 10.1126/science.aaf2403.  <https://pubmed.ncbi.nlm.nih.gov/27365449/>`_


.. _Tabula Muris Consortium, overall coordination, logistical coordination, organ collection and processing, library preparation and sequencing, Computational data analysis, et al. Single-cell transcriptomics of 20 mouse organs creates a Tabula Muris. Nature. 2018;562:367–72.: https://www.nature.com/articles/s41586-019-1049-y
.. _Lubeck E, Coskun AF, Zhiyentayev T, Ahmad M, Cai L. Single-cell in situ RNA profiling by sequential hybridization. Nat. Methods. 2014. p. 360–361.: https://www.nature.com/articles/nbt.4260


:bdg-link-primary:`Giotto GitHub <https://github.com/RubD/Giotto/>` :bdg-link-danger:`Report Issue <SubmittingGitHubIssues>`
