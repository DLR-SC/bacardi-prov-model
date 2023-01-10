<!--
SPDX-FileCopyrightText: 2023 German Aerospace Center (DLR)

SPDX-License-Identifier: CC0-1.0
-->

<h1 align="center">Welcome to the <code>BACARDI PROV Data Model</code>! 👋</h1>
<p align="center">
  <a href="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Badge: Made with Python"/>
  </a>
  <a href="https://www.w3.org/TR/prov-overview/">
    <img alt="Badge: W3C PROV" src="https://img.shields.io/static/v1?logo=w3c&label=&message=PROV&labelColor=2c2c32&color=007acc&logoColor=007acc?logoWidth=200" target="_blank" />
  </a>
  <a href="https://github.com/dlr-sc/gitlab2prov/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://citation-file-format.github.io/">
    <img alt="Badge: Citation File Format Inside" src="https://img.shields.io/badge/-citable%20software-green" target="_blank" />
  </a>
  <a href="https://zenodo.org/badge/latestdoi/DOI">
    <img alt="Badge: DOI" src="https://zenodo.org/badge/DOI.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/dlr_software">
    <img alt="Twitter: DLR Software" src="https://img.shields.io/twitter/follow/dlr_software.svg?style=social" target="_blank" />
  </a>
</p>


> A reference implementation for the BACARDI PROV Data Model.

---


## ️🏗️ ️Installation

Clone the project and install using `pip` from the project root directory:

```bash
pip install .
```

## ⚡ Getting started

The BACARDI PROV data model has been designed according to [W3C PROV](https://www.w3.org/TR/prov-overview/) specification.
The reference implementation uses the Python library [prov](https://github.com/trungdong/prov).

### Task Model

Currently, only the `task` model is defined and documented in [docs/task.md](docs/task.md).
It specifies how provenance of a task in BACARDI must be recorded according to the W3C PROV standard.
The reference implementation can be found in the [task](bacardi_prov_model/task.py) module.

## 🚀‍ Execute Examples

Once installed, the example scripts can be executed on the command line.
All scripts create a directory `example-output` in the current working directory and generate their content into it.
You can execute the scripts as follows:

```sh
# Generates provenance bundle using the extended task model
task-bundle

# Generates provenance bundle using the simplified task model
simple-task-bundle

# Generates two provenance bundles using the simplified task model
multi-task-bundle
```

## ✨ How to cite

If you use the BACARDI PROV data model in a scientific publication, we would appreciate citing the following paper:

* M. Stoffers, M. Meinel, B. Hofmann and A. Schreiber, "Integrating Provenance-Awareness into the Space Debris Processing System BACARDI," 2022 IEEE Aerospace Conference (AERO), 2022, pp. 1-12, doi: 10.1109/AERO53065.2022.9843783.

Bibtex entry:

```BibTeX
@INPROCEEDINGS{9843783,
  author={Stoffers, Martin and Meinel, Michael and Hofmann, Benjamin and Schreiber, Andreas},
  booktitle={2022 IEEE Aerospace Conference (AERO)}, 
  title={Integrating Provenance-Awareness into the Space Debris Processing System BACARDI}, 
  year={2022},
  volume={},
  number={},
  pages={1-12},
  doi={10.1109/AERO53065.2022.9843783}
}
```

You can also cite specific releases published on Zenodo: [![DOI](https://zenodo.org/badge/DOI.svg)](https://zenodo.org/badge/latestdoi/DOI)

## ✏️ References

**Papers that refer to the `BACARDI PROV Data Model`**:

* Stoffers, Martin and Meinel, Michael and Hofmann, Benjamin and Fiedler, Hauke  (2022) A use case study on provenance-based data assessments for mission critical software systems.   In: 73rd International Astronautical Congress (IAC 2022).  73rd International Astronautical Congress (IAC 2022), 18.-22. Sep. 2022, Paris, France.       (In Press)  


## 📝 License

Please see the file [LICENSE.md](LICENSE.md) for further information about how the content is licensed.
