import math

def luas_persegi_panjang(panjang,lebar):
    return panjang*lebar

def keliling_persegi_panjang(panjang,lebar):
    return 2*panjang + 2*lebar

def luas_lingkaran(r):
    luas = math.pi * r * r
    return luas

def keliling_lingkaran(r):
    return 2*math.pi*r

def luas_segitiga(alas,tinggi):
    return 0.5*alas*tinggi

def keliling_segitiga(alas,tinggi,miring):
    return alas+tinggi+miring