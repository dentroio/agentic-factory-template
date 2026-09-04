# WO-002 — Document the local verify command in README

**Status:** Open
**Priority:** P3
**Effort:** S
**Services:** docs

## Problem

Someone cloning this repo may not notice `make run` in the README.

## What to Build

Ensure README has a “Demo app” section with `make run` and `make ci-local`. If already present, add one sentence that WO-001 is the first sample work order.

## Out of scope

Changing the demo app.

## Acceptance Criteria

1. README mentions `make run` and `make ci-local`
2. No application code changed

## Execution

- **Branch:** `wo/002-readme-verify`
- **Risk tier:** P3
- **Services:** docs
- **PR title:** `docs: WO-002 — document verify commands`
- **Pre-PR gate:** `make ci-local`
- **Depends on:** none
- **User verification required:** No
