""" geneblocks/__init__.py """

# __all__ = []

from .CommonBlocks import CommonBlocks
from .DiffBlocks import DiffBlocks, DiffRecordTranslator
from .biotools import load_record,random_dna_sequence, reverse_complement

from .version import __version__
