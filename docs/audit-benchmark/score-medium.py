import json, collections

DOCS='E:/Projects/AI/Skills/doc-architecture/docs/audit-benchmark/'

# Sonnet/medium reps: rep1 = Exp-3 screen; rep2,rep3 = follow-up (wuplfg72m)
rep1f=json.load(open(DOCS+'raw/exp3-sonnet-medium-w1bb4ilfs.output.json',encoding='utf-8'))
rep23f=json.load(open(DOCS+'raw/exp3-sonnet-medium-rep2-3-wuplfg72m.output.json',encoding='utf-8'))

reps={}  # rep -> list of flags
def absorb(d):
    for cell,v in d['result']['byCell'].items():
        rep=int(cell.split('/')[2].replace('rep',''))
        flags=[]
        for k,fl in v['units'].items(): flags+=fl
        reps[rep]=flags
absorb(rep1f); absorb(rep23f)

def textof(f): return (f.get('location','')+' || '+f.get('claim','')+' || '+f.get('finding','')+' || '+f.get('evidence','')).lower()

# classifier — byte-identical signatures to score.py (Exp-2), so medium maps onto the same catalog
def classify(f):
    t=textof(f)
    def has(*subs): return all(s in t for s in subs)
    if 'mode-removal' in t: return 'X6'
    if 'screenshot.png' in t: return 'X3'
    if 'code-quality-audit.md' in t and 'roadmap' in t: return 'X2'
    if 'code-quality-audit.md' in t: return 'X5'
    if 'sky-brightness-day-sky' in t or ('anchor' in t and 'sky-brightness' in t) or ('#sky-brightness' in t): return 'X4'
    if '..\\claude.md' in t or 'parent' in t and 'claude.md' in t and 'auto-load' in t or ('../claude.md' in t): return 'X1'
    if 'parent' in t and 'claude.md' in t: return 'X1'
    if 'core consumer contract' in t and ('move' in t or 'reference-grade' in t or 'architecture' in t or 'reference doc' in t or 'router' in t): return 'P2'
    if ('build / run' in t or 'build/run' in t) and ('tool preference' in t or 'stranded' in t or 'orphan' in t or 'empty' in t or 'misplaced' in t): return 'P1'
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
    if 'astrometryui' in t: return 'C19'
    if 'designer.cs' in t and ('1400' in t or '1707' in t or 'lines' in t): return 'C20'
    if ('user defaults' in t) or ('defaults' in t and 'menu' in t and ('clear' in t or 'edit settings' in t)): return 'C21'
    if ('e:\\projects\\visualstudio' in t or 'visualstudio\\astronomy' in t or 'absolute path' in t) and 'library' in t: return 'Cloc'
    if ('ireadonlylist' in t or 'datetime.kind' in t or 'timekindguard' in t or 'signed-degree' in t or 'signed degree' in t or 'static mutable' in t or 'observationmoment' in t or 'location.elevation' in t or 'meridianaltitude' in t) and ('unverifiable' in t):
        return 'UNVERIF-core'
    return None

SOLID={'C1','C2','C3','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C17','P1','P2','X1','X2','X3','X4','X5','X6','C19','C21'}
SOFT={'C4','C16','C18','C20','Cloc'}

percell={}; unmatched=collections.Counter(); unmatched_ex={}
for rep in sorted(reps):
    ids=set()
    for f in reps[rep]:
        cid=classify(f)
        if cid is None:
            key=f.get('claim','')[:70]; unmatched[key]+=1; unmatched_ex[key]=f
        else: ids.add(cid)
    percell[rep]=ids

print('=== Sonnet/MEDIUM per-rep ids ===')
for rep in sorted(reps):
    s=sorted(x for x in percell[rep] if x in SOLID)
    sf=sorted(x for x in percell[rep] if x in SOFT)
    print('  rep%d: %d flags -> %d solid %s  | %d soft %s' % (rep,len(reps[rep]),len(s),s,len(sf),sf))

print('\n=== CUMULATIVE solid recall (medium) ===')
cum=set(); curve=[]
for rep in sorted(reps):
    cum|={x for x in percell[rep] if x in SOLID}; curve.append(len(cum))
    print('    after rep%d: %2d cumulative solid' % (rep,len(cum)))
medium_union=sorted(cum)
print('    MEDIUM union solid = %d : %s' % (len(cum),medium_union))

# compare vs Sonnet/HIGH baseline (from exp2-convergence.json)
hi=json.load(open(DOCS+'sweeps/exp2-convergence.json',encoding='utf-8'))
hi_sonnet=set(hi['unions']['sonnet'])
print('\n=== MEDIUM vs Sonnet/HIGH ===')
print('  Sonnet/HIGH union (%d): %s' % (len(hi_sonnet),sorted(hi_sonnet)))
print('  Sonnet/MED  union (%d): %s' % (len(cum),sorted(cum)))
print('  shared:        %s' % sorted(cum & hi_sonnet))
print('  MED-only:      %s' % sorted(cum - hi_sonnet))
print('  HIGH-only(med missed): %s' % sorted(hi_sonnet - cum))
print('  high per-rep curve:', hi['cumulative']['sonnet'])

print('\n=== UNMATCHED (long-tail / possibly new-real) ===')
for k,c in unmatched.most_common():
    print('  x%d: %s' % (c,k))

summary={
 'experiment':'exp3-sonnet-medium','effort':'medium','model':'sonnet',
 'sources':{'rep1':'exp3 screen w1bb4ilfs','rep2-3':'follow-up wuplfg72m'},
 'perRepSolid':{rep:sorted(x for x in percell[rep] if x in SOLID) for rep in sorted(reps)},
 'perRepSoft':{rep:sorted(x for x in percell[rep] if x in SOFT) for rep in sorted(reps)},
 'cumulativeSolid':curve,
 'unionSolid':medium_union,
 'vsSonnetHigh':{
   'highUnion':sorted(hi_sonnet),'medUnion':sorted(cum),
   'shared':sorted(cum&hi_sonnet),'medOnly':sorted(cum-hi_sonnet),
   'highOnlyMedMissed':sorted(hi_sonnet-cum),'highCurve':hi['cumulative']['sonnet'],
 },
 'unmatchedLongTail':{k:c for k,c in unmatched.most_common()},
 'perRepFlagCount':{rep:len(reps[rep]) for rep in sorted(reps)},
}
open(DOCS+'sweeps/exp3-sonnet-medium.json','w',encoding='utf-8').write(json.dumps(summary,indent=2))
print('\nsaved sweeps/exp3-sonnet-medium.json')
