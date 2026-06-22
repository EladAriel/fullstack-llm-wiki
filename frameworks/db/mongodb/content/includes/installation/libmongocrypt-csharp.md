---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/libmongocrypt-csharp.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you're using driver version 3.0 or later:

- Install the `MongoDB.Driver.Encryption
<https://www.nuget.org/packages/MongoDB.Driver.Encryption>`__ package from NuGet. This package enables automatic encryption.

- If your application runs on Linux, :ref:`install libmongocrypt
<qe-reference-libmongocrypt>` manually. Then, set the `LIBMONGOCRYPT_PATH` environment variable to the absolute path of the `libmongocrypt` file.

- If your application runs on 64-bit Linux and you're using driver version
3.4.3 or earlier, add the following XML to your `.csproj` file.

Replace `<MongoDriverEncryptionVersion>` with the installed version of the `MongoDB.Driver.Encryption` package:

```xml
 <PropertyGroup>
     <!-- replace the version here with your package version --> 
     <MongoDriverEncryptionVersion>3.4.2</MongoDriverEncryptionVersion>
     <MongoDriverEncryptionPath>$(NuGetPackageRoot)mongodb.driver.encryption\$(MongoDriverEncryptionVersion)</MongoDriverEncryptionPath>
 </PropertyGroup>
 <PropertyGroup>
     <!-- Suppresses the duplicate file error -->
     <ErrorOnDuplicatePublishOutputFiles>false</ErrorOnDuplicatePublishOutputFiles>
 </PropertyGroup>
 <!-- Ensures the correct library after build or publish -->
 <Target Name="EnsureCorrectMongoEncryption" AfterTargets="Build;Publish" Condition="'$(RuntimeIdentifier)' != ''">
     <!-- Determine paths based on current operation -->
     <PropertyGroup>
         <_TargetDir Condition="Exists('$(PublishDir)')">$(PublishDir)</_TargetDir>
         <_TargetDir Condition="'$(_TargetDir)' == ''">$(OutputPath)</_TargetDir>
     </PropertyGroup>
     <!-- Copy the correct library based on runtime identifier (RID) -->
     <ItemGroup>
         <_CorrectMongoLib Include="$(MongoDriverEncryptionPath)/runtimes/linux/native/x64/libmongocrypt.so"
                           Condition="'$(RuntimeIdentifier)' == 'linux-x64'" />
         <_CorrectMongoLib Include="$(MongoDriverEncryptionPath)/runtimes/linux/native/arm64/libmongocrypt.so"
                           Condition="'$(RuntimeIdentifier)' == 'linux-arm64'" />
         <_CorrectMongoLib Include="$(MongoDriverEncryptionPath)/runtimes/linux/native/alpine/libmongocrypt.so"
                           Condition="'$(RuntimeIdentifier)' == 'linux-musl-arm64'" />
     </ItemGroup>
     <!-- Copy with overwrite -->
     <Copy SourceFiles="@(_CorrectMongoLib)"
           DestinationFolder="$(_TargetDir)"
           Condition="'@(_CorrectMongoLib)' != ''"
           OverwriteReadOnlyFiles="true" />
     <Message Text="Fixed MongoDB encryption library for $(RuntimeIdentifier)"
               Condition="'@(_CorrectMongoLib)' != ''" />
 </Target> 
```
