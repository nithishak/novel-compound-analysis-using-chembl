source('functions.r')

setwd(inputConfig[['working_directory_hist']])

plotHistogram (inputConfig[['working_directory_hist']], inputConfig[['file_pattern_hist']])

plotBarGraphs (inputConfig[['working_directory_barplots']], inputConfig[['filePattern_barplot']])

