# PipelineIndexingStatusDetail

Successful Response


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `failed_file_count`                                             | *int*                                                           | :heavy_check_mark:                                              | Files that failed during indexing                               |
| `indexed_file_count`                                            | *int*                                                           | :heavy_check_mark:                                              | Files that were successfully indexed.                           |
| `indexed_no_documents_file_count`                               | *int*                                                           | :heavy_check_mark:                                              | Number of files that were indexed but did not create documents. |
| `pending_file_count`                                            | *int*                                                           | :heavy_check_mark:                                              | The number of pending files to be indexed                       |
| `total_file_count`                                              | *int*                                                           | :heavy_check_mark:                                              | The total number of files assigned to a pipeline.               |