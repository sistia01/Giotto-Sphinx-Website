.. _calculateMetaTable: 

####################################
Calculate Average Gene Expression 
####################################

.. describe:: calculateMetaTable()

*Function to calculate the average gene expression for one or more (combined) annotation columns.*

.. code-block::

	calculateMetaTable(
  		gobject,
  		expression_values = c("normalized", "scaled", "custom"),
  		metadata_cols = NULL,
  		selected_genes = NULL
	)

**********************
Arguments
**********************

.. list-table::
	:widths: 100 100 
	:header-rows: 0 

	* - **gobject**	
	  - giotto object
	* - **expression_values**	
	  - expression values to use
	* - **metadata_cols**	
	  - annotation columns found in pDataDT(gobject)
	* - **selected_genes**	
	  - subset of genes to use

******************
Value 
******************

A ``data.table`` with average expression values for each gene per (combined) annotation

*******************
Examples
*******************

.. code-block::

	data(mini_giotto_single_cell)

**Show cell metadata**

..  code-block::

	pDataDT(mini_giotto_single_cell)
	#>      cell_ID nr_genes perc_genes total_expr leiden_clus cell_types
	#>  1:   cell_2       13         65  111.98320           3     cell C
	#>  2:   cell_7       15         75  115.73030           3     cell C
	#>  3:  cell_12       11         55   95.49802           1     cell A
	#>  4:  cell_15       12         60   99.94782           3     cell C
	#>  5:  cell_17       13         65  111.32963           2     cell B
	#>  6:  cell_30       11         55   96.64302           3     cell C
	#>  7:  cell_37        6         30   57.77777           2     cell B
	#>  8:  cell_40        9         45   82.84693           2     cell B
	#>  9:  cell_44        9         45   79.93838           2     cell B
	#> 10:  cell_53        9         45   82.40747           1     cell A
	#> 11:  cell_64        8         40   73.06345           1     cell A
	#> 12:  cell_74       11         55   93.04295           3     cell C
	#> 13:  cell_85        8         40   73.72574           1     cell A
	#> 14:  cell_86       14         70  115.75186           1     cell A
	#> 15:  cell_90       11         55   93.02181           1     cell A
	#> 16:  cell_95        6         30   59.55714           1     cell A
	#> 17:  cell_96       10         50   88.31757           1     cell A
	#> 18: cell_107       16         80  130.62640           1     cell A
	#> 19: cell_113       12         60   99.83100           2     cell B
	#> 20: cell_118       14         70  117.63523           2     cell B

**Show average gene expression per annotated cell type** 

.. code-block::

	calculateMetaTable(mini_giotto_single_cell,
                   metadata_cols = 'cell_types')
	#>     cell_types uniq_ID variable     value
	#>  1:     cell C  cell C    Cldn5  4.262769
	#>  2:     cell A  cell A    Cldn5  0.000000
	#>  3:     cell B  cell B    Cldn5  4.601433
	#>  4:     cell C  cell C    Rtn4r  8.651224
	#>  5:     cell A  cell A    Rtn4r  5.670079
	#>  6:     cell B  cell B    Rtn4r  2.742910
	#>  7:     cell C  cell C      Vgf  8.625694
	#>  8:     cell A  cell A      Vgf  9.097362
	#>  9:     cell B  cell B      Vgf  1.291685
	#> 10:     cell C  cell C   Lingo1 10.013670
	#> 11:     cell A  cell A   Lingo1  8.728317
	#> 12:     cell B  cell B   Lingo1  3.098198
	#> 13:     cell C  cell C  Slc17a7 10.102439
	#> 14:     cell A  cell A  Slc17a7  9.879413
	#> 15:     cell B  cell B  Slc17a7  5.131600
	#> 16:     cell C  cell C    Lynx1  4.814888
	#> 17:     cell A  cell A    Lynx1  4.281796
	#> 18:     cell B  cell B    Lynx1  2.661027
	#> 19:     cell C  cell C   Atp1a1  9.852690
	#> 20:     cell A  cell A   Atp1a1  9.800178
	#> 21:     cell B  cell B   Atp1a1  4.671602
	#> 22:     cell C  cell C     Scg3  0.000000
	#> 23:     cell A  cell A     Scg3  3.376464
	#> 24:     cell B  cell B     Scg3  8.806105
	#> 25:     cell C  cell C     Myh9  3.039197
	#> 26:     cell A  cell A     Myh9  2.769607
	#> 27:     cell B  cell B     Myh9  5.697493
	#> 28:     cell C  cell C   Pcp4l1  5.888908
	#> 29:     cell A  cell A   Pcp4l1  4.801477
	#> 30:     cell B  cell B   Pcp4l1  2.795894
	#> 31:     cell C  cell C     Pygb  1.426957
	#> 32:     cell A  cell A     Pygb  3.735340
	#> 33:     cell B  cell B     Pygb  8.794492
	#> 34:     cell C  cell C   Col4a2  1.229003
	#> 35:     cell A  cell A   Col4a2  3.545717
	#> 36:     cell B  cell B   Col4a2  7.331353
	#> 37:     cell C  cell C     Sdc4  3.271337
	#> 38:     cell A  cell A     Sdc4  2.541195
	#> 39:     cell B  cell B     Sdc4  7.439861
	#> 40:     cell C  cell C    Csf1r  3.089642
	#> 41:     cell A  cell A    Csf1r  3.295176
	#> 42:     cell B  cell B    Csf1r  3.845324
	#> 43:     cell C  cell C   Mtss1l  6.170010
	#> 44:     cell A  cell A   Mtss1l  2.532647
	#> 45:     cell B  cell B   Mtss1l  7.361713
	#> 46:     cell C  cell C  Slc32a1  1.793733
	#> 47:     cell A  cell A  Slc32a1  4.012130
	#> 48:     cell B  cell B  Slc32a1  0.000000
	#> 49:     cell C  cell C   Adarb2  4.278583
	#> 50:     cell A  cell A   Adarb2  1.731363
	#> 51:     cell B  cell B   Adarb2  1.263504
	#> 52:     cell C  cell C    Abtb2  4.278583
	#> 53:     cell A  cell A    Abtb2  1.682614
	#> 54:     cell B  cell B    Abtb2  2.447522
	#> 55:     cell C  cell C    Htra1  6.193813
	#> 56:     cell A  cell A    Htra1  1.533463
	#> 57:     cell B  cell B    Htra1  6.424891
	#> 58:     cell C  cell C    Cplx1  6.486320
	#> 59:     cell A  cell A    Cplx1  7.204490
	#> 60:     cell B  cell B    Cplx1  5.153216
	#>     cell_types uniq_ID variable     value

