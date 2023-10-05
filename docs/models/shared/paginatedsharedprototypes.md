# PaginatedSharedPrototypes


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `data`                                                                     | list[[shared.SharedPrototype](undefined/models/shared/sharedprototype.md)] | :heavy_check_mark:                                                         | A list of matching shared prototypes.                                      |
| `has_more`                                                                 | *Optional[bool]*                                                           | :heavy_check_mark:                                                         | Whether the paginated result has more results.                             |
| `total`                                                                    | *Optional[int]*                                                            | :heavy_check_mark:                                                         | The total number of results matching your query.                           |