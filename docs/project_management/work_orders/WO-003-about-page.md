# WO-003 — Add an About page

**Status:** Open
**Priority:** P2
**Effort:** S
**Services:** demo

## Problem

The demo is a single page. Users should see a second route so a WO can add a file without rewriting the home greeting.

## What to Build

Add `demo/public/about.html` with heading “About this template” and a link from `index.html` labeled “About”. Serve it with the existing static server (same directory).

## Out of scope

Authentication, CSS frameworks, changing the home greeting (that is WO-001).

## Acceptance Criteria

1. http://localhost:8765/about.html shows the About heading
2. Home page links to About
3. `make ci-local` passes
4. Human confirmed both pages in the browser

## Execution

- **Branch:** `wo/003-about-page`
- **Risk tier:** P2
- **Services:** demo
- **PR title:** `feat(demo): WO-003 — add About page`
- **Pre-PR gate:** `make ci-local`
- **Depends on:** none
- **User verification required:** Yes — open home and About
