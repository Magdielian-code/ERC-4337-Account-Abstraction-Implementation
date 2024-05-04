from mnemonic import Mnemonic

# Generate a new mnemonic phrase with 12 words
mnemonic = Mnemonic("english").generate(128)  # 128-bit strength for 12 words