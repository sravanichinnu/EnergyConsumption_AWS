CREATE OR REPLACE VIEW pjme_predictions_with_error AS
SELECT
    timestamp,
    energy_mw,
    predicted_energy_mw,
    predicted_energy_mw - energy_mw AS error,
    ABS(predicted_energy_mw - energy_mw) AS absolute_error
FROM pjme_xgboost_final_predictions;