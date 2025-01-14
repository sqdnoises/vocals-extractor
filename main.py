import os
import sys
import subprocess
from config_utils import conf_edit, download_file
from model_configs import get_model_config

def main():
    # Configuration parameters
    input_folder = "input"
    output_folder = "output"
    ckpts_folder = "Music-Source-Separation-Training/ckpts"
    model = "VOCALS-MelBand-Roformer (by KimberleyJSN)"
    extract_instrumental = True
    export_format = "flac PCM_16"
    use_tta = False
    overlap = 2
    chunk_size = 485100
    
    # Process export format
    input_folder = os.path.abspath(input_folder)
    output_folder = os.path.abspath(output_folder)
    flac_file = export_format.startswith("flac")
    pcm_type = export_format.split(" ")[1] if flac_file else None
    
    try:
        # Get model configuration
        model_config = get_model_config(model)
        model_type = model_config["model_type"]
        
        # Download necessary files
        config_path = download_file(model_config["urls"]["config"], ckpts_folder)
        ckpt_path = download_file(model_config["urls"]["ckpt"], ckpts_folder)
        
        # Edit configuration if needed
        if model_config["needs_config_edit"]:
            conf_edit(config_path, chunk_size, overlap)
        
        # Prepare command arguments as a list
        cmd_args = [
            f"--model_type", model_type,
            f'--config_path', config_path,
            f'--start_check_point', ckpt_path,
            f'--input_folder', input_folder,
            f'--store_dir', output_folder
        ]
        
        if extract_instrumental:
            cmd_args.append("--extract_instrumental")
        if flac_file:
            cmd_args.append("--flac_file")
        if use_tta:
            cmd_args.append("--use_tta")
        if pcm_type:
             cmd_args.extend(["--pcm_type", pcm_type])
        
        # Execute inference command
        print("Executing inference command...")
        os.chdir("Music-Source-Separation-Training")
        inference_command = [sys.executable, "inference.py"] + cmd_args
        subprocess.run(inference_command, check=True) # Runs the command
    
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()