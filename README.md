# Coal Creek workflow

This represents a workflow for doing all things needed to go from
template xml files to a full run, parameterized by Watershed Workflow
with ATS input files written by ats_input_spec.

This repo comes with the workflow already run, and all images/outputs
already present.  To run it again, run the clean script e.g.:

    . scripts/clean.sh
    
All work is in the main Jupyter notebook at:

    scripts/mesh_CoalCreek_full_workflow.ipynb
    
An environment file for running this is provided in (Watershed
Workflow)[https://github.com/ecoon/watershed-workflow.git].  It also
requires Amanzi and ATS source code repos, and a built Exodus python
wrappers (which you get for free when building Amanzi TPLs).
Additionally, it requires the
(ats_input_spec)[https://github.com/ecoon/ats_input_spec.git] library
which may eventually move into Amanzi source code, but for now lives
in its own repo.
