# Course Datasets

## Gas Sensor Array Drift at Different Concentrations

`gas_sensor_drift.npz` contains the complete 13,910 measurements from the UCI dataset. Each measurement has 128 features extracted from 16 chemical sensors. The stored targets are gas identity, gas concentration in parts per million by volume, and acquisition batch.

The source data were downloaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/270/gas%2Bsensor%2Barray%2Bdrift%2Bdataset%2Bat%2Bdifferent%2Bconcentrations). The repository lists the dataset under the Creative Commons Attribution 4.0 license.

Citation:

Alexander Vergara. Gas Sensor Array Drift at Different Concentrations. UCI Machine Learning Repository, 2012. DOI: [10.24432/C5MK6M](https://doi.org/10.24432/C5MK6M).

The `.npz` file is a direct numerical conversion of the ten original batch files. Feature values are stored as 32-bit floating-point numbers. Class identifiers and batch identifiers are stored as integers. No measurements were removed.

## Human Activity Recognition Using Smartphones

`smartphone_activity_signals.npz` contains a balanced sample of 600 windows from the UCI Human Activity Recognition Using Smartphones dataset. Each window contains 128 samples from three accelerometer channels and three gyroscope channels. The file also stores activity and subject identifiers.

The source data were downloaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/240/human%2Bactivity%2Brecognition%2Busing%2Bsmartphones). The repository lists the dataset under the Creative Commons Attribution 4.0 license.

Citation:

Jorge Reyes-Ortiz, Davide Anguita, Alessandro Ghio, Luca Oneto, and Xavier Parra. Human Activity Recognition Using Smartphones. UCI Machine Learning Repository, 2013. DOI: [10.24432/C54S4K](https://doi.org/10.24432/C54S4K).

The course file retains 100 windows from each of the six activities. Sampling uses a fixed random seed. The complete UCI archive is not stored in this repository.
