#!/usr/bin/env python3
#   trex2champ is a tool which allows to read output files of quantum
#   chemistry codes (GAMESS and trexio files) and write input files for
#   CHAMP in V3.0 format.
#
# Copyright (c) 2021, TREX Center of Excellence
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#   Ravindra Shinde
#   University of Twente
#   Enschede, The Netherlands
#   r.l.shinde@utwente.nl


import unittest
import sys
import os
import numpy as np
from collections import Counter
import argparse

try:
    import trexio
except:
    print("Error: The TREXIO Python library is not installed")
    sys.exit(1)

try:
    import resultsFile
except:
    print("Error: The resultsFile Python library is not installed")
    sys.exit(1)

from .trex2champ import Champ

class TestChamp(unittest.TestCase):

    def setUp(self):
        self.champ = Champ()

    def test_benzene_ground_state(self):
        self.champ.filename="benzene.hdf5"
        self.champ.motype="RHF"
        self.champ.back_end='hdf5'
        self.champ.gamessfile=None
        self.champ.save_geometry=True
        self.champ.save_lcao = True
        self.champ.save_basis = True
        self.champ.save_eigenvalues = False
        self.champ.save_ecp = True
        self.champ.save_symmetry = False
        self.champ.save_determinants = False
        self.champ.save_csfs = False
        self.champ.basis_prefix = "TEST1"

        self.champ.run()
        self.assertIsNotNone(self.champ)
        self.assertEqual(self.champ.nucleus_num, 12)
        self.assertEqual(self.champ.ao_num, 114)
        self.assertEqual(self.champ.mo_num, 108)
        self.assertEqual(self.champ.shell_num, 48)
        self.assertEqual(self.champ.prim_num, 186)
        self.assertEqual(self.champ.ecp_num, 42)

    def test_formaldehyde_ground_state(self):
        self.champ.filename="COH2_GS.trexio"
        self.champ.motype="RHF"
        self.champ.back_end='HDF5'
        self.champ.gamessfile=None
        self.champ.save_geometry=True
        self.champ.save_lcao = True
        self.champ.save_basis = True
        self.champ.save_eigenvalues = False
        self.champ.save_ecp = True
        self.champ.save_symmetry = False
        self.champ.save_determinants = True
        self.champ.save_csfs = False
        self.champ.basis_prefix = "TEST2"

        self.champ.run()
        self.assertIsNotNone(self.champ)
        self.assertEqual(self.champ.nucleus_num, 4)
        self.assertEqual(self.champ.ao_num, 66)
        self.assertEqual(self.champ.mo_num, 66)
        self.assertEqual(self.champ.shell_num, 26)
        self.assertEqual(self.champ.prim_num, 62)
        self.assertEqual(self.champ.ecp_num, 14)
        self.assertEqual(self.champ.num_dets, 1862)
        self.assertEqual(self.champ.num_states, 1)

    def test_butadiene(self):
        self.champ.filename="butadiene_ci44_pVDZ.hdf5"
        self.champ.motype="GUGA"
        self.champ.back_end='HDF5'
        self.champ.gamessfile=None
        self.champ.save_geometry=True
        self.champ.save_lcao = True
        self.champ.save_basis = True
        self.champ.save_eigenvalues = False
        self.champ.save_ecp = True
        self.champ.save_symmetry = False
        self.champ.save_determinants = True
        self.champ.save_csfs = False
        self.champ.basis_prefix = "TEST3"

        self.champ.run()
        self.assertIsNotNone(self.champ)
        self.assertEqual(self.champ.nucleus_num, 10)
        self.assertEqual(self.champ.ao_num, 86)
        self.assertEqual(self.champ.mo_num, 86)
        self.assertEqual(self.champ.shell_num, 38)
        self.assertEqual(self.champ.prim_num, 114)
        self.assertEqual(self.champ.ecp_num, 34)

if __name__ == '__main__':
    unittest.main()
