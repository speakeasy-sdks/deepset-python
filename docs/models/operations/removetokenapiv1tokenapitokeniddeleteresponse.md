# RemoveTokenAPIV1TokenAPITokenIDDeleteResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `http_validation_error`                                                               | [Optional[shared.HTTPValidationError]](../../models/shared/httpvalidationerror.md)    | :heavy_minus_sign:                                                                    | Validation Error                                                                      |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `remove_token_api_v1_token_api_token_id_delete_200_application_json_any`              | *Optional[Any]*                                                                       | :heavy_minus_sign:                                                                    | Successful Response                                                                   |