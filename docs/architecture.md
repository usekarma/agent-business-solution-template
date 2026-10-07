# Architecture

## Context

Describe the system boundary and neighboring systems.

## Components

Document each component and its responsibility.

## Data flow

Document the happy path and important failure paths.

## State and idempotency

Where is business state stored? What makes repeated requests safe?

## Failure model

For each external dependency, document:

- timeout
- retry policy
- permanent failure behavior
- recovery strategy

## Observability

Document logs, metrics, traces, dashboards, and alerts.

## Security

Document authentication, authorization, secrets, network boundaries, and sensitive data handling.
