---
type: "Framework Learn Page"
framework: "Prometheus"
source_repo: "https://github.com/prometheus/docs.git"
source_branch: "main"
source_path: "docs/instrumenting/pushing.md"
source_commit: "9d9e0343a9e6d138204cfe316a125a860a271849"
source_commit_short: "9d9e034"
source_commit_date: "2026-07-21T23:07:09+02:00"
generated_at: "2026-07-25T19:07:59.761329Z"
---
# Pushing

---
title: Pushing metrics
sort_rank: 3
---

Occasionally you will need to monitor components which cannot be scraped. The
[Prometheus Pushgateway](https://github.com/prometheus/pushgateway) allows you
to push time series from [short-lived service-level batch
jobs](/docs/practices/pushing/) to an intermediary job which Prometheus can
scrape. Combined with Prometheus's simple text-based exposition format, this
makes it easy to instrument even shell scripts without a client library.

 * For more information on using the Pushgateway and use from a Unix shell, see the project's
[README.md](https://github.com/prometheus/pushgateway#readme).

 * For use from Java see the
[Pushgateway documentation](https://prometheus.github.io/client_java/exporters/pushgateway/).

 * For use from Go see the [Push](https://pkg.go.dev/github.com/prometheus/client_golang/prometheus/push#Pusher.Push) and [Add](https://pkg.go.dev/github.com/prometheus/client_golang/prometheus/push#Pusher.Add) methods.

 * For use from Python see [Exporting to a Pushgateway](https://prometheus.github.io/client_python/exporting/pushgateway/).

 * For use from Ruby see the [Pushgateway documentation](https://github.com/prometheus/client_ruby#pushgateway).

* To find out about Pushgateway support of [client libraries maintained outside of the Prometheus project](/docs/instrumenting/clientlibs/), refer to their respective documentation.
