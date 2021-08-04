#more on visualization
install.packages("tidyverse")
library(tidyverse)
install.packages("palmerpenguins")
library(palmerpenguins)

#now the visualization part starts for penguin dataset

ggplot(data=penguins)+geom_point(mapping=aes(x=flipper_length_mm,y=body_mass_g,color=species,shape=species))+
  geom_smooth(mapping=aes(x=flipper_length_mm,y=body_mass_g)) +
  facet_wrap(~species)+ labs(title="Palmer Penguins: Body Mass vs Flipper Length")

ggplot(data=penguins)+geom_point(mapping=aes(x=flipper_length_mm,y=body_mass_g,color=species))+
  facet_wrap(~species)


#lets work with different dataset now 

ggplot(data=diamonds) + geom_bar(mapping=aes(x=color,fill=cut)) +
  facet_wrap(~color)


