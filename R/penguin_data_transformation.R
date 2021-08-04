penguins %>% 
  arrange(bill_length_mm)

#to save results, dataframe needs to be assigned
 penguins2 <- penguins %>% 
   arrange(bill_length_mm)
 View(penguins2)
 
 # groupby and summarize functions uses
 penguins %>% 
   group_by(island)  %>% 
   drop_na() %>% 
   summarize(mean_bill_length_mm=mean(bill_length_mm))
 #max_bill_length
 
 penguins %>% 
   group_by(island)  %>% 
   drop_na() %>% 
   summarize(max_bill_length_mm=max(bill_length_mm))
 
 #max and mean together
 
 penguins %>% 
   group_by(island, species)  %>% 
   drop_na() %>% 
   summarize(max_bl_mm=max(bill_length_mm), mean_bl_mm=mean(bill_length_mm))
 
