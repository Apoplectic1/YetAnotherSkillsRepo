import json, re

DOCS='E:/Projects/AI/Skills/docs/audit-benchmark/'

# rep0 from exp1 (scored result) + rep1-3 from full-rerun raw output (both repo-tracked, reproducible)
e1=json.loads(open(DOCS+'sweeps/exp1-model-compare.json',encoding='utf-8').read())
fr=json.loads(open(DOCS+'raw/exp2-fullrerun-w02p76xdr.output.json',encoding='utf-8').read())
frr=fr['result']
if isinstance(frr,str): frr=json.loads(frr)

# build reps[model][rep] = list of flags
reps={'opus':{}, 'sonnet':{}}
for m in ['opus','sonnet']:
    flags=[]
    for k,fl in e1['byModel'][m]['units'].items(): flags+=fl
    reps[m][0]=flags
for cell,v in frr['byCell'].items():
    m,_,rp=cell.split('/'); rep=int(rp.replace('rep',''))
    if m not in reps: continue
    flags=[]
    for k,fl in v['units'].items(): flags+=fl
    reps[m][rep]=flags

def textof(f): return (f.get('location','')+' || '+f.get('claim','')+' || '+f.get('finding','')+' || '+f.get('evidence','')).lower()

# classifier: ordered signatures -> id. first match wins. each sig = list of required substrings (AND); any of OR-groups via tuples
def classify(f):
    t=textof(f)
    def has(*subs): return all(s in t for s in subs)
    # cross-ref / link issues
    if 'mode-removal' in t: return 'X6'
    if 'screenshot.png' in t: return 'X3'
    if 'code-quality-audit.md' in t and 'roadmap' in t: return 'X2'
    if 'code-quality-audit.md' in t: return 'X5'   # code-comment refs (non-roadmap)
    if 'sky-brightness-day-sky' in t or ('anchor' in t and 'sky-brightness' in t) or ('#sky-brightness' in t): return 'X4'
    if '..\\claude.md' in t or 'parent' in t and 'claude.md' in t and 'auto-load' in t or ('../claude.md' in t): return 'X1'
    if 'parent' in t and 'claude.md' in t: return 'X1'
    # placement
    if 'core consumer contract' in t and ('move' in t or 'reference-grade' in t or 'architecture' in t or 'reference doc' in t or 'router' in t): return 'P2'
    if ('build / run' in t or 'build/run' in t) and ('tool preference' in t or 'stranded' in t or 'orphan' in t or 'empty' in t or 'misplaced' in t): return 'P1'
    # currency - specific
    if 'chartevaluation' in t and ('single-field' in t or 'ensurework' in t or 'renderwork' in t or 'three' in t): return 'C1'
    if 'daywindowkey' in t and 'range' in t and ('no ' in t or 'not ' in t or 'no.range' in t or 'zero' in t or 'does not' in t): return 'C2'
    if 'daywindowkey' in t and ('survives only' in t or 'builddaywindow' in t) and 'range' not in t: return 'C15'
    if 'yeardays' in t and ('location' in t or 'keyed by' in t or 'per-target' in t or 'target only' in t): return 'C3'
    if ('2-4' in t or '2–4' in t or 'pre-pop' in t or '1-2 sec' in t or '1–2 sec' in t) and 'sec' in t: return 'C4'
    if 'ensureasync' in t and ('iprogress' in t or 'third' in t or 'two-arg' in t or 'progress param' in t or '3rd' in t): return 'C5'
    if 'sky' in t and ('diag' in t) and ('retired' in t or 'zero' in t or 'no ' in t or 'never' in t or 'not ' in t): return 'C6'
    if 'velopack' in t: return 'C7'
    if 'anycpu' in t: return 'C8'
    if 'diagnostics' in t and ('projectreference' in t or 'third' in t): return 'C11'
    if ('sibling-library' in t or 'sibling library' in t) and ('three' in t or 'xisf' in t): return 'C10'
    if ('one project' in t or 'authored here' in t) and ('two' in t or 'tests' in t): return 'C9'
    if 'button_graph_click' in t and ('single' in t or 'entry point' in t or 'rungraphbuildasync' in t): return 'C12'
    if 'renderarea' in t and ('resizealtitudechartarea' in t or '4-step' in t or 'four' in t or 'four-step' in t): return 'C13'
    if 'mformclosingcts' in t or ('whenany' in t and 'only' in t) or ('targetscanner.scanasync' in t and 'token' in t): return 'C14'
    if 'maxofhorizonprofile' in t or ('floor' in t and 'polyline' in t): return 'C16'
    if 'copyfromscreen' in t or 'drawtobitmap' in t or ('screencapture' in t and 'diagnosticsdialog' in t): return 'C17'
    if 'docs/design' in t and ('naming' in t or 'date prefix' in t or 'yyyy' in t or 'undated' in t): return 'C18'
    # newly discovered in reps
    if 'astrometryui' in t: return 'C19'
    if 'designer.cs' in t and ('1400' in t or '1707' in t or 'lines' in t): return 'C20'
    if ('user defaults' in t) or ('defaults' in t and 'menu' in t and ('clear' in t or 'edit settings' in t)): return 'C21'
    if ('e:\\projects\\visualstudio' in t or 'visualstudio\\astronomy' in t or 'absolute path' in t) and 'library' in t: return 'Cloc'
    # honest unverifiable core-contract dispositions (not solid findings)
    if ('ireadonlylist' in t or 'datetime.kind' in t or 'timekindguard' in t or 'signed-degree' in t or 'signed degree' in t or 'static mutable' in t or 'observationmoment' in t or 'location.elevation' in t or 'meridianaltitude' in t) and ('unverifiable' in t):
        return 'UNVERIF-core'
    return None

SOLID={'C1','C2','C3','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C17','P1','P2','X1','X2','X3','X4','X5','X6','C19','C21'}
SOFT={'C4','C16','C18','C20','Cloc'}

# classify
import collections
percell={}  # (model,rep)-> set of ids
unmatched=collections.Counter()
unmatched_ex={}
for m in ['opus','sonnet']:
    for rep in sorted(reps[m]):
        ids=set()
        for f in reps[m][rep]:
            cid=classify(f)
            if cid is None:
                key=f.get('claim','')[:60]
                unmatched[key]+=1
                unmatched_ex[key]=f
            else:
                ids.add(cid)
        percell[(m,rep)]=ids

# cumulative recall curve (SOLID only)
print('=== per-rep SOLID issue ids ===')
for m in ['opus','sonnet']:
    for rep in sorted(reps[m]):
        s=sorted(x for x in percell[(m,rep)] if x in SOLID)
        print('  %s rep%d: %d solid  %s' % (m,rep,len(s),s))
print()
print('=== CUMULATIVE solid recall (rep0..repN) ===')
allsolid=set()
for m in ['opus','sonnet']:
    cum=set(); print(' ',m)
    for rep in sorted(reps[m]):
        cum |= {x for x in percell[(m,rep)] if x in SOLID}
        print('    after rep%d: %2d cumulative solid' % (rep,len(cum)))
    print('    UNION(%s) solid = %d : %s' % (m,len(cum),sorted(cum)))
    reps[m]['_union']=cum
    allsolid|=cum
print()
ou=reps['opus']['_union']; su=reps['sonnet']['_union']
print('Opus solid union: %d'%len(ou))
print('Sonnet solid union: %d'%len(su))
print('Shared: %d  %s'%(len(ou&su),sorted(ou&su)))
print('Opus-only: %s'%sorted(ou-su))
print('Sonnet-only: %s'%sorted(su-ou))
print('Overall solid union across both: %d  %s'%(len(allsolid),sorted(allsolid)))
print()
print('=== UNMATCHED flags (need manual look) ===')
for k,c in unmatched.most_common():
    print('  x%d: %s'%(c,k))

# ---- dump durable summary ----
summary={
 'experiment':'exp2-convergence','effort':'high',
 'sources':{'rep0':'exp1 wf0ozweuh','rep1-3':'fullrerun w02p76xdr'},
 'perRepSolid':{m:{rep:sorted(x for x in percell[(m,rep)] if x in SOLID) for rep in sorted(x for x in reps[m] if isinstance(x,int))} for m in ['opus','sonnet']},
 'cumulative':{},
 'unions':{'opus':sorted(reps['opus']['_union']),'sonnet':sorted(reps['sonnet']['_union']),
           'shared':sorted(reps['opus']['_union']&reps['sonnet']['_union']),
           'opusOnly':sorted(reps['opus']['_union']-reps['sonnet']['_union']),
           'sonnetOnly':sorted(reps['sonnet']['_union']-reps['opus']['_union']),
           'overall':sorted(allsolid)},
 'unmatchedLongTail':{k:c for k,c in unmatched.most_common()},
}
for m in ['opus','sonnet']:
    cum=set(); curve=[]
    for rep in sorted(x for x in reps[m] if isinstance(x,int)):
        cum|={x for x in percell[(m,rep)] if x in SOLID}; curve.append(len(cum))
    summary['cumulative'][m]=curve
open(DOCS+'sweeps/exp2-convergence.json','w',encoding='utf-8').write(json.dumps(summary,indent=2))
print('saved exp2-convergence.json; curves:',summary['cumulative'])
