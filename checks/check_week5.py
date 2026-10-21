"""Check saved retrieval evidence and SPARQL provenance without rerunning the network."""
from pathlib import Path
from hashlib import sha256
import json
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]


def main():
    base=ROOT/'library/retrieval'
    docs=[json.loads(x) for x in (base/'corpus.jsonl').read_text(encoding='utf-8').splitlines()]
    result=json.loads((base/'search-results.json').read_text(encoding='utf-8'))
    assert len(docs)>=20 and len({d['id'] for d in docs})==len(docs)
    assert result['corpus_sha256']==sha256((base/'corpus.jsonl').read_bytes()).hexdigest()
    assert len(result['results'])>=5
    ids={d['id'] for d in docs}
    for row in result['results']:
        for method in ('bm25','vector'):
            assert len(row['rankings'][method])>=3
            assert all(x['id'] in ids and np.isfinite(x['score']) for x in row['rankings'][method])
    vectors=np.load(base/'document_vectors.npy');qvectors=np.load(base/'query_vectors.npy')
    assert vectors.shape[0]==len(docs) and qvectors.shape[0]==5
    assert np.allclose(np.linalg.norm(vectors,axis=1),1,atol=1e-4)
    provenance=json.loads((base/'sparql-provenance.json').read_text(encoding='utf-8'))
    response=json.loads((base/'sparql-response.json').read_text(encoding='utf-8'))
    assert provenance['status_code']==200 and response['results']['bindings']
    assert (ROOT/'notes/query-machine-learning-types.md').is_file()
    print(f'PASS: {len(docs)} corpus documents, 5 BM25/vector queries, normalized vectors, nonempty executed SPARQL and provenance.')
    print('Abstract-corpus retrieval evidence; no full-text review or statistical relevance benchmark is inferred.')
    return 0


if __name__=='__main__':sys.exit(main())
