# CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostResponse


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `content_type`                                                                             | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `external_user_information`                                                                | [Optional[shared.ExternalUserInformation]](../../models/shared/externaluserinformation.md) | :heavy_minus_sign:                                                                         | Created a shared link for an existing external user                                        |
| `http_validation_error`                                                                    | [Optional[shared.HTTPValidationError]](../../models/shared/httpvalidationerror.md)         | :heavy_minus_sign:                                                                         | Validation Error                                                                           |
| `status_code`                                                                              | *int*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `raw_response`                                                                             | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)      | :heavy_minus_sign:                                                                         | N/A                                                                                        |