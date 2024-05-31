# XRPL Import
from xrpl.constants import CryptoAlgorithm
from xrpl.wallet import Wallet

from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTRequest, WSRequest


class XRPLAuth(AuthBase):
    def __init__(self, xrpl_secret_key: str):
        self._xrpl_secret_key = xrpl_secret_key
        self._wallet = Wallet.from_seed(xrpl_secret_key, algorithm=self.get_algorithm())

    async def rest_authenticate(self, request: RESTRequest) -> RESTRequest:
        pass

    async def ws_authenticate(self, request: WSRequest) -> WSRequest:
        pass

    def get_wallet(self) -> Wallet:
        return self._wallet

    def get_account(self) -> str:
        return self._wallet.classic_address

    def get_algorithm(self) -> CryptoAlgorithm:
        return CryptoAlgorithm.ED25519 if self._xrpl_secret_key.startswith("sEd") else CryptoAlgorithm.SECP256K1
