from etherscan.blocks import Blocks

key=""

api = Blocks(api_key=key)
reward = api.get_block_reward(2165403)
print(reward)