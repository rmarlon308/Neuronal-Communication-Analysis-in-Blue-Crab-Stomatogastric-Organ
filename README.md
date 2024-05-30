# Information Theory Practice
This project analyzes data from two neurons (LP and VD) in the blue crab's stomatogastric organ. Using information theory techniques (entropy, mutual information, temporal and SAX coding), it aims to unveil communication patterns between these neurons in control, GABA injection, and recovery conditions.

## Comparison of SAX and Temporal Encoding Results

The differences between the results obtained using SAX encoding versus temporal encoding have been studied. It was observed that both methods yield equivalent results for small window sizes. However, discrepancies arise as the window size increases.

For the GABA and Recovery files, the results with SAX encoding were very similar, unlike with temporal encoding. This similarity is attributed to the averaging of data within each window in SAX encoding, which, as the window size increases, makes it more likely for the average to fall below the threshold. This occurred because two standard deviations had to be taken into account due to noise in the signal. As a result, the encodings became very similar, with most values falling below the threshold. This issue did not occur with the control signal encoding, where only one standard deviation was used due to the minimal noise, avoiding sample contamination. Using only one standard deviation in noisy signals resulted in erroneous outcomes.

Additionally, the neuronal signal encodings for both neurons were compared. It was found that there is a relationship between the activation of the VD and LP neurons. Whenever one neuron activates, the other follows shortly after.

## Files

### Temporal Spike Encoding
These files contain the temporal spike encoding for different stages:

- **analisis_control.ipynb**: Contains the encoding for the control stage.
- **analisis_gaba.ipynb**: Contains the encoding for the GABA stage.
- **analisis_recuperacion.ipynb**: Contains the encoding for the recovery stage.

### SAX Encoding of Signals
These files contain the SAX encoding for different stages:

- **analisis_control_sax.ipynb**: Contains the SAX encoding for the control stage.
- **analisis_gaba_sax.ipynb**: Contains the SAX encoding for the GABA stage.
- **analisis_recuperacion_sax.ipynb**: Contains the SAX encoding for the recovery stage.

### Functions File
- **funcs.py**: Includes two functions used for threshold calculation and generating encoding graphs.
