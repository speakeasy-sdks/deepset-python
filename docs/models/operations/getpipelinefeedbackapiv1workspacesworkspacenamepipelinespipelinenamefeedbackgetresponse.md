# GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetResponse


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                             | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `http_validation_error`                                                                                    | [Optional[shared.HTTPValidationError]](../../models/shared/httpvalidationerror.md)                         | :heavy_minus_sign:                                                                                         | Validation Error                                                                                           |
| `response_200_get_pipeline_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_get` | *Optional[Any]*                                                                                            | :heavy_minus_sign:                                                                                         | The CSV file with the collected feedback                                                                   |
| `status_code`                                                                                              | *int*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `raw_response`                                                                                             | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                      | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |