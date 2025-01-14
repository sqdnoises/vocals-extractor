import os
import yaml
import torch
from urllib.parse import quote

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow: bool = False, indentless: bool = False):
        return super(IndentDumper, self).increase_indent(flow, False)

def tuple_constructor(loader, node) -> tuple:
    values = loader.construct_sequence(node)
    return tuple(values)

# Register the constructor with PyYAML
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/tuple", tuple_constructor)

def conf_edit(config_path: str, chunk_size: int, overlap: int) -> None:
    with open(config_path, "r") as f:
        data: dict = yaml.load(f, Loader=yaml.SafeLoader)
    
    # handle cases where "use_amp" is missing from config:
    if "use_amp" not in data.keys():
      data["training"]["use_amp"] = True
      
    data["audio"]["chunk_size"] = chunk_size
    data["inference"]["num_overlap"] = overlap
    
    if data["inference"]["batch_size"] == 1:
        data["inference"]["batch_size"] = 2
    
    print("Using custom overlap and chunk_size values:")
    print(f"overlap = {data['inference']['num_overlap']}")
    print(f"chunk_size = {data['audio']['chunk_size']}")
    print(f"batch_size = {data['inference']['batch_size']}")
    
    with open(config_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, Dumper=IndentDumper, allow_unicode=True)

def download_file(url: str, path: str = ".") -> str:
    # Encode the URL to handle spaces and special characters
    encoded_url = quote(url, safe=":/")
    
    os.makedirs(path, exist_ok=True)
    filename = os.path.basename(encoded_url)
    file_path = os.path.abspath(os.path.join(path, filename))
    
    if os.path.exists(file_path):
        print(f"File '{filename}' already exists at '{os.path.abspath(path)}'.")
        return file_path
    
    try:
        torch.hub.download_url_to_file(encoded_url, file_path)
        print(f"File '{filename}' downloaded successfully")
    except Exception as e:
        print(f"Error downloading file '{filename}' from '{url}': {e}")
    
    return file_path