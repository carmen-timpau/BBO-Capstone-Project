**BBO Week 13 - Bayesian Optimisation Strategy Summary**

To predict the next queries for Week 13 (final week) of the BBO project, a Highly-Exploitative variation of the **BBO Week 11 - Bayesian Optimisation Pipeline** was deployed on Week 13 input data, as the core of the Week 11's pipeline is very robust and has been fully automated and optimised to generate the highest quality queries possible at this advanced stage of the project. 

The **BBO Week 13 - Bayesian Optimisation Pipeline** only differs from the **BBO Week 11 - Bayesian Optimisation Pipeline** in terms of the _acquisition functions that are being considered for the Full Joint Kernel x Acquisition Rollout Ablation_. For **Week 13**, a very limited list of **only 3 highly-exploitative acquisition functions** were employed, to leverage the most promising areas identified so far through both exploration and exploitation during the course of the previous 12 weeks of the BBO project.

The specific details of the core structure of the BO pipeline deployed in Week 13 can be accessed at `experiments/week_11/strategy_summary.md` within this repository.

**<ins>Note:</ins>** The BBO Week 11 Full ML Bayesian Optimisation Pipeline is computationally heavy. Runtime to completion is expected to be around ~2.5h if 16 CPU cores are available (as used here), but it may take slightly/significantly longer if not.

**Running the Script:** As implemented in Week 10, all prints are streamed to a log file (`execution_output.log`) instead of the browser console, to avoid progress loss mid-run due to browser crashing, as the pipeline is computationally and resource intensive.

**Checking Obtained Results:** All results obtained for BBO Week 13 can be found in the `experiments/week_13/diagnostics_results/` subfolder within this repository.

