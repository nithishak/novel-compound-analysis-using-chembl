# Project name
Systematic approach utilizing CHEMBL similarity search to find genes for possible protein targets of a novel compound.

## Environment
- OS: Ubuntu
- Python : 2.X
- R : 3.4.1

## Project description
- This project is meant to be applied in situations where a novel compound has been discovered but limited to no literature is present in order to 
give a better understanding of the mechanism of action or target protein.
- There are 2 parts to this project:
1. Chembl Analysis - The first part involves performing a similarity search in CHEMBL for compounds that share 70% or more chemical structure similarity to 
the novel compound. To do this, the canonical smiles of the novel compound is used. In addition to finding out the list of similar compounds, 
SQL inner joins can be performed to further understand the activities of these compounds and the genes for the proteins they target. This approach
gives us a better picture of what protein the novel compound may be targetting.
2. Data visualization -The second part relies on visual representations using ggplots to understand the information obtained from part 1 better. 
- Once the list of similar compounds is generated, a denstity histogram can be plotted to look at the distribution of similarity across the compounds. This 
helps answers questions like are most of the similar compounds very similar (above 90% similarity for eg.) to the novel compound? 
- Following this, a bar plot can be plotted to show the genes for the top 20 protein targets of the similar compounds. This gene list can provide
us with an inkling as to what kind of genes the novel compound may be targetting.

## Folders available
1. Chembl_analysis (code in Python)
2. Data_visualization (code in R)

## How to run?
Run the main.py file in Chembl_analysis, followed by main.py in Data_visualization.
