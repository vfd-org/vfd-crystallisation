import math

import numpy as np

from src.statistics import aic, bic, delta_metric, metrics_row, reduced_chi_square


def test_reduced_chi2_simple():
    assert reduced_chi_square(20.0, n_data=22, n_params=2) == 1.0


def test_reduced_chi2_dof_zero_returns_nan():
    assert math.isnan(reduced_chi_square(5.0, n_data=2, n_params=2))


def test_aic_increases_with_parameters_at_fixed_chi2():
    a1 = aic(10.0, n_params=2)
    a2 = aic(10.0, n_params=4)
    assert a2 > a1


def test_bic_increases_with_parameters_at_fixed_chi2():
    b1 = bic(10.0, n_params=2, n_data=30)
    b2 = bic(10.0, n_params=4, n_data=30)
    assert b2 > b1


def test_bic_penalty_heavier_for_large_n():
    # BIC penalty per parameter is ln N — heavier than AIC's 2.
    assert (bic(10.0, 4, 30) - bic(10.0, 2, 30)) > (aic(10.0, 4) - aic(10.0, 2))


def test_delta_metric_signs():
    assert delta_metric(15.0, 10.0) == 5.0
    assert delta_metric(8.0, 10.0) == -2.0


def test_metrics_row_shape():
    row = metrics_row("LCDM", chi2=20.0, n_params=2, n_data=22)
    for key in ("model", "chi2", "n_params", "n_data", "chi2_red", "aic", "bic"):
        assert key in row
