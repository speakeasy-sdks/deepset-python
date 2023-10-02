# LogEntry


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The date and time when the log entry was created.                    |
| `level`                                                              | *Optional[str]*                                                      | :heavy_check_mark:                                                   | The log level. Can be one of 'error', 'warning', 'info', 'debug'.    |
| `msg`                                                                | *Optional[str]*                                                      | :heavy_check_mark:                                                   | The log message.                                                     |