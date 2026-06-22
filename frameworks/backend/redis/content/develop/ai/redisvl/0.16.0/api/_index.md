---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/redisvl/0.16.0/api/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
linkTitle: RedisVL API
title: RedisVL API
weight: 5
hideListLinks: true
url: '/develop/ai/redisvl/0.16.0/api/'
---


Reference documentation for the RedisVL API.



* [Schema](schema/)
  * [IndexSchema](schema/#indexschema)
  * [Index-Level Stopwords Configuration](schema/#index-level-stopwords-configuration)
  * [Defining Fields](schema/#defining-fields)
  * [Basic Field Types](schema/#basic-field-types)
  * [Vector Field Types](schema/#vector-field-types)
  * [SVS-VAMANA Configuration Utilities](schema/#svs-vamana-configuration-utilities)
  * [Vector Algorithm Comparison](schema/#vector-algorithm-comparison)
* [Search Index Classes](searchindex/)
  * [SearchIndex](searchindex/#searchindex)
  * [AsyncSearchIndex](searchindex/#asyncsearchindex)
* [Vector](vector/)
  * [Vector](vector/#id1)
* [Query](query/)
  * [VectorQuery](query/#vectorquery)
  * [VectorRangeQuery](query/#vectorrangequery)
  * [AggregateHybridQuery](query/#aggregatehybridquery)
  * [HybridQuery](query/#hybridquery)
  * [TextQuery](query/#textquery)
  * [FilterQuery](query/#filterquery)
  * [CountQuery](query/#countquery)
  * [MultiVectorQuery](query/#multivectorquery)
  * [SQLQuery](query/#sqlquery)
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
  * [VertexAIVectorizer](vectorizer/#vertexaivectorizer)
  * [CohereTextVectorizer](vectorizer/#coheretextvectorizer)
  * [BedrockVectorizer](vectorizer/#bedrockvectorizer)
  * [CustomVectorizer](vectorizer/#customvectorizer)
  * [VoyageAIVectorizer](vectorizer/#voyageaivectorizer)
  * [MistralAITextVectorizer](vectorizer/#mistralaitextvectorizer)
* [Rerankers](reranker/)
  * [CohereReranker](reranker/#coherereranker)
  * [HFCrossEncoderReranker](reranker/#hfcrossencoderreranker)
  * [VoyageAIReranker](reranker/#voyageaireranker)
* [LLM Cache](cache/)
  * [SemanticCache](cache/#semanticcache)
  * [Cache Schema Classes](cache/#cache-schema-classes)
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
