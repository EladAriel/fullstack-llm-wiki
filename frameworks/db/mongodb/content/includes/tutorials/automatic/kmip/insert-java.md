---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/kmip/insert-java.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```java
public static void insertPatient(
    MongoCollection collection,
    String name,
    int ssn,
    String bloodType,
    ArrayList<Document> medicalRecords,
    int policyNumber,
    String provider
) {

    Document insurance = new Document()
        .append("policyNumber", policyNumber)
        .append("provider", provider);

    Document patient = new Document()
        .append("name", name)
        .append("ssn", ssn)
        .append("bloodType", bloodType)
        .append("medicalRecords", medicalRecords)
        .append("insurance", insurance);

    collection.insertOne(patient);
}
```
