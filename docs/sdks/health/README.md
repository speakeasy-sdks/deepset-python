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
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
```


### Response

**[operations.HealthHealthGetResponse](../../models/operations/healthhealthgetresponse.md)**


## get_openapi

Opens the documentation in Open API.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.health.get_openapi()

if res.redirect_get_200_application_json_any is not None:
    # handle response
```


### Response

**[operations.RedirectGetResponse](../../models/operations/redirectgetresponse.md)**

