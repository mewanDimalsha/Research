import utils.clients
import utils.http_session
import utils.transport
import utils.session
import os
import wfdb

os.makedirs('data', exist_ok=True)
wfdb.dl_database('mitdb', 'data', records='all')


# Load the record and annotations (first 3000 samples for demo)
record = wfdb.rdsamp('mitdb/100', pn_dir='data', sampto=3000)
annotation = wfdb.rdann('mitdb/100', 'atr', pn_dir='data', sampto=3000)

# Print the first few samples and channel names
print("Signal data (first 5 samples):")
print(record.p_signals[:5])
print("\nChannel names:", record.signame)

# Plot the record with annotations and ECG grids
wfdb.plot_wfdb(record=record, annotation=annotation, plot_sym=True,
                time_units='seconds', title='MIT-BIH Record 100', figsize=(10,4), ecg_grids='all')

