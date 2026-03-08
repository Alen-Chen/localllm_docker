from huggingface_hub import snapshot_download

repo_id = "Qwen/Qwen2.5-Coder-7B-Instruct-AWQ"

local_dir = "./Qwen2.5-Coder-7B-Instruct-AWQ"

snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    local_dir_use_symlinks=False,
    resume_download=True
)

print("Download complete:", local_dir)
