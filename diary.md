# Research diary

## 2026-10-21 - initial environment (translated historical entry)

[written] The user requested a separate repository, concise AGENTS.md, append-only
diary.md, rewritten STATUS.md and commits explaining why. Forced ReAct was unwanted.
[source] Original context: chat 6ad55e65-b228-83eb-982c-13f434b90801; NCM context:
chat 6ad62397-44dc-83eb-9770-39f494b040c6. Two additional papers were requested.
[generated] A separate environment was created without moving private code. W2-W5
slides were read; W3 p.71, W4 p.84 and W5 pp.87-88 were visually checked. W1 slides
were absent from both the local directory and ZIP.

## 2026-10-21 - bootstrap verification (translated historical entry)

[source] Initial structure check: exit 0, 87 links and three PDF hashes. PDF lengths:
NCM 40 pages, HDLM 29 pages, H-CDLM 27 pages. A false positive on an inline-code
wiki-link example was fixed. Missing-target and altered-PDF controls failed as expected.
A one-off PyYAML review found 8 classes and 16 typed objects with consistent links.
[generated] Bootstrap was marked done, without inventing user acceptance. The full
homework was not declared complete. External NCM working trees were not modified.

## 2026-10-21 - research-first scope and language migration

[written] The user clarified that the project must conduct research, with acceptance,
verifiers and work modes for paper review, summarization and literature search.
All maintained project files must be English, regardless of chat language.
[source] Both requested chats and Notion page N1 were read. N1 is unverified source
notes. Key proposals and their attribution were distilled into research-context.md.
[generated] The working-tree diary was translated once to satisfy the explicit
language instruction; the initial commit preserves the original wording. Future
entries remain append-only. Model implementation here has not started. Existing
external experiments are acknowledged as separate historical work.

## 2026-10-21 - source review, memory and weeks 1-3 evidence

[source] Read the NCM main paper (PDF pp.2-13) with focused evidence review on pp.6-9;
read HDLM hierarchy/transition/training pages and H-CDLM method/evaluation pages.
Six method/evaluation pages were rendered for direct inspection. Three original PDFs
retain their catalog hashes. NCM L1 covers main sections, L2 has eight claims, L3 is
one sentence, and six claims have source-page judgments and machine-locatable anchors.
[generated] Distinguish model factorization from real-data independence; qualify
Table 1 reconstruction by dataset; do not equate unigram entropy with corpus diversity.
These corrections refine the research premises without asserting an experimental gain.
[source] Structure and evidence checks returned 0. On an isolated copy, directing C7
to a wrong source page returned 1. Four offline driver scenarios passed expected
accept/reject/protection/repeat checks; the policy was explicitly a deterministic fixture.
[generated] Confirmed week-1 summary scope and week-2/3 artifact criteria are recorded;
the absent week-1 presentation and unexecuted live notebook exercises remain disclosed.
Paper-review tasks are done, not user-accepted. Next: research design and targeted search.
