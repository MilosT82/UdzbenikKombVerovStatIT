ocene<-c(6,7,10,8,6,9,8,7,8,8,9,8,10)
ocene1<-read.delim("clipboard")

prosek<-mean(ocene)
prosek
varijansa<-var(ocene)
varijansa
StDevijacija<-sd(ocene)
StDevijacija

#install.packages("modeest")
library(modeest)
modus<-mfv(ocene)
modus
medijana<-median(ocene)
medijana
PrviKvartil<-quantile(ocene, 0.25)
PrviKvartil
TreciKvartil<-quantile(ocene, 0.75)
TreciKvartil
maksimum<-max(ocene)
maksimum
minumum<-min(ocene)
minumum
opseg<-max(ocene)-min(ocene)
opseg

library(moments)
skew<-skewness(ocene)
skew
kurt<-kurtosis(ocene)
kurt

pregled<-summary(ocene)
pregled

hist(ocene) #grafikon