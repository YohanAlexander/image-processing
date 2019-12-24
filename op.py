import tqdm
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

class Image():
    def __init__(self, x, y, header, comment, pixel):
        self.x = x
        self.y = y
        self.pixel = int(pixel)
        self.header = header
        self.comment = comment
        self.image = np.ones(shape=(int(x), int(y)), dtype=int)

class Masc():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.a = int((m - 1) / 2)
        self.b = int((n - 1) / 2)
        self.masc = np.ones(shape=(m, n))

def read_ppm(file):

    with open(f'{file}', 'r') as ppmfile:

        header = ppmfile.readline().strip()

        comment = ppmfile.readline().strip()

        x, y = ppmfile.readline().split()

        if(header == "P1"):
            image = Image(x, y, header, comment, 1)
        else:
            pixel = ppmfile.readline().strip()
            image = Image(x, y, header, comment, pixel)

        for line in tqdm.trange(int(x), desc='Lendo imagem'):
            for columm in range(int(y)):
                char = ppmfile.readline()
                if(char == '\n'):
                    char = ppmfile.readline()
                    image.image[line, columm] = int(char)
                else:
                    image.image[line, columm] = int(char)

    return image

def write_ppm(img, file):

    aux = 0

    x, y = img.image.shape

    with open(f'{file}', 'w') as ppmfile:

        ppmfile.write(f"{img.header}\n")

        ppmfile.write(f"{img.comment}\n")

        ppmfile.write(f"{x} {y}\n")

        if(img.header != "P1"):
            ppmfile.write(f"{img.pixel}\n")

        for line in tqdm.trange(int(x), desc='Escrevendo imagem'):
            for columm in range(int(y)):
                aux += 1
                if(aux == 70):
                    ppmfile.write(str(img.image[line, columm]) + "\n")
                    aux = 0
                else:
                    ppmfile.write(str(img.image[line, columm]) + " ")

def negativo(img, file):

    neg = Image(img.x, img.y, img.header, img.comment, img.pixel)

    neg.image = img.pixel - img.image

    write_ppm(neg, file)

def limiarizar(img, file, limiar):

    lim = Image(img.x, img.y, img.header, img.comment, img.pixel)

    #lim.image = img.pixel - img.image + limiar

    for i in range(img.pixel):
        for j in range(img.pixel):
            if(img.image[i][j] > limiar):
                lim.image[i][j] = 255;
            else:
                lim.image[i][j] = 0;

    write_ppm(lim, file)

def histograma(img):

    x, y = img.image.shape

    lim = np.ones(shape=(img.pixel + 1,), dtype=int)

    for i in range(x):
        for j in range(y):
            lim[img.image[i][j]] += 1;

    norm = lim / img.image.size

    plt.bar(range(img.pixel + 1), norm * img.pixel)
    plt.savefig("Resultados/hist.png")
    plt.close()

    return lim

def equalizar(img, file):

    x, y = img.image.shape

    hist = histograma(img)

    norm = hist / img.image.size

    cum = np.cumsum(norm)

    eq = np.round(cum * img.pixel)

    plt.bar(range(img.pixel + 1), eq)
    plt.savefig("Resultados/eq.png")
    plt.close()

    imgeq = Image(img.x, img.y, img.header, img.comment, img.pixel)

    for i in range(x):
        for j in range(y):
            imgeq.image[i][j] = eq[img.image[i][j]]

    write_ppm(imgeq, file)

if __name__ == "__main__":

    out = read_ppm('Figuras/ImagemEscura.pgm')
    write_ppm(out, "Resultados/file")
    negativo(out, "Resultados/neg")
    limiarizar(out, "Resultados/lim", 50)
    histograma(out)
    equalizar(out, "Resultados/eq")
