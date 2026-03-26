from huggingface_hub import hf_hub_download

# Replace with the model repo and GGUF filename you want
repo_id = "mradermacher/MiniMax-M2.5-REAP-172B-A10B-i1-GGUF"
filename = "MiniMax-M2.5-REAP-172B-A10B.i1-Q4_K_M.gguf"

# Download file
file_path = hf_hub_download(
  repo_id=repo_id,
  filename=filename,
  local_dir="./models",
  local_dir_use_symlinks=False
)

print(f"Downloaded to: {file_path}")
