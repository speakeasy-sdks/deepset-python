# PresignedPrefix

The request configuration used for uploading files. Set each file key to `<org_id>/<workspace_id>/<session_id>/${filename}`, where filename is <file_name>.<txt|pdf> or <file_name>.<txt|pdf>.meta.json for meta files.


## Fields

| Field                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `fields`                                                                                                                                                                                                                                   | Dict[str, *str*]                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                         | The fields to include in the request to the presigned URL. These fields are required in the body of each request.                                                                                                                          | [object Object]                                                                                                                                                                                                                            |
| `url`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | The presigned URL to upload the file to. This URL was generated using the AWS ShareObjectPresignedUrl feature. To learn more, see [AWS Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html). |                                                                                                                                                                                                                                            |