# SessionDetail


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `documentation_url`                                                          | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The URL to the documentation of the session.                                 |
| `expires_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_check_mark:                                                           | The time when the session expires.                                           |
| `ingestion_status`                                                           | [components.FileIngestionStatus](../../models/shared/fileingestionstatus.md) | :heavy_check_mark:                                                           | The status of the ingestion process for this file.                           |
| `session_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | Unique identifier of a session.                                              |