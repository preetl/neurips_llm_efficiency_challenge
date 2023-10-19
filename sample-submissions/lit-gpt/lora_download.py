from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="preetlalli/llama-3b-lora",
    token="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",
    local_dir="open-llama-3b",
)
