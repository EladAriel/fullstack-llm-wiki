---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/enable-authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# Enable Access Control on Self-Managed Deployments

.. include:: /includes/LDAP-deprecated.rst

Enabling access control on a MongoDB deployment enforces authentication. With access control enabled, users must authenticate and can only perform actions permitted by their assigned roles.

> **Note:** You can't disable access control in {+atlas+}.

## Access Control Resources

To enable access control for a standalone instance, see the following resources:

- `/tutorial/configure-scram-client-authentication`
- `/tutorial/configure-x509-client-authentication`
- `/tutorial/control-access-to-mongodb-with-kerberos-authentication`
- `/tutorial/control-access-to-mongodb-windows-with-kerberos-authentication`
- `/tutorial/kerberos-auth-activedirectory-authz`
- `/tutorial/configure-ldap-sasl-activedirectory`
- `/tutorial/configure-ldap-sasl-openldap`
- `/tutorial/authenticate-nativeldap-activedirectory`
- `/core/oidc/security-oidc`
To enable access control for a `replica set </replication>` or a `sharded cluster <sharding-sharded-cluster>`, see the following resources:

- `/tutorial/deploy-replica-set-with-keyfile-access-control`
- `/tutorial/enforce-keyfile-access-control-in-existing-replica-set`
- `/tutorial/enforce-keyfile-access-control-in-existing-replica-set-without-downtime`
- `/tutorial/deploy-sharded-cluster-with-keyfile-access-control`
- `/tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster`
- `/tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster-no-downtime`
- `/tutorial/control-access-to-mongodb-with-kerberos-authentication`
- `/tutorial/control-access-to-mongodb-windows-with-kerberos-authentication`
- `/tutorial/kerberos-auth-activedirectory-authz`
- `/tutorial/configure-ldap-sasl-activedirectory`
- `/tutorial/configure-ldap-sasl-openldap`
- `/tutorial/authenticate-nativeldap-activedirectory`
## Next Steps

To create additional users, see `/tutorial/create-users`.

To manage users, assign roles, and create custom roles, see `/tutorial/manage-users-and-roles`.
