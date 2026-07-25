---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/gcp/gcp-credentials-note.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Tip:** You saved a file containing your service account key credentials
in the `Create a GCP Service Account <gcp-register-account>`
step of this guide.
If you downloaded your credentials in JSON format, you can
use the following command to extract the value of your private
key, substituting `<credentials-filename>` with the name of
your credentials file. The following command requires that you
install [OpenSSL](https://docs.openssl.org/master/)_:
.. code-block::
   :copyable: true
   cat <credentials-filename> | jq -r .private_key | openssl pkcs8 -topk8 -nocrypt -inform PEM -outform DER | base64
If you downloaded your credentials in PKCS12 format, you need to
specify your GCP service account import password and to add a
PEM pass phrase to access the key when accessing it using the
following command, substituting `<credentials-filename>` with
the name of your credentials file:
.. code-block::
   :copyable: true
   openssl pkcs12 -info -in <credentials-filename>
