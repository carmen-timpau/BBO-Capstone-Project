**BBO Week 12 - Bayesian Optimisation Strategy Summary**

To predict the next queries for Week 12 (penultimate week) of the BBO project, the **BBO Week 11 - Bayesian Optimisation Pipeline** was deployed on Week 12 input data, as it is very robust and has been fully automated and optimised to generate the highest quality queries possible at this advanced stage of the project.

The specific details of this BO pipeline's structure can be accessed at `experiments/week_11/strategy_summary.md` within this repository.

**<ins>Note:</ins>** The BBO Week 11 Full ML Bayesian Optimisation Pipeline is computationally heavy. Runtime to completion is expected to be around ~2.5h if 16 CPU cores are available (as used here), but it may take slightly/significantly longer if not.

**Running the Script:** As implemented in Week 10, all prints are streamed to a log file (`execution_output.log`) instead of the browser console, to avoid progress loss mid-run due to browser crashing, as the pipeline is computationally and resource intensive.

**Checking Obtained Results:** All results obtained for BBO Week 12 can be found in the `experiments/week_12/diagnostics_results/` subfolder within this repository.
