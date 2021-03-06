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

from numpy.testing import assert_, assert_warns

from MDAnalysisTests.datafiles import (
    PDB_conect2TER,
    PDB_singleconect,
)

import MDAnalysis as mda
from MDAnalysis.topology.PDBParser import PDBParser

def test_conect2ter():
    def parse():
        with PDBParser(PDB_conect2TER) as p:
            struc = p.parse()
        return struc
    assert_warns(UserWarning, parse)
    struc = parse()

    assert_('bonds' in struc)
    assert_(len(struc['bonds']) == 4)


def test_single_conect():
    def parse():
        with PDBParser(PDB_singleconect) as p:
            struc = p.parse()
        return struc
    assert_warns(UserWarning, parse)
    struc = parse()
    assert_('bonds' in struc)
    assert_(len(struc['bonds']) == 2)

