"""Local closed-world graph checks; not the unavailable course check_week4.py."""
from pathlib import Path
import re
import sys
import yaml

ROOT=Path(__file__).resolve().parents[1]


def main():
    schema=yaml.safe_load((ROOT/'ontology.yaml').read_text(encoding='utf-8'))
    objects={};errors=[]
    for folder in ('notes','tasks','reports'):
        for p in (ROOT/folder).glob('*.md'):
            text=p.read_text(encoding='utf-8');m=re.match(r'^---\n(.*?)\n---\n',text,re.S)
            if not m:continue
            meta=yaml.safe_load(m.group(1));kind=meta.get('type')
            if kind not in schema['classes']:errors.append(f'{p.name}: unknown type {kind}')
            edges=re.findall(r'^- ([^:\n]+): \[\[([^\]\n]+)\]\]$',text,re.M)
            objects[p.relative_to(ROOT).with_suffix('').as_posix()]={'meta':meta,'edges':edges}
    for key,obj in objects.items():
        kind=obj['meta']['type']
        if ('type','ontology/'+kind) not in obj['edges']:errors.append(f'{key}: missing class link')
        for rel,target in obj['edges']:
            spec=schema['relations'].get(rel)
            if not spec or kind not in spec['domain']:
                errors.append(f'{key}: invalid relation/domain {rel}');continue
            if rel=='type':
                if not (ROOT/(target+'.md')).is_file():errors.append(f'{key}: class missing')
            elif spec.get('range')==['File']:
                if not (ROOT/target).is_file():errors.append(f'{key}: missing file {target}')
            elif target not in objects or objects[target]['meta']['type'] not in spec['range']:
                errors.append(f'{key}: range mismatch {rel} -> {target}')
        if kind=='Source':
            if not obj['meta'].get('source_url') or not obj['meta'].get('accessed'):errors.append(f'{key}: missing provenance')
            if not any(r=='storedIn' for r,_ in obj['edges']):errors.append(f'{key}: missing stored source')
        if kind=='Task':
            status=obj['meta'].get('status')
            if status not in schema['attributes']['status']['values']:errors.append(f'{key}: invalid status')
            if status in ('done','accepted'):
                report=any(x['meta']['type']=='Report' and ('completes',key) in x['edges'] for x in objects.values())
                children=[x for x in objects.values() if ('subtaskOf',key) in x['edges']]
                if not report and not (children and all(x['meta'].get('status') in ('done','accepted') for x in children)):errors.append(f'{key}: done without outcome')
            if status=='accepted' and not obj['meta'].get('acceptance_evidence'):errors.append(f'{key}: acceptance without user evidence')
    if len(schema['classes'])<3 or len(schema['rules'])<2 or len(objects)<10:errors.append('Course minimum graph size not reached')
    if errors:
        print('\n'.join('FAIL: '+e for e in errors));return 1
    print(f'PASS: {len(schema["classes"])} classes, {len(schema["rules"])} rules, {len(objects)} typed objects; types, relations, provenance and task outcomes consistent.')
    print('No global OWL reasoning or user acceptance is inferred.')
    return 0


if __name__=='__main__':sys.exit(main())
