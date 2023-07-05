# CreateTagAPIV1WorkspacesWorkspaceNameTagsPostResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `create_tag_response`                                                                 | [Optional[shared.CreateTagResponse]](../../models/shared/createtagresponse.md)        | :heavy_minus_sign:                                                                    | Successful Response                                                                   |
| `http_validation_error`                                                               | [Optional[shared.HTTPValidationError]](../../models/shared/httpvalidationerror.md)    | :heavy_minus_sign:                                                                    | Validation Error                                                                      |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |