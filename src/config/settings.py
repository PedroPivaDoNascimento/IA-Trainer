SCORING_PIPELINE_MAP = {
    'r2': 'r2',
    'mae': 'neg_mean_absolute_error',
    'mse': 'neg_mean_squared_error',
    'rmse': 'neg_root_mean_squared_error'
}

METRIC_SCORING_MAP = {
    'r2': 'r2',
    'mae': 'mae',
    'mse': 'mse',
    'rmse': 'rmse'
}

STD_MAP = {
    'r2': 'std_test_r2',
    'mae': 'std_test_mae',
    'mse': 'std_test_mse',
    'rmse': 'std_test_rmse'
}