#######################
Giotto
#######################

The Giotto package consists of two modules, Giotto Analyzer and  `Giotto Viewer <www.spatialgiotto.com>`_, which provide tools to process, analyze and visualize **single-cell spatial expression data**. The underlying framework is generalizable to virtually all currently available spatial datasets. We recently demonstrated the general applicability on 10 different datasets created by 9 different state-of-the-art spatial technologies, including in situ hybridization (seqFISH+, merFISH, osmFISH), sequencing (Slide-seq, Visium, STARmap) and imaging-based multiplexing/proteomics (CyCIF, MIBI, CODEX). These technologies differ in terms of resolution (single cell vs multiple cells), spatial dimension (2D vs 3D), molecular modality (protein vs RNA), and throughput (number of cells and genes). More information and documentation about the latest version of Giotto Analyzer can be found at https://rubd.github.io/Giotto_site/ (**URL CHANGE**).

.. image:: images/overview_datasets.png
    :width: 400
    :alt: Image showing the overview of Spatial Giotto
    :align: center

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

*******************************
Other Relevant information
*******************************

Relevant Links
=======================================

`Source code <https://github.com/RubD/Giotto/>`__ 
---------------------------------------------------------

`Report a bug <https://github.com/RubD/Giotto/issues>`__
---------------------------------------------------------

License
=====================
`MIT`_ | `File License`_ 

.. _MIT: https://opensource.org/licenses/mit-license.php
.. _File License: https://rubd.github.io/Giotto_site/LICENSE-text.html

How to Cite Giotto?
==========================================

* `Dries et al. Giotto, a toolbox for integrative analysis and visualization of spatial expression data. bioRxiv (2020).`_
* `Dries, R., Zhu, Q., Dong, R., Eng, C. H. L., Li, H., Liu, K., ... & Yuan, G. C. (2021). Giotto: a toolbox for integrative analysis and visualization of spatial expression data. Genome biology, 22(1), 1-31. <https://pubmed.ncbi.nlm.nih.gov/33685491/>`_


.. _Dries et al. Giotto, a toolbox for integrative analysis and visualization of spatial expression data. bioRxiv (2020).: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02286-2

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

.. toctree information below

.. toctree::
   :maxdepth: 2
   :caption: General 
   :hidden:

   Installation <gettingstarted.rst> 
   Giotto Workflow <giottoworkflowanalyses.rst>
   Example Datasets <datasets.rst>  
   Giotto Functions <documentation.rst>
   Tips and Tricks <tipsandtricks.rst>
   Try Giotto <trygiotto.rst>
   
.. toctree::
   :maxdepth: 1
   :caption: Supplemental Information
   :hidden:
   
   Errors and FAQS <errorsfaqsandtips.rst>
   Changelog <additionalinformation.rst>
   Browse Source Code <https://github.com/RubD/Giotto/>
   Report a Bug <https://github.com/RubD/Giotto/issues>
   Contribute <contribute.rst>

