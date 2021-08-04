
#To load data 'data' function can be used
data("ToothGrowth")

# View function shows data in different tab
View(ToothGrowth)

#fileter function can be used on the dataset 
filtered_tg <- filter(ToothGrowth, dose==0.5)
View(filtered_tg)

#'arrange' function can be used to filter by column
arrange(filtered_tg, len)

#lets try nested function

arrange(filter(ToothGrowth, dose==0.5), len)

#lets use pipe now: set the to the data set and use pipe

filtered_toothgrowth <- ToothGrowth %>% 
  filter(dose==0.5) %>% 
  group_by(supp) %>% 
  summarize(mean_len = mean(len, na.rm = T), .group="drop")

