# WO-001 — Change the demo greeting

**Status:** Open
**Priority:** P2
**Effort:** S
**Services:** demo

## Problem

The demo page at http://localhost:8765 shows “Hello, factory”. New users should see that Work Orders can change a running product, not only a file on disk.

## What to Build

In `demo/public/index.html`, change the greeting text to **Hello, Work Orders**. Update `demo/test_greeting.py` so the test expects the new string.

## Out of scope

Restyling the page. Adding authentication.

## Acceptance Criteria

1. http://localhost:8765 shows “Hello, Work Orders”
2. `make ci-local` passes
3. A human confirmed the browser before commit

## Execution

- **Branch:** `wo/001-change-greeting`
- **Risk tier:** P2
- **Services:** demo
- **PR title:** `feat(demo): WO-001 — change greeting to Hello, Work Orders`
- **Pre-PR gate:** `make ci-local`
- **Depends on:** none
- **User verification required:** Yes — open http://localhost:8765, confirm the heading
