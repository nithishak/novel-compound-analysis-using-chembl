source('config.r') 
library(ggplot2)
library(limma)



#Function 1 : Plot histograms of how similar compounds from CHEMBL similarity search results are to the actual compound
plotHistogram <- function(working_dir_hist, filePattern_hist) {
  setwd(working_dir_hist)
  file_list = list.files(pattern = filePattern_hist)
  for (file_name in file_list){
     df = read.csv(file= file_name, stringsAsFactors = FALSE)
     title = paste("Histogram for",sub(filePattern_hist,"",file_name), sep = ' ')
     print (title)

     histogram <- ggplot(df, aes(x= similarity)) +
       geom_histogram(aes(y = ..density..), binwidth = 0.25, color= "white") + 
       geom_density(alpha=.2, fill="#FF6666", color= "red")  +
       scale_x_continuous(name="similarity(%)", breaks = seq(70,100,2), limits=c(70,100)) +
       scale_y_continuous(name="Density") +
       ggtitle(title) +
       theme_bw() + 
       theme(plot.title = element_text(size=16, hjust=0.5, face= "bold"), axis.title = element_text(size=12)) 

       print (histogram)
       hist_file_name = paste0("hist_for_", sub(filePattern_hist,"",file_name), '.png')
       ggsave(hist_file_name, width =8, height = 6, dpi = 84)
       
     }
   }

#Function 2: Plot bar plots to understand genes for targets that similar compounds targeted the most
plotBarGraphs <- function (working_dir_barplots, filePattern_barplot){
  setwd(working_dir_barplots)
  file_list = list.files(pattern = filePattern_barplot)
  for (file_name in file_list){
    title <- paste("Bar plot for", sub(filePattern_barplot,"",file_name), sep =' ')
    df <- read.csv(file_name, stringsAsFactors = FALSE)
    df$Official_Symbol <- alias2SymbolTable(df$component_synonym) #standardizing gene symbols for future comparisons across all files, to eliminate gene synonyms
    df <- df[!is.na(df$Official_Symbol),] #remove all gene symbols which are NA
    dff <- df [1:20,] #choose top 20 genes, meaning these genes for the protein targets that were targeted the most by compounds similar to the compound of interest during CHEMBL similarity search

    bar_plot <- ggplot(data=dff, aes(x= reorder(Official_Symbol, -count), y= count)) + #organizes genes from largest to smallest count in plot
    geom_bar(stat="identity", fill= "orange", color = "black") +
    labs (x="Gene Symbols", y= "Frequency",title = title) +
    theme_bw() +
    theme(axis.text.x = element_text(size  = 10, angle = 45,hjust = 1, vjust = 1)) +
    theme(plot.title = element_text(hjust = 0.5)) +
    theme(plot.title = element_text(size=16, hjust=0.5, face= "bold"), axis.title = element_text(size=12))
    
   
    print(bar_plot)
    barplot_file_name = paste0("barplot_for_", sub(filePattern_barplot,"",file_name), '.png')
    ggsave(barplot_file_name, width =8, height = 6, dpi = 84)
  }
}
