import matplotlib.pyplot as plt
import emd
from scipy.io import loadmat
import numpy as np
from scipy import ndimage

sample_rate = 200

config = emd.sift.get_config('mask_sift')
config['max_imfs'] = 7
config['mask_freqs'] = 50/sample_rate
config['mask_amp_mode'] = 'ratio_sig'
config['imf_opts/sd_thresh'] = 0.05
    
from functools import partial
my_mask_sift = partial(emd.sift.mask_sift, **config)

#_______________________________________________________________________
#função para plotar o holospectrum

def holospectrum(fam, fcarrier, sholo):
   fig,ax=plt.subplots(1,1, figsize=(12,6))
   cp = ax.contourf(fcarrier, fam, sholo.T**0.25, cmap = 'jet', shade = 'nearest', levels=np.linspace(np.min(sholo.T)**0.25, np.max(sholo.T)**0.25, 40))
   plt.yscale('log')
   plt.xscale('log')
   plt.ylim(0.5,16)
   plt.xlim(1,32)
   plt.yticks(2**np.arange(5),2**np.arange(5))
   plt.xticks(2**np.arange(6),2**np.arange(6))
   plt.colorbar(cp)
   #cb.set_label(r'$V^{2}$', rotation=0)
   ax.set_title('holospectrum')
   ax.set_xlabel('FM Frequency (Hz)')
   ax.set_ylabel('AM Frequency (Hz)')
   plt.show()
    
   return 

#_________________________________________________________________________
#função para a imf2

def mask_sift_second_layer(IA, masks, config={}):
    imf2 = np.zeros((IA.shape[0], IA.shape[1], config['max_imfs']))
    for ii in range(IA.shape[1]):
        config['mask_freqs'] = masks[ii:]
        tmp = emd.sift.mask_sift(IA[:, ii], **config)
        imf2[:, ii, :tmp.shape[1]] = tmp
    return imf2

#__________________________________________________________________________
#função p calcular o hilbert huang 

def hilbert_huang(data, sample_rate):
     imf = my_mask_sift(data)
     
###2. calculando o conteudo das imfs (fase, freq e amplitude instantaneas)
     IP, IF, IA = emd.spectra.frequency_transform(imf, sample_rate, 'nht')
    
# Define sift parameters for the second level
     masks = np.array([25/2**ii for ii in range(12)])/sample_rate
     config = emd.sift.get_config('mask_sift')
     config['mask_amp_mode'] = 'ratio_sig'
     config['mask_amp'] = 2
     config['max_imfs'] = 5
     config['imf_opts/sd_thresh'] = 0.05
     config['envelope_opts/interp_method'] = 'mono_pchip'

# Sift the first 5 first level IMFs
     imf2 = emd.sift.mask_sift_second_layer(IA, masks, sift_args=config)

##2.2. calculando o conteudo da imf2
     IP2, IF2, IA2 = emd.spectra.frequency_transform(imf2, sample_rate, 'nht')
    
    ###3. definindo os bins de frequencia que serão usados no histograma
     carrier_hist = (1, 100, 128, 'log') # Carrier frequency histogram 
     am_hist = (1e-2, 32, 64, 'log') # AM frequency histogram

###4. 1d, 2d e 3d hilbert huang transform
#(power over carrier frequency)
     fcarrier, spec = emd.spectra.hilberthuang(IF, IA, carrier_hist, sum_imfs=False)

#power over time x carrier frequency)
     fcarrier, hht = emd.spectra.hilberthuang(IF, IA, carrier_hist, sum_time=False)
     shht = ndimage.gaussian_filter(hht, 2)

#time averaged Holospectrum (power over carrier frequency x AM frequency)
     fcarrier, fam, holo = emd.spectra.holospectrum(IF, IF2, IA2, carrier_hist, am_hist)
     sholo = ndimage.gaussian_filter(holo, 1)
        
     return fcarrier, fam, spec, sholo 


