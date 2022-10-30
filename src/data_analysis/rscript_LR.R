#ALTEREM O SOURCE DOS RESULTS!!!
data <- read.csv(file = "C:/Users/Junior/Desktop/results/results.csv", header = FALSE,  sep = ";", row.names = NULL,  stringsAsFactors = FALSE)
colnames(data) = c("algorithm", "answer", "runtime", "vertices", "edges")

EK_data <- data[data$algorithm == 'EK',]
MPM_data <- data[data$algorithm == 'MPM',]
Dinic_data <- data[data$algorithm == 'Dinic',]

EK_data_vertices = EK_data[order(EK_data[,'vertices'], +EK_data[,'edges']),]
EK_data_vertices = EK_data_vertices[!duplicated(EK_data_vertices$vertices),]

MPM_data_vertices = MPM_data[order(MPM_data[,'vertices'], +MPM_data[,'edges']),]
MPM_data_vertices = MPM_data_vertices[!duplicated(MPM_data_vertices$vertices),]

Dinic_data_vertices = Dinic_data[order(Dinic_data[,'vertices'], +Dinic_data[,'edges']),]
Dinic_data_vertices = Dinic_data_vertices[!duplicated(Dinic_data_vertices$vertices),]

#-------------------VERTICES-----------------------

#Linear regression EK vertices
plot(EK_data_vertices$vertices, EK_data_vertices$runtime)
Vlinear_reg_EK = lm(EK_data_vertices$runtime ~ EK_data_vertices$vertices)
summary(Vlinear_reg_EK)
abline(Vlinear_reg_EK)

#Linear regression MPM vertices
plot(MPM_data_vertices$vertices, MPM_data_vertices$runtime)
Vlinear_reg_MPM = lm(MPM_data_vertices$runtime ~ MPM_data_vertices$vertices)
summary(Vlinear_reg_MPM)
abline(Vlinear_reg_MPM)

#Linear regression Dinic vertices
plot(Dinic_data_vertices$vertices, Dinic_data_vertices$runtime)
Vlinear_reg_Dinic = lm(Dinic_data_vertices$runtime ~ Dinic_data_vertices$vertices)
summary(Vlinear_reg_Dinic)
abline(Vlinear_reg_Dinic)

#-------------------EDGES-----------------------

#Linear regression EK edges
plot(EK_data_vertices$edges, EK_data_vertices$runtime)
Elinear_reg_EK = lm(EK_data_vertices$runtime ~ EK_data_vertices$edges)
summary(Elinear_reg_EK)
abline(Elinear_reg_EK)

#Linear regression MPM edges
plot(MPM_data_vertices$edges, MPM_data_vertices$runtime)
Elinear_reg_MPM = lm(MPM_data_vertices$runtime ~ MPM_data_vertices$edges)
summary(Elinear_reg_MPM)
abline(Elinear_reg_MPM)

#Linear regression Dinic edges
plot(Dinic_data_vertices$edges, Dinic_data_vertices$runtime)
Elinear_reg_Dinic = lm(Dinic_data_vertices$runtime ~ Dinic_data_vertices$edges)
summary(Elinear_reg_Dinic)
abline(Elinear_reg_Dinic)
