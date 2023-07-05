# SearchResult

Returns the search results.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `query_id`                                                                          | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The search query                                                                    |
| `results`                                                                           | list[[DeepsetCloudQueryResponse](../../models/shared/deepsetcloudqueryresponse.md)] | :heavy_check_mark:                                                                  | List of search results.                                                             |