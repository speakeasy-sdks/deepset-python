# SearchQuery

Shows information about the search query which returned this result.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `created_at`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_check_mark:                                                             | Specifies when the search query was done.                                      |
| `duration`                                                                     | *float*                                                                        | :heavy_check_mark:                                                             | The number of seconds the pipeline took to find the answer.                    |
| `filters`                                                                      | [Optional[components.SearchFilters]](../../models/components/searchfilters.md) | :heavy_minus_sign:                                                             | Shows which metadata filters were used for the search query.                   |
| `query`                                                                        | *str*                                                                          | :heavy_check_mark:                                                             | The search query                                                               |
| `query_id`                                                                     | *str*                                                                          | :heavy_check_mark:                                                             | Unique identifier of the search query.                                         |
| `user`                                                                         | [components.FeedbackUser](../../models/components/feedbackuser.md)             | :heavy_check_mark:                                                             | The user who gave feedback to the search result.                               |