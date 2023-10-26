# PipelineFieldSearchResult


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `data`                                           | List[*str*]                                      | :heavy_check_mark:                               | A list of fields that you searched for.          |
| `has_more`                                       | *bool*                                           | :heavy_check_mark:                               | Whether the paginated result has more results.   |
| `total`                                          | *int*                                            | :heavy_check_mark:                               | The total number of results matching your query. |