# GO Finder
Program: to find GO terms from a given text file

Gene Ontology or GO are a formal respresentatio desrcibing the biological domain with relations to operate them.
It is defined in three aspects:
1. Molecular function - Molecular level activities performed by gene products.
2. Cellular compononet - The locations relative to cellular structures in which a gene product performs a function.
3. Biological prcoess - the larger processes accomplished by moleclar activites.

##Usage:
usage: goterms.py [-h] str

positional arguments:
  str         GO text file

optional arguments:
  -h, --help  show this help message and exit
  
The input for this program can be a single GO term or GO terms stored as a text file.

The output for the program is given as for the GO:0005814  is shown as:
GO:0005814      level-05        depth-05        centriole [cellular_component]

##Installations:
Your python environment must be set up with:

<pip install goatools>

To install the development version:

<pip install git+git://github.com/tanghaibao/goatools.git>

.obo file for the most current GO:

<wget http://geneontology.org/ontology/go-basic.obo>


###Yet to update:
Test suite,
Function or option to sift through Biological process, Molecular function and Cellular compononet.

Author: Sri Harsha Vishwanath
