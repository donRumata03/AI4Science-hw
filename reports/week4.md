---
type: Report
---
# Week 4: research graph

[generated] The research graph distinguishes classes from concrete methods, sources,
hypotheses, metrics and tasks. The class hierarchy has Entity as root; local rules
check provenance, completed-task outcomes and relation endpoint types.

## Acceptance evidence
The schema has more than 3 classes and 2 rules; more than 10 objects have explicit
class links. ontology.yaml, ontology/, notes/, tasks/ and .obsidian/ are present.
check_graph.py checks local closed-world consistency and is explicitly a replacement
for the unavailable course checker, not an OWL reasoner.

## Competency questions and current answers
1. Which assumption motivates the study? NCM's factorized current-level conditional;
   see within-level-hypothesis and paper-ncm, with PDF Eq.5 verified in memory/.
2. Which source supports each method? ncm, hdlm and h-cdlm link to separate primary PDFs.
3. Which metrics are planned? MAUVE and diversity have protocol requirements; no
   experimental values are fabricated.
4. Which outcomes exist? The bootstrap, NCM summary and method comparison have reports;
   tasks are done, not human-accepted.
5. Which outside knowledge is connected? The retrieval-enrichment block adds a
   provenance-preserving Wikidata query and links its concept to the research methods.

## Working-block evidence and limitation
The earlier research-source block is commit fd9bd5c. This block extends the schema
and adds a reusable verifier, and is committed separately. The retrieval/enrichment
block follows as another commit. These are real work blocks; they are not falsely
presented as two separately user-accepted sessions. The practice's explicit user
acceptance step remains available for review after delivery.

## Links
- type: [[ontology/Report]]
- completes: [[tasks/develop-graph]]
