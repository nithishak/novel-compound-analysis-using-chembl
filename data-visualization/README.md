# Project name

Density histograms to compare compounds similarity distribution <br>
                        and <br>
Barplots to understand top gene hits for similar compounds <br>

## Environment 
- OS- Ubuntu
- R 3.4.1

## Objective: 
- To plot density histograms to visually represent the similarity distribution of compounds (in other words to answer the question: How similar are the similar compounds to the compound of interest?)
-To plot bar plots of top 20 genes for proteins that the similar compounds target

## Libraries needed: 
1. ggplot2 <br>
To install: <br>
````install.packages("ggplot2")````
2. limma <br>
To install: <br>
source("https://bioconductor.org/biocLite.R") <br>
biocLite("limma")

## Inputs needed:
1. Any file that contains list of similar compounds ('Sim.csv' files)
2. Any file that contains list of genes/compound_synonyms for proteins that similar compounds target ('genes.csv' files)

## Files available:
1. config.py - contains input fields as a R list
2. functions.py - contains several helper functions
3. main.py - contains main code which uses the helper functions

## Details:
- From our previous CHEMBL_analysis, we have, a file ending with Sim.csv that contains the list of compounds which are 70% or more similar to the compound of interest, as well as a file ending with gene.csv that contains the genes for proteins that the similar compounds are likely to target.
- Density Histogram:
We can plot density histograms to see the similarity distributions across similar compounds. Sim.csv files are used for these plots.
The plot should look something like this: <br>
![1](https://user-images.githubusercontent.com/35882413/36400604-ea39392c-159f-11e8-99c3-6bfdf6de813e.png)
- Barplots:
We can also plot bar graphs to look at genes for the 20 most targeted proteins by similar compounds. genes.csv files are used for these plots.
The plot should look something like this: <br>
![2](https://user-images.githubusercontent.com/35882413/36400605-ea4e6e00-159f-11e8-89e9-9de8d88a02e5.png)

## How to run? :
- Change required input fields in the config.py file and set relevant paths.
- Run commands from the main.py file.
