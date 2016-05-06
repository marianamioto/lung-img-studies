# quali
Este repositório foi criado para organizar arquivos referentes ao projeto de mestrado.

Resumo
A Fibrose Pulmonar Idiopática (FPI), umas das possíveis doenças pulmonares parenquimatosas difusas, tem um prognóstico de deterioração da função pulmonar e é responsável por cerca de 50% dos casos que são encaminhados para o transplante de pulmão. A FPI está, na maioria das vezes, associada com um padrão histológico e radiológico de Pneumonia Intersticial Usual (PIU) e o padrão radiológico pode ser observado em exames radiográficos, mais especificamente, em Tomografias Computadorizadas de Alta Resolução (TCAR). Nesse contexto, considerando a complexidade da tomada de decisão diagnóstica dos radiologistas, devido à grande quantidade de imagens geradas em um exame de TCAR, propomos um estudo que investigue algoritmos que possam caracterizar de forma quantitativa os achados radiológicos, possibilitando o reconhecimento computadorizado de padrões nos exames de TCAR. Iremos utilizar processamento de imagens aplicados às imagens TCAR de tórax para caracterizar os padrões que compõem o quadro tomográfico de PIU. Em uma primeira fase do estudo, foi necessário buscar bases de imagens e configura-las para que o processamento fosse realizado. Após a aquisição e reorganização dos exames das bases, foram realizados experimentos que contemplam a etapa de pré-processamento, onde o método de Otsu e o método Adaptativo foram implementados a fim de estabelecer a binarização das imagens para posteriormente implementar e aplicar o método Marching Squares para a detecção das bordas da área do pulmão. Os resultados mostram que devemos realizar estudos quanto à janela de contraste utilizada durante o pré-processamento, para maximizar a extração de textura. O pré-processamento resultou em uma segmentação confiável (segundo a medida de Região não uniforme), porém com inconsistências que deverão ser tratadas nas próximas etapas do estudo.

Palavras-chave: Doenças Pulmonares Intersticiais, Pneumonia Intersticial Usual, Tomografia de Alta Resolução, Segmentação, Região Não Uniforme.


O arquivo "requirements.txt" é um arquivo que contém uma lista de itens a serem instalados usando pip install da seguinte forma:

  pip install -r requirements.txt
  
  
  Fonte: https://pip.pypa.io/en/stable/user_guide/#requirements-files
  
