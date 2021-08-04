#practice R functions and analysis of data withing tidyverse
#head function displays all columns and first several rows

head(diamonds)

#str function arranges the data horizontally

str(diamonds)

#glimpse is similar to str function

glimpse(diamonds)

#col names function yields columns names

colnames(diamonds)

#rename function is straight forward

rename(diamonds, carat_new = carat, cut_new = cut)

summarize(diamonds, mean_price = mean(price))

# Now lets build first visualization using R
#plus with ggplot helps add additional features to the plot

ggplot(data = diamonds, aes(x = carat, y = price, color = cut)) + 
  geom_point() + facet_wrap(~cut)
