"""OLAS API SERVER using flask"""
import json
import os
import time
from pathlib import Path

from flask import Flask, jsonify
from flask_caching import Cache
from web3 import Web3

app = Flask(__name__)

# Cache configuration
app.config["CACHE_TYPE"] = "simple"
cache = Cache(app)

# Connect to Ethereum node (using Infura as an example)
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
w3 = Web3(Web3.HTTPProvider(f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"))

# Replace with your contract's ABI and address
OLAS_CONTRACT_ADDRESS = "0x0001A500A6B18995B03f44bb040A5fFc28E45CB0"
VEOLAS_CONTRACT_ADDRESS = "0x7e01A500805f8A52Fad229b3015AD130A332B7b3"
BUOLAS_CONTRACT_ADDRESS = "0xb09CcF0Dbf0C178806Aaee28956c74bd66d21f73"
VALORY_MULTISIG_ADDRESS = "0x87cc0d34f6111c8A7A4Bdf758a9a715A3675f941"
TIMELOCK_ADDRESS = "0x3C1fF68f5aa342D296d4DEe4Bb1cACCA912D95fE"

# Load ABI from a file
OLAS_CONTRACT_ABI = json.loads(Path("olas_abi.json").read_text(encoding="utf-8"))

olas_contract = w3.eth.contract(  # type: ignore
    address=OLAS_CONTRACT_ADDRESS, abi=OLAS_CONTRACT_ABI
)

# Cache timeout (e.g., 10 minutes)
CACHE_TIMEOUT = 600


@app.route("/circulating_supply", methods=["GET"])
@cache.cached(timeout=CACHE_TIMEOUT)
def get_circulating_supply():
    """Get circulating suply api endpoint."""
    total_supply = olas_contract.functions.totalSupply().call()
    veolas_total_supply = olas_contract.functions.balanceOf(
        VEOLAS_CONTRACT_ADDRESS
    ).call()
    buolas_total_supply = olas_contract.functions.balanceOf(
        BUOLAS_CONTRACT_ADDRESS
    ).call()
    valory_multisig = olas_contract.functions.balanceOf(VALORY_MULTISIG_ADDRESS).call()
    timelock = olas_contract.functions.balanceOf(TIMELOCK_ADDRESS).call()
    circulating_supply = (
        total_supply
        - veolas_total_supply
        - buolas_total_supply
        - valory_multisig
        - timelock
    )

    response = {
        "success": True,
        "data": {
            "circulatingSupply": str(circulating_supply),
            "token": "OLAS",
            "decimals": 18,
        },
        "generatedTimeMs": int(time.time() * 1000),  # Current time in milliseconds
    }
    return jsonify(response)


@app.route("/circulating_supply_simple", methods=["GET"])
@cache.cached(timeout=CACHE_TIMEOUT)
def get_circulating_supply_simple():
    """Get circulating suply api endpoint."""
    total_supply = olas_contract.functions.totalSupply().call()
    veolas_total_supply = olas_contract.functions.balanceOf(
        VEOLAS_CONTRACT_ADDRESS
    ).call()
    buolas_total_supply = olas_contract.functions.balanceOf(
        BUOLAS_CONTRACT_ADDRESS
    ).call()
    valory_multisig = olas_contract.functions.balanceOf(VALORY_MULTISIG_ADDRESS).call()
    timelock = olas_contract.functions.balanceOf(TIMELOCK_ADDRESS).call()
    circulating_supply = (
        total_supply
        - veolas_total_supply
        - buolas_total_supply
        - valory_multisig
        - timelock
    )

    circulating_supply_decimals = circulating_supply / 10**18
    return str(circulating_supply_decimals)


@app.route("/total_supply", methods=["GET"])
@cache.cached(timeout=CACHE_TIMEOUT)
def get_total_supply():
    """Get total suply api endpoint."""
    total_supply = olas_contract.functions.totalSupply().call()
    response = {
        "success": True,
        "data": {
            "totalSupply": str(total_supply),
            "token": "OLAS",
            "decimals": 18,
        },
        "generatedTimeMs": int(time.time() * 1000),  # Current time in milliseconds
    }
    return jsonify(response)


@app.route("/total_supply_simple", methods=["GET"])
@cache.cached(timeout=CACHE_TIMEOUT)
def get_total_supply_simple():
    """Get total suply api endpoint."""
    total_supply = olas_contract.functions.totalSupply().call()
    total_supply_decimals = total_supply / 10**18
    return str(total_supply_decimals)


@app.route("/check", methods=["GET"])
def check():
    """Simple health check."""
    return jsonify({"check": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
