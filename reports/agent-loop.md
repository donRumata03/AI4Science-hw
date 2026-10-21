# Optional agent-driver practice

[generated] `python checks/agent_loop_demo.py` executes an offline adaptation of
the course notebook's environment/driver ideas on our three-paper catalog.
The deterministic policy is a fixture, not a language model.

Before execution, the criterion is fixed from the complete catalog: the output count
must equal its number of documents. Four scenarios were executed:

| Scenario | Observed result |
|---|---|
| Complete tool observation | Correct count accepted by external criterion |
| Silently truncated observation | Plausible but wrong count rejected |
| Write targeting protected catalog | Blocked before mutation; source unchanged |
| Repeated wait action | Stopped by repeat detection |

The saved trace is [agent-loop-demo.json](agent-loop-demo.json). Source files are
represented in an isolated dictionary and never changed on disk. These checks exercise
the driver and external criterion. They do not estimate a model policy or replace
the original notebook's paid/live-inference exercises, which were not run.
