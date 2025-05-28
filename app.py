import wfdb
import os

# Download all MIT-BIH Arrhythmia Database files to a local directory
wfdb.dl_database('mitdb', os.getcwd(), records='all')

# Load the record and annotations (sampto=3000 limits to first 3000 samples for quick demo)
record = wfdb.rdsamp('mitdb/100', sampto=3000)
annotation = wfdb.rdann('mitdb/100', 'atr', sampto=3000)

# Print the first few samples and channel names
print("Signal data (first 5 samples):")
print(record.p_signals[:5])
print("\nChannel names:", record.signame)

# Plot the record with annotations and ECG grids
wfdb.plot_wfdb(record=record, annotation=annotation, plot_sym=True,
                time_units='seconds', title='MIT-BIH Record 100', figsize=(10,4), ecg_grids='all')
