# FileWriteModeEnum

The write mode determines how to handle uploading a file if it's already in the workspace. Your options are: keep the file with the same name, make the request fail if a file with the same name already exists, or overwrite the file. If you choose to overwrite, all files with the same name are overwritten.


## Values

| Name        | Value       |
| ----------- | ----------- |
| `KEEP`      | KEEP        |
| `OVERWRITE` | OVERWRITE   |
| `FAIL`      | FAIL        |