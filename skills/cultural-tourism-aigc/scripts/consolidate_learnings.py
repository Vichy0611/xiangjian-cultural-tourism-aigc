#!/usr/bin/env python3
"""Convert an aggregate learning summary into a human-reviewable Skill note."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def render(summary: dict) -> str:
    required = {'completed_generations', 'revision_events', 'route_counts', 'transition_counts', 'issue_counts'}
    missing = required - summary.keys()
    if missing:
        raise ValueError('missing fields: ' + ', '.join(sorted(missing)))
    lines = [
        '# Experience review', '',
        '> Aggregate signals only. Review before promoting any item into canonical Skill guidance.', '',
        f"- Completed generations: {summary['completed_generations']}",
        f"- Revision events: {summary['revision_events']}", '',
        '## Repeated correction signals', '',
    ]
    issues = sorted(summary['issue_counts'].items(), key=lambda item: (-item[1], item[0]))
    lines.extend(f'- `{name}`: {count}' for name, count in issues) if issues else lines.append('- None')
    lines.extend(['', '## Production patterns', ''])
    lines.append('- Routes: ' + (', '.join(f'`{k}` {v}' for k, v in sorted(summary['route_counts'].items())) or 'none'))
    lines.append('- Transitions: ' + (', '.join(f'`{k}` {v}' for k, v in sorted(summary['transition_counts'].items())) or 'none'))
    lines.extend(['', '## Human decision', '', '- [ ] Evidence comes from multiple projects.', '- [ ] The condition of use is explicit.', '- [ ] No private content is present.', '- [ ] Approved for manual promotion.', ''])
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('summary', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    summary = json.loads(args.summary.read_text(encoding='utf-8'))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(summary), encoding='utf-8')
    print(args.output)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
