# IC-UFPA
pra registrar os testes da IC

- Atualmente trabalhando em análise do holospectrum do grupo de autistas e grupo de controle

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

______________________________________________________________________________________________________________________

- Problemas encontrados:
1. encaixar a função HHT3D no laço for (acredita que esta dando problema por que esta retorna 4 saídas

______________________________________________________________________________________________________________________

- Falta ser feito: 
1. Descobrir quem são o grupo de controle e quem são o grupo autista para fazer a média dos grupos
2. Fazer a média e então a HHT e o holospectrum, ou fazer o HHT de cada sujeito do grupo e então a média e o holospectrum? 
          - definitivamente HHT de cada sujeito e então a média dos holos
