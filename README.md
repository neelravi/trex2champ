
# trex2champ

trex2champ is a tool which allows to read output files of quantum
chemistry codes (GAMESS and trexio files) and write input files for
CHAMP in V3.0 format.

## Installation

You can install  `trex2champ` from PyPI:

    pip install trex2champ

## Usage

You can use trex2champ by running the following command:

```bash
trex2champ \
	--trex 	"filename.trexio" \
	--backend	"HDF5" \
	--basis_prefix  "BFD-aug-cc-pVDZ" \
	--lcao \
	--ecp \
	--sym \
	--geom \
	--basis \
	--det
```

You may also use the `--help` flag to get more information about the available options:

```bash
trex2champ --help
```

## License

trex2champ is distributed under the terms of the MIT license.

## Issues

If you encounter any problems, please report them on the Github issue tracker.

## Author

Dr. Ravindra Shinde
r.l.shinde@utwente.nl



