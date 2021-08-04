#Analyze chocola
install.packages("tidyverse")
library(tidyverse)
#to verify the directory where the file is located
getwd()

#Import data .csv file
flavors_df <- read.csv("flavors.csv", header = TRUE, sep ="," )

#Loading dplyr to perform calculations such as mean,max and sd
library(dplyr)
#renaming columns

flavors_df %>% 
  rename(Brand = Company...Maker.if.known.)
#cleaning data
trimmed_flavors_df <- flavors_df %>%
  select(Rating,Cocoa.Percent,Company.Location)
trimmed_flavors_df

#calculations and summarize
trimmed_flavors_df %>% 
  summarize(mean=mean(Rating))

# conditional formatting in R
best_trimmed_flavors_df <- trimmed_flavors_df  %>% 
  arrange(-Rating)
#Just filter
filter(best_trimmed_flavors_df, Cocoa.Percent > 75% & Rating > 3.9) %>% 
         print(best_trimmed_flavors_df)
         
      print(best_trimmed_flavors_df)

#plot time
ggplot(data = best_trimmed_flavors_df) + geom_bar(mapping=aes(x=Company.Location, color=Rating, fill=Rating)) 

  
 