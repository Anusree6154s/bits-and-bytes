---
layout: default
title: Load Testing
date: Nov 10, 2026
excerpt: Understanding load testing
parent: Devops And Infrastructure
permalink: load-testing
---

# Load Testing

| Testing tests               | purpose                               | duration  | typically load            |
| --------------------------- | ------------------------------------- | --------- | ------------------------- |
| Smoke test                  | verify system works                   | 1-5 min   | very low                 |
| Load                        | verify expected traffic               | 5-30 min  | expected production load. |
| Stress                      | Find breaking point                   | 10-30 min | Beyond expected load!     |
| Spike                       | Test sudden traffic surges            | Few mins  | Instant large jump        |
| Soak                        | Find long term issues.                | Hours     | Normal load               |
| Scalability                 | verify horizontal/vertical scaling    | load.     |
| Breakpoint                  | Find exact failure point              |           |                           |
| Failure                     | verify recovery from failures         |           |                           |
| Chaos                       | Intentionally inject failures         |           |                           |
| Capacity                    | Determine max sustainable throughput. |           |                           |
| Resilience test             |                                       |           |
| Performance regression test |                                       |           |

## Load Testing proper table (generally used ones)

- Test type: Smoke test
  - Purpose :- Verify test setup & basic functionality
  - Typical load vs normal :- 1-5% (10-15 users)
  - Duration :- seconds to 5 min
- Load Test (must have)
  - Validate performance under expected load
  - load :- 100% (1000 users)
  - Duration :- 15 min to 1 hr
- Avg. load test
  - Simulate normal business day
  - load :- 50-80% (500-800 users)
  - duration :- 30 min to several hrs
- Stress test (must have)
  - Find breaking point
  - load :- 120-500% (1200-5000+ users)
  - duration :- minutes
- Soak/endurance test (sustained test) (must have)
  - Long period check to detect memory leak, connection leak, eta degradation, etc.
  - load :- 70-100% (700-1000 users sustained)
  - duration :- 4-72 hrs (3 days)
  - Capacity test (sometimes )
    - Find max load, while still meeting SLA.
    - SLA :- Service level agreement.
      - A document agreement
      - defines what level of service must be defined & how it is measured.
      - typical metrics include uptime, response time, resolution time, availability.
      - If provide fails to meet targets, SLA may specify penalties, service credits or remedies.
      - eg: if an application's SLA is
      - availability = 99.9%
      - P95 latency < 300 ms
      - error rate < 0.1%
      - then during load tests these must be maintained.
    - ### Related terms
      - SLI (Service level indicator)
        - The measurement values
        - Eg: availability, P95 latency, P95 etc
      - SLO (Service level objective)
        - A target for an SLI / engineerng goal
        - Eg: P95 latency < 300ms - over a rolling 30-day period
        - 99% successful requests over 30 days
      - SLA (Service level agreement)
        - customer facing promise
        - involves business/legal consequences
        - P95 latency (Percentile 95 latency)
        - A method to display response times/latency
        - monitoring:
        - Eg: P95 = 300 ms means 95% of requests completed in 300ms or less - 5% faile.
    - load :- Gradually increase from 100% upward.
    - duration :- 30 min - 2 hr
    - Classically stress test but to find near point in compliance of SLA).
- Scalability test
  - verify scaling behaviour when adding resources.
  - load :- incrementally increasing load.
  - duration :- Hours
- Volume test :-
  - Test large data size (not user count)
  - load :- normal users, huge data volume.
  - duration :- series
- Concurrency test :-
  - Many users hitting same resource simultaneously.
  - load :- 100-300% on specific endpoint
  - durations :- minutes
- Resilience test
  - Behaviour during failure.
  - load :- normal load + injected failures.
  - duration :- 30 min to hours.
- Recovery test (outage)
  - Recovery after outage/crash.
  - load :- usually after stress/spike.
  - duration :- mins to hours.
- Peak test (traffic)
  - Validate operation during known peak traffic.
  - load :- 100-150% of highest expected peak.
  - duration :- 30 min to 2 hrs.
  - diff from concurrency testing in a way that enteric apps heavy load is tested.
  - Testing expected real life, high traffic like black friday sale.

## Common load testing tools

- From local m/c to deployed appk6, Apache JMeter (UI based testing - JSlocust (Python scripts based)artillery (yaml based ver &)
- k6 
    - JS based
    - CLI/UI friendly
    - used heavily w/ nestJS + K8s
- Artillery 
    - node native alternative
    - yaml or JS based
- Apache JMeter 
    - GUI based.
    - Manual entry of endpoints.
    - used in banks / large enterprises.
    - legacy
- locust 
    - python based.
    - distributed load testing support.
- For backend HTTP tools (for quick checks only).
    - wrk, autocannon, hey
    - used for raw benchmarks & not full scenarios. 
    
