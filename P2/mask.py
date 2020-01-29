import op
import tqdm
import numpy as np

def media(file, m, n):

    img = op.read_ppm(file)

    imgout = op.Image(img.x, img.y, img.header, img.comment, img.pixel)

    i, j = img.image.shape

    masc = op.Masc(m, n)

    masc.masc *= (1/(m * n))

    for x in tqdm.trange(masc.a, i - 1 - masc.a, desc='Media'):
        for y in range(masc.b, j - 1 - masc.b):
            pixel = 0
            for s in range(m):
                for t in range(n):
                    pixel += masc.masc[s][t] * img.image[x + s - masc.a][y + t - masc.b]
            imgout.image[x][y] = pixel

    op.write_ppm(imgout, "Resultados/media")

def mediana(file, m, n):

    img = op.read_ppm(file)

    imgout = op.Image(img.x, img.y, img.header, img.comment, img.pixel)

    i, j = img.image.shape

    masc = op.Masc(m, n)

    for x in tqdm.trange(masc.a, i - 1 - masc.a, desc='Removendo ruido'):
        for y in range(masc.b, j - 1 - masc.b):
            for s in range(m):
                for t in range(n):
                    masc.masc[s][t] = img.image[x + s - masc.a][y + t - masc.b]
            imgout.image[x][y] = np.median(masc.masc)

    op.write_ppm(imgout, "Resultados/mediana")

if __name__ == "__main__":

    media('Figuras/lua.pgm', 13, 13)
    mediana('Figuras/lua.pgm', 13, 13)
