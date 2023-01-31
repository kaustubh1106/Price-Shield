import fastapi as _fastapi
import project# as _blockchain

blockchain = project.Blockchain()
app = _fastapi.FastAPI()

@app.post("/mineblock/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The bblockchain is invalid")
    block = blockchain.mine_block(data=data)

    return block

@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="the blockchain is invalid,someone has altered the data!"
        )
    chain=blockchain.chain
    return chain