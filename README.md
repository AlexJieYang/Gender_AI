# Gender_AI

Figures describing AI probability by publication year, career age, team gender composition, country, and scientific outcomes.

## Environment

Use Python 3.11 or 3.12. Install the declared Python dependencies from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. Select the same environment in JupyterLab. 

## Inputs and outputs

Set `data_dir` and `output_dir` in `config.json`, or use the `PROJECT_DATA_DIR` and `PROJECT_OUTPUT_DIR` environment variables. Relative directories resolve from the repository root. `PROJECT_CONFIG` selects another JSON configuration file. `DATA.md` describes the data fields and units used by the analyses.

Generated figures are stored under `outputs/<notebook>/`; R tables use `outputs/tables/`. Set `PROJECT_OUTPUT_DIR` to choose another output directory. Start notebooks and R scripts with the repository root as the working directory. Output directories are created when needed.

Bootstrap figures default to 10,000 resamples and seed 1. `BOOTSTRAP_RESAMPLES` (minimum 1,000) and `RANDOM_SEED` configure these values. Bootstrap calculations use bounded batches where supported.

## Workflow

1. Set the data directory for the prepared first-author and last-author tables. `AIProb` must be a probability between 0 and 1.
2. Open any of the five figure notebooks from the repository root. Each loads its own data and can be run independently.
3. For `Fig 4 country.ipynb`, use the Natural Earth country layer and its companion files in the data directory.

## Source validation

```bash
python scripts/check_sources.py
```

This command parses Python sources, notebook cell sources, and JSON without executing research code or loading research data. The GitHub workflow performs the same static checks. Notebooks are stored with empty outputs and no execution counts.

## Citation and reuse

Use `CITATION.cff` for the software repository and cite the associated research publication separately. 

The code is licensed under Apache-2.0; see `LICENSE`.
Third-party datasets, external map data, and research publications retain their original rights and terms; the software license does not grant rights to those materials.
