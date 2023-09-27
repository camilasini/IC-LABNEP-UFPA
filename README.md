# IC-UFPA
Registro dos códigos da IC no Laboratório de Neuroprocessamento
- Título do trabalho: Marcador de habilidade visuoespacial baseado em registros de EEG em crianças e adolescentes com transtorno do espectro autista
    - Início: Agosto/2022 - Final: Agosto/2023

__________________________________________________________________________________________________________
- estatística descritiva:
    - 8 grupo experimental
    - 11 grupo controle
    
___________________________________________________________________________________________________________________
- Análise do holospectrum (Hilbert Huang Spectral Analysis) do grupo de autistas e grupo de controle

O código consiste em:
1. Extrair IMFs
2. Calcular Fase, Frequência e Amplitude instantânea das IMFs
3. Com essas variáveis é possível calcular a Transformada de Hilbert Huang 1D
4. Para o holospectrum é preciso fazer um sift de segundo nível, extrair mais IMFs de cada IMF e obter nova fase, freq e amplitude instantanea
5. Com essas novas variáveis, calcular a transformada de Hilbert Huang 3D (potência sobre frequência x frequência modulada)
6. Com as 3 variáveis geradas pela HHT 3D, calcula-se o holospectrum.

______________________________________________________________________________________________________________________

- Já fiz:
1. As funções de hilbert huang 3D e holospectrum
2. laço for para carregar na lista 'data' os valores dos arquivos 
3. Comparação entre fazer a média antes ou depois do holospectrum
4. Função de plot do holospectrum
5. Plot das médias dos canais dos grupos experimental e controle
______________________________________________________________________________________________________________________

- Falta ser feito: 
1. Média dos canais, agrupar de acordo com a área do cérebro (frontal, parietal, etc) dos grupos experimental e controle
