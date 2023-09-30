# Token


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `api_token_id`                                                                  | *Optional[str]*                                                                 | :heavy_check_mark:                                                              | Unique identifier of the API token.                                             |
| `expires_at`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)            | :heavy_check_mark:                                                              | Timestamp when the token should expire, for example '2022-05-12T12:25:09+02:00' |
| `user`                                                                          | [Optional[shared.UserName]](undefined/models/shared/username.md)                | :heavy_check_mark:                                                              | N/A                                                                             |