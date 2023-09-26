# ModelRegistryToken


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `invalid`                                         | *bool*                                            | :heavy_check_mark:                                | Signals whether the token is invalid.             |
| `model_registry_token_id`                         | *str*                                             | :heavy_check_mark:                                | Unique identifier of the model registry token     |
| `provider`                                        | *str*                                             | :heavy_check_mark:                                | Model provider, for example huggingface           |
| `provider_domain`                                 | *str*                                             | :heavy_check_mark:                                | Model provider domain, for example huggingface.co |