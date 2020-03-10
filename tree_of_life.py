from ete import NCBITaxa
import pandas as pd

orthologs=read_table('/h')
ncbi = NCBITaxa()
ncbi.update_taxonomy_database()
