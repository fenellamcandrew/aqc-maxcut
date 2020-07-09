###############################################################################
# EDA
#
# Author: Vivek Katial
# Created 2020-07-10 00:32:53
###############################################################################

#' You'll need to install tidyverse and janitor to run this code

# Import libraries
library(tidyverse)

# Load data
d_runs <- read_csv("data/d_runs.csv") %>% 
    janitor::clean_names() %>% 
    filter(status == "FINISHED")

d_runs %>% 
    group_by(params_n_qubits, params_graph_type) %>% 
    filter(params_n_qubits > 7) %>% 
    summarise(mean_entang = mean(metrics_max_entanglement, na.rm = T)) %>% 
    ggplot(aes(x = params_n_qubits, y = mean_entang, col = params_graph_type)) + 
    geom_line() + 
    scale_x_continuous(breaks = scales::pretty_breaks())

d_runs %>% 
    filter(params_n_qubits > 7) %>% 
    ggplot(aes(x = metrics_max_entanglement, y = metrics_prob_success)) +
    geom_point(alpha = 0.15) + 
    facet_wrap(~params_n_qubits+params_t)

d_runs %>% 
    filter(params_n_qubits > 7) %>% 
    ggplot(aes(x = as.factor(params_n_qubits), y = metrics_prob_success)) +
    geom_boxplot() + 
    facet_wrap(~params_graph_type)
