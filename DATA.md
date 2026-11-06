# Data fields

Both Parquet files need `Year`, `AIProb`, `cit`, `CD`, and `Novelty`. Figure-specific fields include `first_Female`/`last_Female`, `first_age`/`last_age`, `first_country`/`last_country`, and, for the first-author team figures, `Gender_P`, `Gender_entropy`, and `team_size`. Gender indicators use 0 for male and 1 for female. Country codes must match the ISO2 conversion of the Natural Earth `SOVEREIGNT` field. `AIProb` is required in [0, 1], and percentage conversion is local to figures that label percentages.

The country shapefile requires its `.shx`, `.dbf`, and `.prj` companions in the same directory. Its geometry and field naming must match the supplied Natural Earth dataset. Natural Earth and other third-party inputs retain their own terms.

Prepared tables use study-specific model scores, author identifiers, gender assignments, and novelty/disruption variables. Preserve the associated provenance and variable definitions.

Figure 1 uses percentile bootstrap intervals. The gap band combines the separate female and male interval endpoints and represents an approximate uncertainty band. Other figures retain their stated normal-approximation summaries. Bootstrap resampling uses rows as the sampling unit.
