# SessionFile


## Fields

| Field                                                                                                                    | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `file_ingestion_id`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The ID of the ingested file.                                                                                             |
| `ingestion_status`                                                                                                       | [SessionFileFileIngestionStatusEnum](../../models/shared/sessionfilefileingestionstatusenum.md)                          | :heavy_check_mark:                                                                                                       | The ingestion status of the ingested file.                                                                               |
| `ingestion_status_reason`                                                                                                | [Optional[SessionFileFileIngestionStatusReasonEnum]](../../models/shared/sessionfilefileingestionstatusreasonenum.md)    | :heavy_minus_sign:                                                                                                       | The ingestion status message that explains the ingestion status. This is only available for files that failed to ingest. |
| `name`                                                                                                                   | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The name of the ingested file.                                                                                           |