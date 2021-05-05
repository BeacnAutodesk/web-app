# web-app

## Description
This is a simple Flask Web App intended to mockup how an LCA application could look for the client. In its current state, there are key examples intended to display what fields are necessary for a gate-to-gate LCA (namely the materials, mass, density, etc.). 

[Exiobase Data Referenced](https://www.exiobase.eu/index.php/data-download/exiobase3hyb)

### Key Files and Folders
- `analysis_script.py`, this is where the inputs are received, and gate-to-gate LCA calculations are conducted baased on pre-configured datapoints.
- `forms.py`, this file uses WTForms to create the forms which users interact with, including registration, login, and LCA Analysis.
- `main.py`, this file holds the actual Flask implementation for each page, respectively.
- `templates`, this folder contains all of the html scripts to render the Web Application.

## Requirements/Libraries
- `flask`
- `forms`
- `flask_wtf`
- `wtforms`

## Directions
To run the Flask Web Application on a local machine, run `python3 main.py`.



