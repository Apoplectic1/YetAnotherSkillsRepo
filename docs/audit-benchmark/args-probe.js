export const meta = {
  name: 'args-probe',
  description: 'Diagnostic: report what the args global actually contains (no agents spawned)',
  phases: [{ title: 'probe' }],
}

// FIX: normalize args — it may arrive as a JSON string OR an object OR undefined
const A = (typeof args === 'string') ? JSON.parse(args) : (args || {})

const report = {
  rawArgsType: typeof args,
  normalizedHasCells: !!A.cells,
  cellsIsArray: Array.isArray(A.cells),
  cellsLen: Array.isArray(A.cells) ? A.cells.length : null,
  branchTaken: A.cells ? 'backfill' : 'FULL-MATRIX',
}
log('args-probe: ' + JSON.stringify(report))
return report
