from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="preetlalli/llama-2-7B",
    token="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",
    local_dir="llama-2-7B",
)
