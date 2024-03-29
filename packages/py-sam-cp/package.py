# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PySamCp(PythonPackage):
    """sam_cp replacement"""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/sam-cp"
    url = (
        "https://cdcvs.fnal.gov/cgi-bin/git_archive.cgi/cvs/projects/sam-cp.v9_0_8.tar"
    )

    version(
        "9_0_8",
        sha256="e50e69b97afa3fc4dbc785c08e6aacc9cf44357155c6b2272778ddebfdc4e269",
    )
