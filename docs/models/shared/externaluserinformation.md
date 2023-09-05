# ExternalUserInformation

Created a shared link for an existing external user


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `user_id`                                                                                      | *str*                                                                                          | :heavy_check_mark:                                                                             | Unique ID of the external user.                                                                |
| `user_token`                                                                                   | *str*                                                                                          | :heavy_check_mark:                                                                             | A JSON web token you can use to grant access to a set of API endpoints for this specific user. |