---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/health-managers.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/health-manager-short-names.rst

==================================================================

# Configure Self-Managed Sharded Cluster Health with Health Managers

This document describes how to use |HMS| to monitor and manage sharded cluster health issues.

## Overview

A |HM| runs health checks on a `health manager facet` at a specified `intensity level <health-managers-intensity-levels>`. |HM| checks run at specified time intervals. A |HM| can be configured to move a failing `mongos <mongos>` out of a cluster automatically. `Progress Monitor <health-managers-progress-monitor>` ensures that |HM| checks do not become stuck or unresponsive.

### Health Manager Facets

The following table shows the available |HM| facets:

.. include:: /includes/fact-health-manager-facets.rst

### Health Manager Intensity Levels

The following table shows the available |HM| intensity levels:

.. include:: /includes/fact-health-manager-intensities.rst

## Active Fault Duration

When a failure is detected and the |HM| intensity level is set to `critical`, the |HM| waits the amount of time specified by :parameter:`activeFaultDurationSecs` before stopping and moving the `mongos <mongos>` out of the cluster automatically.

## Progress Monitor

.. include:: /includes/fact-progressMonitor.rst

### `progressMonitor` Fields

.. include:: /includes/fact-progress-monitor-fields.rst

## Examples

The following examples show how |HMS| can be configured. For information on |HM| parameters, see `Health Manager Parameters <health-manager-parameters>`.

### Intensity

.. include:: /includes/example-healthMonitoringIntensities.rst

.. include:: /includes/fact-healthMonitoringIntensities-values-array.rst

See :parameter:`healthMonitoringIntensities` for details.

### Intervals

.. include:: /includes/example-healthMonitoringIntervals.rst

.. include:: /includes/fact-healthMonitoringIntervals-values-array.rst

See :parameter:`healthMonitoringIntervals` for details.

### Active Fault Duration

.. include:: /includes/example-activeFaultDurationSecs.rst

See :parameter:`activeFaultDurationSecs` for details.

### Progress Monitor

.. include:: /includes/fact-progressMonitor.rst

.. include:: /includes/example-progress-monitor.rst

See :parameter:`progressMonitor` for details.
