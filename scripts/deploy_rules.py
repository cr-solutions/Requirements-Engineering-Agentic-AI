#!/usr/bin/env python3
"""Deploy the master rules file (.ai-rules.md) into the tool-specific rules file of a project.

Usage:
    python3 scripts/deploy_rules.py <tool> <project-dir>
    python3 scripts/deploy_rules.py --list

Only the text between the markers
    <!-- BEGIN:ai-rules ... -->  and  <!-- END:ai-rules -->
is replaced. Everything else in the target file (front matter, project context,
imports) stays untouched, so the script is safe to run repeatedly.
"""
import logging
import re
import sys
from pathlib import Path

LOGGER = logging.getLogger('deploy_rules')

# Exit codes follow the system range 0-99 from the global rules.
EXIT_OK = 0
EXIT_USAGE = 2
EXIT_MISSING_FILE = 3
EXIT_MISSING_MARKER = 4

MASTER_FILE = Path(__file__).resolve().parent.parent / '.ai-rules.md'

# One entry per supported tool: path of the rules file relative to the project dir.
# Why a plain dict: adding a tool is a one-line change and needs no new code path.
TARGETS = {
    'kiro': '.kiro/steering/global_rules.md',
    'claude': 'CLAUDE.md',
    'gemini': 'GEMINI.md',
    'antigravity': 'AGENTS.md',
    'cursor': '.cursor/rules/global-rules.mdc',
    'copilot': '.github/copilot-instructions.md',
    'agents-md': 'AGENTS.md',
}

BLOCK_PATTERN = re.compile(
    r'(<!-- BEGIN:ai-rules[^\n]*-->\n).*?(<!-- END:ai-rules -->)',
    re.DOTALL,
)


class DeployError(Exception):
    """Raised for any failure that should end the script with a specific exit code."""

    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


def render_block(master_text):
    # Why the trailing newline: the END marker must start on its own line.
    return master_text.rstrip('\n') + '\n'


def deploy(tool, project_dir):
    target_rel = TARGETS.get(tool)
    if target_rel is None:
        raise DeployError(f'Unknown tool "{tool}". Supported: {", ".join(sorted(TARGETS))}', EXIT_USAGE)

    # EAFP: just try to read, the OSError tells us what is wrong.
    try:
        master_text = MASTER_FILE.read_text(encoding='utf-8')
    except OSError as error:
        raise DeployError(f'Cannot read master file {MASTER_FILE}: {error}', EXIT_MISSING_FILE)

    target = Path(project_dir) / target_rel
    try:
        target_text = target.read_text(encoding='utf-8')
    except OSError as error:
        raise DeployError(f'Cannot read target file {target}: {error}', EXIT_MISSING_FILE)

    if not BLOCK_PATTERN.search(target_text):
        raise DeployError(f'No ai-rules markers found in {target}', EXIT_MISSING_MARKER)

    # Why a lambda: the master text contains backslashes, which re.sub would otherwise interpret.
    new_text = BLOCK_PATTERN.sub(
        lambda match: match.group(1) + render_block(master_text) + match.group(2),
        target_text,
        count=1,
    )
    # Why open() and not write_text(): the newline argument needs Python 3.10+, and we always want LF.
    with target.open('w', encoding='utf-8', newline='\n') as handle:
        handle.write(new_text)
    LOGGER.info('Deployed %s into %s', MASTER_FILE.name, target)


def main(argv):
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    if argv == ['--list']:
        for tool, rel in sorted(TARGETS.items()):
            print(f'{tool:12} {rel}')
        return EXIT_OK

    if len(argv) != 2:
        print(__doc__)
        return EXIT_USAGE

    try:
        deploy(argv[0], argv[1])
    except DeployError as error:
        LOGGER.error('%s', error)
        return error.code
    return EXIT_OK


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
