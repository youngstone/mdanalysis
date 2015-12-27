# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
#
# MDAnalysis --- http://www.MDAnalysis.org
# Copyright (c) 2006-2015 Naveen Michaud-Agrawal, Elizabeth J. Denning, Oliver Beckstein
# and contributors (see AUTHORS for the full list)
#
# Released under the GNU Public Licence, v2 or any higher version
#
# Please cite your use of MDAnalysis in published work:
# N. Michaud-Agrawal, E. J. Denning, T. B. Woolf, and O. Beckstein.
# MDAnalysis: A Toolkit for the Analysis of Molecular Dynamics Simulations.
# J. Comput. Chem. 32 (2011), 2319--2327, doi:10.1002/jcc.21787
#
from numpy.testing import (
    assert_,
)
import MDAnalysis as mda

from MDAnalysisTests.topology.base import ParserBase
from MDAnalysisTests.datafiles import (
    PDB,
    PDB_small,
)


class TestPDBParser(ParserBase):
    """This one has neither chainids or segids"""
    parser = mda.topology.PrimitivePDBParser.PrimitivePDBParser
    filename = PDB
    expected_attrs = ['ids', 'names',
                      'resids', 'resnames']
    expected_n_atoms = 47681
    expected_n_residues = 11302
    expected_n_segments = 1


class TestPDBParserSegids(ParserBase):
    """Has segids"""
    parser = mda.topology.PrimitivePDBParser.PrimitivePDBParser
    filename = PDB_small
    expected_attrs = ['ids', 'names',
                      'resids', 'resnames', 'segids']
    expected_n_atoms = 3341
    expected_n_residues = 214
    expected_n_segments = 1