"""Own-topic adaptation of search_lab.ipynb cells 5, 9, 13, 19, 34 and 45.

The course section 14 searches titles plus OpenAlex abstracts, not full PDFs.
BM25 uses its formula; neural retrieval uses its documented MiniLM fallback.
"""
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import re
import sys
import time

import numpy as np
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
MODEL = "sentence-transformers/all-MiniLM-L6-v2"
QUERIES = [
 "How does NCM construct hierarchical residual codes and condition each level?",
 "How can masked diffusion generate discrete codes jointly with a frozen tokenizer?",
 "Which remasking samplers can revise already generated diffusion tokens?",
 "How do semantic vocabulary clusters differ from learned latent hierarchies?",
 "How should MAUVE and diversity evaluate generated text beyond perplexity?",
]
STOP = set("a an and are as at be by for from has have in is it its of on or that the this to was were which with we our can".split())


def tokenize(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP and len(w) > 1]


def restore_abstract(inverted):
    return " ".join(w for _, w in sorted((p, w) for w, positions in (inverted or {}).items() for p in positions)[:400])


def fetch(topic):
    r = requests.get("https://api.openalex.org/works", params={"search":topic,"per_page":15,"filter":"has_abstract:true","select":"id,doi,display_name,publication_year,abstract_inverted_index"}, timeout=30)
    r.raise_for_status()
    return {"query":topic,"request":r.url,"retrieved":datetime.now(timezone.utc).isoformat(),"response":r.json()}


def main():
    started=time.monotonic()
    out=ROOT/'library/retrieval';out.mkdir(parents=True,exist_ok=True)
    cache=out/'openalex-responses.json'
    responses=json.loads(cache.read_text(encoding='utf-8')) if cache.exists() else list(ThreadPoolExecutor(4).map(fetch,["diffusion language models","remasking diffusion language models","latent diffusion text generation","MAUVE text generation evaluation"]))
    (out/'openalex-responses.json').write_text(json.dumps(responses,ensure_ascii=True,indent=2),encoding='utf-8')
    docs=[];seen=set()
    # Interleave queries so generic DLM search does not consume the entire library.
    for rank in range(15):
        for response in responses:
            works=response['response']['results']
            if rank>=len(works):continue
            w=works[rank];title=w['display_name'] or '';key=re.sub(r'\W+','',title.lower())
            abstract=restore_abstract(w.get('abstract_inverted_index'))
            if key in seen or len(abstract.split())<45 or re.search(r'[\u0400-\u04ff]',title+abstract):continue
            if re.search(r'audio|speech|music|video|image|assembly',title,re.I):continue
            seen.add(key)
            docs.append({'id':w['id'].rsplit('/',1)[-1],'title':title,'year':w['publication_year'],'doi':w['doi'],'abstract':abstract,'text':title+'. '+abstract,'source_url':w['id'],'retrieved':response['retrieved'],'search_query':response['query'],'scope':'title_and_abstract'})
            if len(docs)>=24:break
        if len(docs)>=24:break
    catalog=json.loads((ROOT/'library/catalog.json').read_text(encoding='utf-8'))
    for paper in catalog['documents']:
        page=PdfReader(ROOT/paper['pdf_path']).pages[0].extract_text() or ''
        abstract=page.split('Abstract',1)[-1]
        abstract=abstract.split('\n1 Introduction')[0]
        if paper['arxiv_id']=='2610.14162':abstract=abstract.split('\n4 8 16')[0]
        abstract=' '.join(abstract.split()[:220])
        docs.append({'id':paper['arxiv_id'],'title':paper['title'],'year':int('20'+paper['arxiv_id'][:2]),'doi':None,'abstract':abstract,'text':paper['title']+'. '+abstract,'source_url':paper['source_url'],'retrieved':'2026-10-21','scope':'title_and_pdf_abstract','pdf_path':paper['pdf_path']})
    assert len(docs)>=20
    (out/'corpus.jsonl').write_text(''.join(json.dumps(d,ensure_ascii=True)+'\n' for d in docs),encoding='utf-8')
    index=defaultdict(dict);lengths=[]
    for i,d in enumerate(docs):
        tokens=tokenize(d['text']);lengths.append(len(tokens))
        for w,tf in Counter(tokens).items():index[w][i]=tf
    avg=sum(lengths)/len(lengths);n=len(docs)
    def bm25(query,k1=1.2,b=.75):
        scores=np.zeros(n)
        for w in tokenize(query):
            postings=index.get(w,{})
            weight=math.log(1+(n-len(postings)+.5)/(len(postings)+.5))
            for i,tf in postings.items():scores[i]+=weight*tf*(k1+1)/(tf+k1*(1-b+b*lengths[i]/avg))
        return scores
    os.environ['TOKENIZERS_PARALLELISM']='false'
    import torch
    torch.set_num_threads(4)
    from sentence_transformers import SentenceTransformer
    encoder=SentenceTransformer(MODEL,revision='1110a243fdf4706b3f48f1d95db1a4f5529b4d41',device='cpu')
    vectors=encoder.encode([d['text'] for d in docs],normalize_embeddings=True,show_progress_bar=False,batch_size=8)
    qvectors=encoder.encode(QUERIES,normalize_embeddings=True,show_progress_bar=False,batch_size=5)
    np.save(out/'document_vectors.npy',vectors);np.save(out/'query_vectors.npy',qvectors)
    results=[]
    for qi,q in enumerate(QUERIES):
        scores={'bm25':bm25(q),'vector':vectors@qvectors[qi]};row={'query':q,'rankings':{}}
        for method,s in scores.items():
            row['rankings'][method]=[{'rank':r+1,'id':docs[int(i)]['id'],'title':docs[int(i)]['title'],'score':float(s[i]),'abstract':docs[int(i)]['abstract']} for r,i in enumerate(np.argsort(-s)[:5])]
        results.append(row)
    metadata={'source_notebook':'search_lab.ipynb','adapted_cells':[5,9,13,19,34,45],'corpus_scope':'titles and abstracts, matching course section 14','documents':n,'queries':5,'bm25':{'k1':1.2,'b':.75},'encoder':MODEL,'model_revision':getattr(encoder[0].auto_model.config,'_commit_hash',None),'device':'cpu','normalized_embeddings':True,'dimension':int(vectors.shape[1]),'max_seq_length':encoder.max_seq_length,'versions':{'torch':torch.__version__},'elapsed_seconds':time.monotonic()-started,'corpus_sha256':sha256((out/'corpus.jsonl').read_bytes()).hexdigest(),'results':results}
    (out/'search-results.json').write_text(json.dumps(metadata,ensure_ascii=True,indent=2),encoding='utf-8')
    print(json.dumps({'documents':n,'queries':5,'encoder':MODEL,'elapsed_seconds':metadata['elapsed_seconds']},indent=2))


if __name__=='__main__':main()
