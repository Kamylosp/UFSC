
x = c(172, 132,	166, 186, 243, 186,	209, 128,
      169, 178, 221, 191, 196, 169, 119, 119,
      135, 78, 162, 186, 135,	149, 124,	114,
      95,	136, 116,	103, 119,	114, 176,	180,
      186, 187,	199, 188,	157, 151, 164,165)
      
#Obtendo Informacoes
media_amostra <- mean(x)
mediana_amostra <- median(x)
minimo_amostra <- min(x)
maximo_amostra <- max(x)
quartil_1 <- quantile(x, 0.25)
quartil_3 <- quantile(x, 0.75)
quartis <- quantile(x, c(0.25, 0.75))
amplitude <- (range(x))[2] - (range((x)))[1]



#hist(x, main = paste("Histograma aula 16/03/23"), 
#     xlab = "[cm]", breaks = "Sturges", col = "lightgreen", lwd=3)

#abline(v=mean(x), h=0, lwd=2, col="red")

boxplot(x)
