#funções
sim2dist <- function(x, maxSim = 1) #função que transforma uma matriz de similaridade em um vetor de distâncias
{
  stopifnot(is.matrix(x))
  stopifnot(isSymmetric(x))
  stopifnot(maxSim >= max(x))
  d <- maxSim - x # from similarity to distance
  return(as.dist(d))
}
stress <- function(data,imax=100) #função que tretorna um conjunto do stress 
{
  par <- 1:imax #ciracao do vetor com as dimensoes possiveis
  stss <- rep(0,imax) #criacao do vetor nulo com os valores da funcao stress
  for (i in par) stss[i] <- isoMDS(data, y=cmdscale(data,i), k=i, maxit = 50000)$stress
  return(stss)
}

#bibliotecas
require(graphics)
library(MASS)

#programa principal
data <- read.table('Data_Similarity_Full_5.txt', header=TRUE) #leitura do data frame
data.dist <- sim2dist(data.matrix(data)) #transformação do data frame em um vetor de distâncias
data.MDS<-isoMDS(data.dist, y=cmdscale(data.dist,2), k=2, maxit = 50000) #calcuo do Multidimensional Scaling
nclust <- 4 #número de clusters que separaremos os dados
data.clust <- hclust(data.dist,method ="ward")
clusters <- cutree(data.clust,k=nclust)
png("Graph_hclust.png", width=1400, height=1000)
plot (data.clust,cex=1)
rect.hclust(data.clust, k=nclust, border=clusters)
dev.off()
png("Graph_dms.png", width=1400, height=1000)
x <- data.MDS$points[,1]
y <- data.MDS$points[,2]
plot (x,y,pch=20,col='white', xlab=" ",ylab=" ",cex=2)
text (x,y,labels=colnames(data), cex=1)
dev.off()
data.stress <- stress(data.dist,50)
png("Graph_stress.png", width=1400, height=1000)
plot(data.stress,pch=20,cex=2)
dev.off()

