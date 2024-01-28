import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.signal import find_peaks
from sklearn.metrics import mutual_info_score, normalized_mutual_info_score
from matplotlib.pyplot import figure
import matplotlib

def getStatsMetrics(signal, dist_sd=1):
    mean = np.mean(signal)
    sd = np.std(signal)
    low, high = mean-dist_sd*sd, mean+dist_sd*sd
    return (mean, sd, low, high)

def getHistSignalPlot(data, mean, low, high, dist_sd, sig_name, umb = 'high', bins=60):
    plt.hist(data, bins=bins)

    plt.axvline(x = high, color='g', linestyle='--', linewidth=2, label = 'Mean + '+str(dist_sd)+'*SD')
    plt.annotate(str(round(mean,2)),(mean + 0.01,0.05e6))

    if umb == 'high':
        plt.axvline(x = mean, color='orange', linestyle='--', linewidth=2, label = 'Mean '+ sig_name)
        plt.annotate(str(round(high,2)),(high + 0.1,0.05e6))
    elif umb == 'low':
        plt.axvline(x = low, color='g', linestyle='--', linewidth=2, label = 'Mean - '+str(dist_sd)+'*SD')
        plt.annotate(str(round(low,2)),(low - 0.2,0.05e6))
    else:
        plt.axvline(x = mean, color='orange', linestyle='--', linewidth=2, label = 'Mean '+ sig_name)
        plt.annotate(str(round(low,2)),(low - 0.2,0.05e6))
        plt.axvline(x = low, color='g', linestyle='--', linewidth=2, label = 'Mean - '+str(dist_sd)+'*SD')
        plt.annotate(str(round(high,2)),(high + 0.1,0.05e6))

    
    plt.title('Histograma '+sig_name)
    plt.xlabel(sig_name)
    plt.ylabel('Frecuencia')
    plt.legend()


def getSpikesPlot(data, break_size, data_init, data_end, high, mean, sig_name):
    data2 = data
    data2 = data2.iloc[data_init:data_end]
    breaks = np.arange(data_init,data_end,break_size)
    data2.loc[:,'breaks'] = np.repeat(breaks,break_size)[0:data_end-data_init]

    for i in breaks[breaks<=data_end]:
        plt.axvline(x=i, color = 'silver', linestyle = '-.')
    plt.plot(data2.Time, data2.iloc[:,list(data2.columns).index(sig_name)], label = 'Señal '+ sig_name)
    plt.scatter(data2.Time[data2['IsSpike'+sig_name] == 1], data2.iloc[:,list(data2.columns).index('Value'+sig_name)][data2['IsSpike'+sig_name] == 1], color = 'r', label = 'Spikes')
    plt.axhline(y = high, color='g', linestyle='--', linewidth=2, label = 'Mean+4*sd')
    plt.axhline(y = mean, color='orange', linestyle='--', linewidth=2, label = 'Mean')
    plt.title(sig_name)
    plt.xlabel('Time')
    plt.ylabel(sig_name)
    plt.legend()
    plt.annotate('Tamaño de ventana: '+ str(break_size) + '\nMean+4*sd: '+ str(round(high,4)) + '\nPalabra: 1 bit', (0,0), (0,-30), fontsize=8, 
                xycoords='axes fraction', textcoords='offset points', va='top')


