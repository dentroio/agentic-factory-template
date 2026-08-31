# WO-004 — Do not invent extra features during WO-003

**Status:** Open
**Priority:** P2
**Effort:** S

## Problem

During review of the About page, someone will want a footer, analytics, or a dark theme. Those must not land in WO-003.

## What to Build

This WO exists as a **follow-on placeholder**. Implement only if you actually want a site footer: add a one-line footer on home and About: “Built with the Agentic Factory template.”

## Out of scope

Analytics, auth, redesign.

## Acceptance Criteria

1. Footer text present on both pages **or** this spec stays Open until you decide to dispatch it
2. Does not change the greeting string from WO-001

## Execution

- **Branch:** `wo/004-footer`
- **Risk tier:** P2
- **PR title:** `feat(demo): WO-004 — site footer`
- **Pre-PR gate:** `make ci-local`
- **Depends on:** WO-003
- **User verification required:** Yes — see footer on both pages
