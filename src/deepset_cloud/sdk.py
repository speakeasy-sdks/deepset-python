"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .api_token import APIToken
from .document_store import DocumentStore
from .eval_run import EvalRun
from .evaluation_set import EvaluationSet
from .file import File
from .health import Health
from .model_registry_token import ModelRegistryToken
from .models_ import Models
from .notebook import Notebook
from .organization import Organization
from .pipeline import Pipeline
from .sdkconfiguration import SDKConfiguration
from .search_session import SearchSession
from .shared_prototype import SharedPrototype
from .upload_session import UploadSession
from .user import User
from .workspace import Workspace
from deepset_cloud import utils
from deepset_cloud._hooks import SDKHooks
from deepset_cloud.models import components
from typing import Callable, Dict, Optional, Union

class DeepsetCloud:
    r"""Deepset Cloud: deepset Cloud API description"""
    health: Health
    user: User
    models: Models
    model_registry_token: ModelRegistryToken
    notebook: Notebook
    organization: Organization
    api_token: APIToken
    workspace: Workspace
    eval_run: EvalRun
    evaluation_set: EvaluationSet
    file: File
    document_store: DocumentStore
    pipeline: Pipeline
    search_session: SearchSession
    shared_prototype: SharedPrototype
    upload_session: UploadSession

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 http_bearer: Union[Optional[str], Callable[[], Optional[str]]] = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[utils.RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param http_bearer: The http_bearer required for authentication
        :type http_bearer: Union[Optional[str], Callable[[], Optional[str]]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if callable(http_bearer):
            def security():
                return components.Security(http_bearer = http_bearer())
        else:
            security = components.Security(http_bearer = http_bearer)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.health = Health(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.models = Models(self.sdk_configuration)
        self.model_registry_token = ModelRegistryToken(self.sdk_configuration)
        self.notebook = Notebook(self.sdk_configuration)
        self.organization = Organization(self.sdk_configuration)
        self.api_token = APIToken(self.sdk_configuration)
        self.workspace = Workspace(self.sdk_configuration)
        self.eval_run = EvalRun(self.sdk_configuration)
        self.evaluation_set = EvaluationSet(self.sdk_configuration)
        self.file = File(self.sdk_configuration)
        self.document_store = DocumentStore(self.sdk_configuration)
        self.pipeline = Pipeline(self.sdk_configuration)
        self.search_session = SearchSession(self.sdk_configuration)
        self.shared_prototype = SharedPrototype(self.sdk_configuration)
        self.upload_session = UploadSession(self.sdk_configuration)
