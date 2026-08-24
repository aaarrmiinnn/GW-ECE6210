"""Local datasets used by the ECE 6210 lecture notebooks."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.utils import Bunch


DATA_DIRECTORY = Path(__file__).resolve().parent / "data"


def load_gas_sensor_drift(as_frame: bool = False) -> Bunch:
    """Load the UCI gas-sensor drift dataset stored with the course."""

    archive = np.load(DATA_DIRECTORY / "gas_sensor_drift.npz")
    data = archive["X"]
    target = archive["gas_id"].astype(int)
    concentration = archive["concentration"]
    batch = archive["batch"].astype(int)
    feature_names = archive["feature_names"]
    target_names = archive["gas_names"]

    frame = None
    if as_frame:
        frame = pd.DataFrame(data, columns=feature_names)
        frame["gas_id"] = target
        frame["gas"] = pd.Categorical.from_codes(target, target_names)
        frame["concentration_ppmv"] = concentration
        frame["batch"] = batch
        data = frame.loc[:, feature_names]
        target = frame["gas_id"]
        concentration = frame["concentration_ppmv"]
        batch = frame["batch"]

    return Bunch(
        data=data,
        target=target,
        concentration=concentration,
        batch=batch,
        feature_names=feature_names,
        target_names=target_names,
        frame=frame,
        DESCR=(
            "Measurements from 16 chemical sensors exposed to six gases at "
            "different concentrations. The 128 features summarize steady-state "
            "and transient sensor responses."
        ),
    )


def load_smartphone_activity_signals() -> Bunch:
    """Load the compact UCI smartphone inertial-signal sample."""

    archive = np.load(DATA_DIRECTORY / "smartphone_activity_signals.npz")
    return Bunch(
        signals=archive["signals"],
        target=archive["activity_id"].astype(int),
        subject=archive["subject_id"].astype(int),
        target_names=archive["activity_names"],
        channel_names=archive["channel_names"],
        DESCR=(
            "A balanced sample of 600 windows from the UCI Human Activity "
            "Recognition Using Smartphones dataset. Each window contains 128 "
            "samples from three accelerometer and three gyroscope channels."
        ),
    )
