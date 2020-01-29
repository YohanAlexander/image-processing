#! /usr/bin/python
# -*- coding: utf-8 -*-

import tqdm
import numpy as np

class Image():
    def __init__(self, x, y, header, comment, pixel):
        self.x = x
        self.y = y
        self.pixel = int(pixel)
        self.header = header
        self.comment = comment
        self.image = np.ones(shape=(int(x), int(y)), dtype=float)

class Masc():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.a = int((m - 1) / 2)
        self.b = int((n - 1) / 2)
        self.masc = np.ones(shape=(m, n), dtype=float)

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
                char = ppmfile.read(1)
                if(char == '\n'):
                    char = ppmfile.read(1)
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
                    ppmfile.write(str(img.image[line, columm]))

def mediana(path, file, m, n):

    img = read_ppm(path)

    imgout = Image(img.x, img.y, img.header, img.comment, img.pixel)

    i, j = img.image.shape

    masc = Masc(m, n)

    for x in tqdm.trange(masc.a, i - 1 - masc.a, desc='Removendo ruido'):
        for y in range(masc.b, j - 1 - masc.b):
            for s in range(m):
                for t in range(n):
                    masc.masc[s][t] = img.image[x + s - masc.a][y + t - masc.b]
            imgout.image[x][y] = np.median(masc.masc)

    imgout.image = imgout.image.astype(int)

    write_ppm(imgout, file)

    return imgout

def main():

    imgout = mediana("teste.pbm", "suave", 2, 2)

if __name__ == "__main__":
    main()
