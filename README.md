

<!-- ABOUT THE PROJECT -->
# Projetos de Processamento de imagens

Implementação em Python, utilizando a biblioteca Numpy, de filtros ou máscaras, e operações pontuais de processamento de imagens, para o uso em imagens no formato `.ppm` ou `.pbm`.

<!-- GETTING STARTED -->
## Funcionamento

### Pré-requisitos

A versão do interpretador `Python` utilizada no desenvolvimento foi a `3.6`, por isso para o funcionamento adequado é necessária uma distribuição acima desta versão, que pode ser gerenciada em ambientes virtuais como o `Anaconda`.

* Python>=3.6
* PIP

Em sistemas linux utilize os comandos no terminal:
```sh
sudo apt install python3
sudo apt install python3-pip
```

Para executar o software corretamente, você precisará de algumas dependências que podem ser gerenciadas pelo gerenciador de pacotes do Python `PIP`, use o comando no terminal:

```sh
pip install numpy matplotlib tqdm
```

<!-- USAGE EXAMPLES -->
### Uso
Para o uso adequado do programa identifique o formato P1 ou P2, e modifique a main com o nome do arquivo contendo a imagem:
```sh
python op.py
python mask.py
python pbm.py
```
