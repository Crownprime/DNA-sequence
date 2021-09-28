#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
global var
"""

from environs import Env

env = Env()
env.read_env()

sequence_textarea = env('SEQUENCE')
codes = env('CODES')

"""
Primer design protocol is a select, there are it's all options:
Basic         User-specified (Basic)
Advanced      User-specified (Advanced)
QuikChange    QuikChange Site-Directed Mutagenesis Kit by Stratagene
ExSite        ExSite Site-Directed Mutagenesis Kit by Stratagene
GeneTailor    GeneTailor Site-Directed Mutagenesis System by Invitrogen
"""
protocol = 'Basic'

"""
primer type is a radio input, there are it's all options:
complementary     Complementary primers
overlapping       Overlapping primers
"""
primer_type = 'complementary'

"""
Expression system is a select, there are it's all options:
None                      None
Aplysia californica       Aplysia californica
Arabidopsis thaliana      Arabidopsis thaliana
Bos taurus                Bos taurus
Caenorhabditis elegans    Caenorhabditis elegans
Candida albicans          Candida albicans
Canis familiaris          Canis familiaris
Chlamydomonas reinhardtii Chlamydomonas reinhardtii
Danio rerio               Danio rerio
Dictyostelium discoideum  Dictyostelium discoideum
Drosophila melanogaster   Drosophila melanogaster
Equus caballus            Equus caballus
Escherichia coli          Escherichia coli
Felis catus               Felis catus
Gallus gallus             Gallus gallus
Homo sapiens              Homo sapiens
Mus musculus              Mus musculus
Mycoplasma pneumoniae     Mycoplasma pneumoniae
Oryza sativa              Oryza sativa
Oryzias latipes           Oryzias latipes
Ovis aries                Ovis aries
Plasmodium falciparum     Plasmodium falciparum
Pneumocystis carinii      Pneumocystis carinii
Rattus norvegicus         Rattus norvegicus
Saccharomyces cerevisiae  Saccharomyces cerevisiae
Schizosaccharomyces pombe Schizosaccharomyces pombe
Sus scrofa domestica      Sus scrofa domestica
Takifugu rubripes         Takifugu rubripes
Xenopus laevis            Xenopus laevis
Zea mays                  Zea mays
"""
species = 'Escherichia coli'

consts = {
  "sequence_textarea": sequence_textarea,
  "codes": codes,
  "protocol": protocol,
  "primer_type": primer_type,
  "species": species,
  "chopped_DNA_sequence": 'GT',

  # Melting temp (°C)
  "min_Tm": "75",
  "max_Tm": "85",

  # GC content (%)
  "min_GC": "40",
  "max_GC": "60",

  # Length (bp)
  "min_length": "25",
  "max_length": "45",

  # 5' flanking region (bp)
  "min_5p_flank": "11",
  "max_5p_flank": "21",

  # 3' flanking region (bp)
  "min_3p_flank": "11",
  "max_3p_flank": "21",

  # there are two checkboxes, if you want to cancel checked, you should delete it.
  # Primers terminate in G or C.
  "ends_in_GC": 'on',
  # Mutation site at center of primer.
  "mut_at_center": 'on'
}
