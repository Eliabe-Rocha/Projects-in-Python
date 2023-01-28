# Projeto contador de polichinelo com uso de vision computacional #
[![NPM](https://img.shields.io/static/v1?label=author&message=Eliabe%20Rocha&color=red)](https://eliaberocha.netlify.app/)
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Eliabe-Rocha/Multilevel_Regression_ENEM/blob/main/LICENSE)

<h3>Objetivo</h3>
<p>O projeto de contador de polichinelos teve por objetivo treinar habilidade em python e nas bibliotecas de visão computacional <b>openCV</b> e mediapipe, esta última com foco em rastreamento de movimentos.</p>

<h3>Ferramentas</h3>

<p>Para execução do projeto foram utiilizadas: </p>

<li><b>linguagem python versão 3.8.13</b></li>

<li><b>Biblioteca OpenCV versão 4.7.0.68</b></li>

<p><pre>Usada para carregar e identificar os frames do vídeo ou camera usada no projeto. </pre></p>

<li><b>Biblioteca mediapipe versão 0.9.0.1</b></li>

<p><pre>Usada para rastrear os pontos do corpo, ou partes do corpo. Nesse projeto, foram utilizados os os pontos da mãos e  pés.</pre></p>

<h3>Sobre o projeto</h3>
<p>Para exucação do projeto, foi utilizado a webcam do notebook como meio de entrada dos dados. Porém, é importante destacar que a biblioteca openCV permite a carga de vídios  não streaming e imagens.</p>
<p>Após a caputura dos dados, foi utilizada a biblioteca mediapipe para rastrear os pontos do corpo que permitiriam identificar se o usuário estaria ou não realizando o execício e, se sim, quantos.</p>

<p>O google, desenvolvedor do mediapipe, disponibiliza na página da ferramenta um mapa de pontos rastreáveis (landmarks). Como aposta a figura abaixo.</p>

</br>
<a href = "https://google.github.io/mediapipe/solutions/pose.html"><img src = "https://user-images.githubusercontent.com/62529397/215294535-23700fd3-d9f2-4eb7-88cc-c514377649c9.png" width="50%" height="50%" alt = "pose landmarks." align = "center"></a>
</br>
</br>
<p>Para realizar identificação do polichinelo, foram escolhidos os pontos 31 e 32, pés esquerdo e direito, e pontos 19 e 20, mãos esquerda e direita.</p>
<p>Quando o usuário aproxima as mãos(distância das mãos < 150) e afasta os pés(distância dos pés > 150), o programa executa a contagem do exercício, acrescendo + 1 no contador. </p>
<p>Para isso, foi necessário extrair a distancia dos pontos no eixo X e Y através de um cálculo de hipotenusa (biblioteca math).</p>

