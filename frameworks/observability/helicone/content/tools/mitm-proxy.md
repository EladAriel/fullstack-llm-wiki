---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/tools/mitm-proxy.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.200181Z"
---
---
title: "Man-in-the-Middle Proxy"
description: "Automatically capture your logs without changing any code."
---

<Warning>

## Important: Please Read This First

This is a work in progress and may include bugs or other issues. If you encounter any problems, please report them.

<b>This tool is NOT intended for production use.</b>

This tool is designed for testing and debugging purposes only.

</Warning>

## How It Works

<Info>MITM = Man-in-the-Middle Proxy</Info>

The proxy operates as a simple HTTP server that listens on a specified port. It is configured to intercept all traffic destined for `api.openai.com` and reroutes it—with the correct headers and configurations to `oai.helicone.ai`. This enables you to swiftly integrate Helicone and all of its features without having to alter a single line of code.

# Potential Use Cases for the MITM Proxy

- Github Actions
  - Continuous Integration/Continuous Deployment (CI/CD)
  - Testing
  - Debugging
  - Cost savings (utilizing Bucket Cache)
- Local Development
  - Debugging
  - Testing
  - Cost savings (utilizing Bucket Cache)

## Installation (Ubuntu/Debian)

<Warning>Use this tool only in controlled/testing environments.</Warning>

We provide a script that will automatically install and configure the proxy for you.

### Starting the Proxy

```bash
# Configure Cache
export HELICONE_CACHE_ENABLED="true" # Enable caching

# Configure Custom Properties
# Note: There is a lock file that allows you to configure properties dynamically
export HELICONE_PROPERTY_<PROPERTY_NAME>="<PROPERTY_VALUE>" # Set custom properties

bash -c "$(curl -fsSL https://raw.githubusercontent.com/Helicone/helicone/main/mitmproxy.sh)" -s start
echo "sk-<HELICONE_KEY>" > ~/.helicone/api_key # Alternatively, you can export HELICONE_API_KEY to your path before starting the proxy to bypass this step.

export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt # This is required for HTTPS requests to work properly.
# Your python script here...
```

### Stopping the Proxy

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/Helicone/helicone/main/mitmproxy.sh)" -s stop
```

### Viewing Logs

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/Helicone/helicone/main/mitmproxy.sh)" -s tail
```

## Installation (Mac)

<Warning>
  We do not recommend installing this on your local machine. Instead, please use
  a virtual environment or a container. Man-in-the-Middle (MITM) Proxies can
  pose serious security risks.
</Warning>

To install on a Mac, follow the same instructions as for Ubuntu/Debian, but use the `mitmproxy_mac.sh` script instead. You can find this script here: `https://raw.githubusercontent.com/Helicone/helicone/main/mitmproxy_mac.sh`

## Configuring the Dynamic Helicone Headers

You can configure custom properties using a lock file located at `~/.helicone/custom_properties.json`. These properties will be applied to all requests.

```json
{
  "<PROPERTY_NAME>": "<PROPERTY_VALUE>"
}
```

To dynamically configure the proxy, you can install our python package.

```bash
pip install helicone
```

Then, use the following code:

```python
from helicone.lock import HeliconeLockManager
HeliconeLockManager.write_custom_property("job_id", "1")
'''
Other Methods:
 - write_custom_property(property_name: str, value: str) // Write a custom property
 - remove_custom_property(property_name: str) // Remove a custom property
 - clear_all_properties() // Clear all properties
'''
```

This enables you to manipulate properties dynamically, making your workflow more flexible and efficient.
