library(gsubfn)
library(rgl)

list <- structure(NA, class = "result")
"[<-.result" <- function(x, ..., value) {
  args <- as.list(match.call())
  args <- args[-c(1:2, length(args))]
  length(value) <- length(args)
  for (i in seq(along = args)) {
    a <- args[[i]]
    if (!missing(a)) eval.parent(substitute(a <- v, list(a = a, v = value[[i]])))
  }
  x
}

read_data <- function() {
  data <- read.csv(
        file = "../results/results.csv", header = FALSE, sep = ";",
        row.names = NULL, stringsAsFactors = FALSE
    )

  colnames(data) <- c("algorithm", "answer", "runtime", "vertices", "edges")

  ek_data <- data[data$algorithm == "EK",]
  mpm_data <- data[data$algorithm == "MPM",]
  dinic_data <- data[data$algorithm == "Dinic",]

  ek_data$algorithm <- NULL
  mpm_data$algorithm <- NULL
  dinic_data$algorithm <- NULL

  ek_data <- ek_data[!(ek_data$answer == -1 | ek_data$runtime >= 100),]
  mpm_data <- mpm_data[!(mpm_data$answer == -1 | mpm_data$runtime >= 100),]
  dinic_data <- dinic_data[!(dinic_data$answer == -1 | dinic_data$runtime >= 100),]

  ek_data <- ek_data[order(ek_data[, "vertices"], + ek_data[, "edges"]),]
  mpm_data <- mpm_data[order(mpm_data[, "vertices"], + mpm_data[, "edges"]),]
  dinic_data <- dinic_data[order(dinic_data[, "vertices"], + dinic_data[, "edges"]),]

  return(list(
        "ek_data" = ek_data, "mpm_data" = mpm_data,
        "dinic_data" = dinic_data
    ))
}

plot_runtime_edges_foreach_vertice <- function(data) {
  data <- data[order(data[, "vertices"], + data[, "edges"]),]

  unique_vertices <- unique(data$vertices)
  print(unique_vertices)

  par(mfrow = c(2, 2))
  i = 0
  for (vertice in unique_vertices) {
    filtered <- data[data$vertices == vertice,]
    filtered <- filtered[order(filtered[, "edges"]),]
    plot(filtered$edges, filtered$runtime)
    i = i + 1

    if (i == 3) {
      x11()
      i = 0
    }
  }
}

main <- function() {
  list[ek_data, mpm_data, dinic_data] <- read_data()

  plot(ek_data$runtime ~ (ek_data$vertices + ek_data$edges))
  plot(ek_data)

  plot_runtime_edges_foreach_vertice(ek_data)
  plot_runtime_edges_foreach_vertice(mpm_data)
  plot_runtime_edges_foreach_vertice(dinic_data)

  regression <- lm(ek_data$runtime ~ ek_data$vertices + ek_data$edges)
  summary(regression)

  regression <- lm(ek_data$runtime ~ ek_data$vertices + ek_data$edges)
  summary(regression)

  regression <- lm(ek_data$runtime ~ poly(ek_data$vertices + ek_data$edges, 3))
  summary(regression)
}
