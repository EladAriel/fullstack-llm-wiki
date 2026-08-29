---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/redisvl/0.8.1/api/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.904780Z"
---
# _Index

---
linkTitle: RedisVL API
title: RedisVL API
weight: 5
hideListLinks: true
url: '/develop/ai/redisvl/0.8.1/api/'
---


Reference documentation for the RedisVL API.



* [Schema](schema/)
  * [IndexSchema](schema/#indexschema)
  * [Defining Fields](schema/#defining-fields)
  * [Supported Field Types and Attributes](schema/#supported-field-types-and-attributes)
* [Search Index Classes](searchindex/)
  * [SearchIndex](searchindex/#searchindex)
  * [AsyncSearchIndex](searchindex/#asyncsearchindex)
* [Query](query/)
  * [VectorQuery](query/#vectorquery)
  * [VectorRangeQuery](query/#vectorrangequery)
  * [HybridQuery](query/#hybridquery)
  * [TextQuery](query/#textquery)
  * [FilterQuery](query/#filterquery)
  * [CountQuery](query/#countquery)
* [Filter](filter/)
  * [FilterExpression](filter/#filterexpression)
  * [Tag](filter/#tag)
  * [Text](filter/#text)
  * [Num](filter/#num)
  * [Geo](filter/#geo)
  * [GeoRadius](filter/#georadius)
* [Vectorizers](vectorizer/)
  * [HFTextVectorizer](vectorizer/#hftextvectorizer)
  * [OpenAITextVectorizer](vectorizer/#openaitextvectorizer)
  * [AzureOpenAITextVectorizer](vectorizer/#azureopenaitextvectorizer)
  * [VertexAITextVectorizer](vectorizer/#vertexaitextvectorizer)
  * [CohereTextVectorizer](vectorizer/#coheretextvectorizer)
  * [BedrockTextVectorizer](vectorizer/#bedrocktextvectorizer)
  * [CustomTextVectorizer](vectorizer/#customtextvectorizer)
  * [VoyageAITextVectorizer](vectorizer/#voyageaitextvectorizer)
* [Rerankers](reranker/)
  * [CohereReranker](reranker/#coherereranker)
  * [HFCrossEncoderReranker](reranker/#hfcrossencoderreranker)
  * [VoyageAIReranker](reranker/#voyageaireranker)
* [LLM Cache](cache/)
  * [SemanticCache](cache/#semanticcache)
* [Embeddings Cache](cache/#embeddings-cache)
  * [EmbeddingsCache](cache/#embeddingscache)
* [LLM Message History](message_history/)
  * [SemanticMessageHistory](message_history/#semanticmessagehistory)
  * [MessageHistory](message_history/#messagehistory)
* [Semantic Router](router/)
  * [Semantic Router](router/#semantic-router-api)
  * [Routing Config](router/#routing-config)
  * [Route](router/#route)
  * [Route Match](router/#route-match)
  * [Distance Aggregation Method](router/#distance-aggregation-method)
