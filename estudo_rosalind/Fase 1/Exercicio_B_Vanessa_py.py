# -*- coding: utf-8 -*-
"""Exercicio_B_Vanessa.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jjtPFbMw6_bQ73JLvhP6HLrtSfemVmWi

##18/04/21
#**Complementing a Strand of DNA**

http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

s = "AAAACCCGGT"

# string vazia que receberá as bases complementares
dna_complementar = ''

# dicionário com a base complementar
troca = {"A": "T",
         "T": "A",
         "G": "C",
         "C": "G"}

# iterar sobre cada base de 's' e adicionar sua base complementar em 'dna_complementar'
for base in s:
  dna_complementar += troca[base]


print(dna_complementar)

# reverso do dna_complementar
dna_complementar_reverso = dna_complementar[::-1]

print(dna_complementar_reverso)

"""#**Computing GC content**"""

# usei a biblioteca Biopython para ler o arquivo tipo FASTA
!pip install biopython

from Bio import SeqIO
from Bio.SeqUtils import GC

# lendo o arquivo
arquivo = SeqIO.parse("/content/rosalind_gc.txt", "fasta")

# para cada sequência, imprimir sua ID e seu conteúdo GC
for item in arquivo:
  print(item.id, GC(item.seq))

# achar o maior GC
maior_gc = 0

for item in arquivo:
  if GC(item.seq) > maior_gc:
    maior_gc = GC(item.seq)
    id = item.id    
    
print(item.id)
print(maior_gc)