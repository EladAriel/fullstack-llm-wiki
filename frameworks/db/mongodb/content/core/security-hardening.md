---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-hardening.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================================

# Network and Configuration Hardening for Self-Managed Deployments

To reduce the risk exposure of the entire MongoDB system, ensure that only trusted hosts have access to MongoDB.

## MongoDB Configuration Hardening

### IP Binding

.. include:: /includes/fact-default-bind-ip-change.rst

.. include:: /includes/warning-bind-ip-security-considerations.rst

> **Warning:** Make sure that your :binary:`~bin.mongod` and :binary:`~bin.mongos`
instances are only accessible on trusted networks. If your system
has more than one network interface, bind MongoDB programs to the
private or internal network interface.

For more information, see `/core/security-mongodb-configuration`.

## Network Hardening

### Firewalls

Firewalls allow administrators to filter and control access to a system by providing granular control over network communications. For administrators of MongoDB, the following capabilities are important: limiting incoming traffic on a specific port to specific systems and limiting incoming traffic from untrusted hosts.

On Linux systems, the `iptables` interface provides access to the underlying `netfilter` firewall. On Windows systems, `netsh` command line interface provides access to the underlying Windows Firewall. For additional information about firewall configuration, see:

- `/tutorial/configure-linux-iptables-firewall` and
- `/tutorial/configure-windows-netsh-firewall`.
For best results and to minimize overall exposure, ensure that only traffic from trusted sources can reach :binary:`~bin.mongod` and :binary:`~bin.mongos` instances and that the :binary:`~bin.mongod` and :binary:`~bin.mongos` instances can only connect to trusted outputs.

### Virtual Private Networks

Virtual private networks, or VPNs, make it possible to link two networks over an encrypted and limited-access trusted network. Typically, MongoDB users who use VPNs use TLS/SSL rather than IPSEC VPNs for performance issues.

Depending on configuration and implementation, VPNs provide for certificate validation and a choice of encryption protocols, which requires a rigorous level of authentication and identification of all clients. Furthermore, because VPNs provide a secure tunnel, by using a VPN connection to control access to your MongoDB instance, you can prevent tampering and "man-in-the-middle" attacks.

### Disable IP Forwarding

IP forwarding allows servers to forward packets to other systems.  Disable this feature on servers that host :program:`mongod`.

## Contents

- IP Binding </core/security-mongodb-configuration>
- Use Linux iptables  </tutorial/configure-linux-iptables-firewall>
- Use Windows netsh </tutorial/configure-windows-netsh-firewall>
