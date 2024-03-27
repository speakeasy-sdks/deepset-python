# IngestionStatus

The status of the ingestion process for this file.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `failed_files`                                       | *Optional[int]*                                      | :heavy_minus_sign:                                   | The number of files that failed to be ingested.      |
| `finished_files`                                     | *Optional[int]*                                      | :heavy_minus_sign:                                   | The number of files that were successfully ingested. |