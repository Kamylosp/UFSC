x <- c(174.4,177.9,185.6,180.8,173.9,176.8,165.0,176.4,172.1,170.3,
       172.0,170.4,170.8,175.1,167.3,166.9,165.8,176.1,171.1,174.3,
       179.7,180.8,179.9,169.8,175.6,169.0,173.3,174.6,177.4,174.7,
       168.5,174.1,172.4,178.7,179.0,175.5,181.5,171.0,159.0,164.9,
       179.0,173.9,177.6,172.1,175.5,164.4,167.7,185.2,166.2,172.1)

#Obtendo Informacoes
media_amostra <- mean(x)
mediana_amostra <- median(x)
minimo_amostra <- min(x)
maximo_amostra <- max(x)
quartil_1 <- quantile(x, 0.25)
quartil_3 <- quantile(x, 0.75)
quartis <- quantile(x, c(0.25, 0.75))


print(minimo_amostra)

boxplot(x)