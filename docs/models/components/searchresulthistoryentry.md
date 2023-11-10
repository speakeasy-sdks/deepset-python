# SearchResultHistoryEntry


## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `documents`                                                                                                        | List[[components.SearchResultHistoryEntryDocuments](../../models/components/searchresulthistoryentrydocuments.md)] | :heavy_check_mark:                                                                                                 | Documents that contain the search result.                                                                          |
| `rank`                                                                                                             | *Optional[int]*                                                                                                    | :heavy_minus_sign:                                                                                                 | The rank of the search result. A lower value means more relevant result.                                           |
| `result`                                                                                                           | [Optional[components.SearchResults]](../../models/components/searchresults.md)                                     | :heavy_minus_sign:                                                                                                 | List of search results.                                                                                            |
| `search_result_history_id`                                                                                         | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | List of search results.                                                                                            |
| `type`                                                                                                             | *int*                                                                                                              | :heavy_check_mark:                                                                                                 | The type of the search result. This can be either 'document' or 'answer'.                                          |