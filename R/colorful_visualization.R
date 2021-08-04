install.packages('Tmisc')
library(Tmisc)
data(quartet)
View(quartet)

quartet %>% 
  group_by(set) %>% 
  summarize(mean(x),sd(x),mean(y),sd(y),cor(x,y))

ggplot(quartet, aes(x,y), colour=dataset) + geom_point() +geom_smooth(method=lm,se=FALSE) +facet_wrap(~set)


install.packages("datasauRus")
library(datasauRus)

ggplot(datasaurus_dozen,aes(x=x,y=y,colour=dataset)) + geom_point()+theme(legend.position = "none") +facet_wrap(~dataset) 

penguins %>% 
  drop_na() %>% 
  group_by(species) %>% 
  summarize(min(bill_depth_mm))