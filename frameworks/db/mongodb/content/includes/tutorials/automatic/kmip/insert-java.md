---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/kmip/insert-java.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
