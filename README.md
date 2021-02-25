# FLARE
[![DOI](https://zenodo.org/badge/340846727.svg)](https://doi.org/10.5281/zenodo.4562274)

FLARE is an astrophysical code written in Python to generate a synthetic catalog of 100,000 Fast Radio Bursts (FRBs). It uses the Monte Carlo statistical technique to generate a synthetic FRB catalog. It also analyses the resulting catalog and makes its histograms.

FLARE runs FRB generation scripts in parallel, which makes the code very fast.
## Installation 
To install FLARE on a computer, run the following commands in your terminal:
```bash
> mkdir FLARE
> cd FLARE
> git clone https://github.com/Kushaalkumar-pothula/FLARE.git
> cd FLARE
```
Now you should have the FLARE code successfully installed on your machine.

## Usage
To generate a synthetic FRB catalog using FLARE, you will need to run ```gen.sh```, which can be done by running the following commands in terminal:
```bash
> chmod +x gen.sh
> ./gen.sh
```
You will now find some ```.txt``` files, which have the local date-time (during the catalog generation) as a prefix. Each of these ```.txt``` files contain a specific property of a mock FRB.
These results are analyzed in a single run of FLARE, and they are saved as ```.png``` files.

## User Guide
Going through the FLARE user guide (https://github.com/Kushaalkumar-pothula/FLARE/wiki) is *highly* recommended. It includes important articles about FLARE, which are helpful for learning to use FLARE.

## Author
[Kushaal Kumar Pothula](https://sites.google.com/view/kushaal-kumar-pothula/)

## Citing FLARE
If you use FLARE in your research, please cite FLARE by adding this BibTeX entry to your bibliography:
```
@software{kushaal_kumar_pothula_2021_4562275,
  author       = {Kushaal Kumar Pothula},
  title        = {The FLARE Code},
  month        = feb,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v1.0.1},
  doi          = {10.5281/zenodo.4562274},
  url          = {https://doi.org/10.5281/zenodo.4562274}
}
```
