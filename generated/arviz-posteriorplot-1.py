import arviz as az
non_centered = az.load_arviz_data('non_centered_eight')
az.posteriorplot(non_centered)
