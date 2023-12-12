# Health
(*health*)

### Available Operations

* [check](#check) - Health
* [get_openapi](#get_openapi) - Redirect

## check

Checks if the API works correctly.

### Example Usage

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
    pass
```


### Response

**[operations.HealthHealthGetResponse](../../models/operations/healthhealthgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_openapi

Opens the documentation in Open API.

### Example Usage

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.health.get_openapi()

if res.any is not None:
    # handle response
    pass
```


### Response

**[operations.RedirectGetResponse](../../models/operations/redirectgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
