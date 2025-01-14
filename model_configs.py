import os

configs = {
    "VOCALS-InstVocHQ": {
        "model_type": "mdx23c",
        "config_path": "config_vocals_mdx23c.yaml",
        "start_check_point": "model_vocals_mdx23c_sdr_10.17.ckpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.0/model_vocals_mdx23c_sdr_10.17.ckpt",
            "config": "https://raw.githubusercontent.com/ZFTurbo/Music-Source-Separation-Training/main/configs/config_vocals_mdx23c.yaml"
        },
        "needs_config_edit": False
    },
    "VOCALS-MelBand-Roformer (by Becruily)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_vocals_becruily.yaml",
        "start_check_point": "mel_band_roformer_vocals_becruily.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/becruily/mel-band-roformer-vocals/resolve/main/mel_band_roformer_vocals_becruily.ckpt",
            "config": "https://huggingface.co/becruily/mel-band-roformer-vocals/resolve/main/config_vocals_becruily.yaml"
        },
        "needs_config_edit": True
    },
    "INST-MelBand-Roformer (by Becruily)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_instrumental_becruily.yaml",
        "start_check_point": "mel_band_roformer_instrumental_becruily.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/becruily/mel-band-roformer-instrumental/resolve/main/mel_band_roformer_instrumental_becruily.ckpt",
            "config": "https://huggingface.co/becruily/mel-band-roformer-instrumental/resolve/main/config_instrumental_becruily.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-MelBand-Roformer (by KimberleyJSN)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_vocals_mel_band_roformer_kj.yaml",
        "start_check_point": "MelBandRoformer.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/KimberleyJSN/melbandroformer/resolve/main/MelBandRoformer.ckpt",
            "config": "https://raw.githubusercontent.com/ZFTurbo/Music-Source-Separation-Training/main/configs/KimberleyJensen/config_vocals_mel_band_roformer_kj.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-MelBand-Roformer Kim FT (by Unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_kimmel_unwa_ft.yaml",
        "start_check_point": "kimmel_unwa_ft.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Kim-Mel-Band-Roformer-FT/resolve/main/kimmel_unwa_ft.ckpt",
            "config": "https://huggingface.co/pcunwa/Kim-Mel-Band-Roformer-FT/resolve/main/config_kimmel_unwa_ft.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-BS-Roformer_1297 (by viperx)": {
        "model_type": "bs_roformer",
        "config_path": "model_bs_roformer_ep_317_sdr_12.9755.yaml",
        "start_check_point": "model_bs_roformer_ep_317_sdr_12.9755.ckpt",
        "urls": {
            "ckpt": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/model_bs_roformer_ep_317_sdr_12.9755.ckpt",
            "config": "https://raw.githubusercontent.com/ZFTurbo/Music-Source-Separation-Training/main/configs/viperx/model_bs_roformer_ep_317_sdr_12.9755.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-BS-Roformer_1296 (by viperx)": {
        "model_type": "bs_roformer",
        "config_path": "model_bs_roformer_ep_368_sdr_12.9628.yaml",
        "start_check_point": "model_bs_roformer_ep_368_sdr_12.9628.ckpt",
        "urls": {
            "ckpt": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/model_bs_roformer_ep_368_sdr_12.9628.ckpt",
            "config": "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/mdx_c_configs/model_bs_roformer_ep_368_sdr_12.9628.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-BS-RoformerLargev1 (by unwa)": {
        "model_type": "bs_roformer",
        "config_path": "config_bsrofoL.yaml",
        "start_check_point": "BS-Roformer_LargeV1.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/jarredou/unwa_bs_roformer/resolve/main/BS-Roformer_LargeV1.ckpt",
            "config": "https://huggingface.co/jarredou/unwa_bs_roformer/raw/main/config_bsrofoL.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-Melband-Roformer BigBeta5e (by unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "big_beta5e.yaml",
        "start_check_point": "big_beta5e.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Mel-Band-Roformer-big/resolve/main/big_beta5e.ckpt",
            "config": "https://huggingface.co/pcunwa/Mel-Band-Roformer-big/resolve/main/big_beta5e.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-Mel-Roformer big beta 4 (by unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_melbandroformer_big_beta4.yaml",
        "start_check_point": "melband_roformer_big_beta4.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Mel-Band-Roformer-big/resolve/main/melband_roformer_big_beta4.ckpt",
            "config": "https://huggingface.co/pcunwa/Mel-Band-Roformer-big/raw/main/config_melbandroformer_big_beta4.yaml"
        },
        "needs_config_edit": True
    },
    "INST-Mel-Roformer v1 (by unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_melbandroformer_inst.yaml",
        "start_check_point": "melband_roformer_inst_v1.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst/resolve/main/melband_roformer_inst_v1.ckpt",
            "config": "https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst/raw/main/config_melbandroformer_inst.yaml"
        },
        "needs_config_edit": True
    },
    "INST-Mel-Roformer v2 (by unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_melbandroformer_inst_v2.yaml",
        "start_check_point": "melband_roformer_inst_v2.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst/resolve/main/melband_roformer_inst_v2.ckpt",
            "config": "https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst/raw/main/config_melbandroformer_inst_v2.yaml"
        },
        "needs_config_edit": True
    },
    "INST-Mel-Roformer v1e (by unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_melbandroformer_inst.yaml",
        "start_check_point": "inst_v1e.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst/resolve/main/inst_v1e.ckpt",
            "config": "https://huggingface.co/pcunwa/Mel-Band-Roformer-Inst/raw/main/config_melbandroformer_inst.yaml"
        },
        "needs_config_edit": True
    },
    "INST-VOC-Mel-Roformer a.k.a. duality (by unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_melbandroformer_instvoc_duality.yaml",
        "start_check_point": "melband_roformer_instvoc_duality_v1.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Mel-Band-Roformer-InstVoc-Duality/resolve/main/melband_roformer_instvoc_duality_v1.ckpt",
            "config": "https://huggingface.co/pcunwa/Mel-Band-Roformer-InstVoc-Duality/raw/main/config_melbandroformer_instvoc_duality.yaml"
        },
        "needs_config_edit": True
    },
    "INST-VOC-Mel-Roformer a.k.a. duality v2 (by unwa)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_melbandroformer_instvoc_duality.yaml",
        "start_check_point": "melband_roformer_instvox_duality_v2.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/pcunwa/Mel-Band-Roformer-InstVoc-Duality/resolve/main/melband_roformer_instvox_duality_v2.ckpt",
            "config": "https://huggingface.co/pcunwa/Mel-Band-Roformer-InstVoc-Duality/raw/main/config_melbandroformer_instvoc_duality.yaml"
        },
        "needs_config_edit": True
    },
    "KARAOKE-MelBand-Roformer (by aufr33 & viperx)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_mel_band_roformer_karaoke.yaml",
        "start_check_point": "mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/jarredou/aufr33-viperx-karaoke-melroformer-model/resolve/main/mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt",
            "config": "https://huggingface.co/jarredou/aufr33-viperx-karaoke-melroformer-model/resolve/main/config_mel_band_roformer_karaoke.yaml"
        },
        "needs_config_edit": True
    },
    "OTHER-BS-Roformer_1053 (by viperx)": {
        "model_type": "bs_roformer",
        "config_path": "model_bs_roformer_ep_937_sdr_10.5309.yaml",
        "start_check_point": "model_bs_roformer_ep_937_sdr_10.5309.ckpt",
        "urls": {
            "ckpt": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/model_bs_roformer_ep_937_sdr_10.5309.ckpt",
            "config": "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/mdx_c_configs/model_bs_roformer_ep_937_sdr_10.5309.yaml"
        },
        "needs_config_edit": True
    },
    "CROWD-REMOVAL-MelBand-Roformer (by aufr33)": {
        "model_type": "mel_band_roformer",
        "config_path": "model_mel_band_roformer_crowd.yaml",
        "start_check_point": "mel_band_roformer_crowd_aufr33_viperx_sdr_8.7144.ckpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v.1.0.4/mel_band_roformer_crowd_aufr33_viperx_sdr_8.7144.ckpt",
            "config": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v.1.0.4/model_mel_band_roformer_crowd.yaml"
        },
        "needs_config_edit": True
    },
    "VOCALS-VitLarge23 (by ZFTurbo)": {
        "model_type": "segm_models",
        "config_path": "config_vocals_segm_models.yaml",
        "start_check_point": "model_vocals_segm_models_sdr_9.77.ckpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.0/model_vocals_segm_models_sdr_9.77.ckpt",
            "config": "https://raw.githubusercontent.com/ZFTurbo/Music-Source-Separation-Training/refs/heads/main/configs/config_vocals_segm_models.yaml"
        },
        "needs_config_edit": False
    },
    "CINEMATIC-BandIt_Plus (by kwatcharasupat)": {
        "model_type": "bandit",
        "config_path": "config_dnr_bandit_bsrnn_multi_mus64.yaml",
        "start_check_point": "model_bandit_plus_dnr_sdr_11.47.chpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.0/model_vocals_segm_models_sdr_9.77.ckpt",
            "config": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v.1.0.3/config_dnr_bandit_bsrnn_multi_mus64.yaml"
        },
        "needs_config_edit": False
    },
    "DRUMSEP-MDX23C_DrumSep_6stem (by aufr33 & jarredou)": {
        "model_type": "mdx23c",
        "config_path": "aufr33-jarredou_DrumSep_model_mdx23c_ep_141_sdr_10.8059.yaml",
        "start_check_point": "aufr33-jarredou_DrumSep_model_mdx23c_ep_141_sdr_10.8059.ckpt",
        "urls": {
            "ckpt": "https://github.com/jarredou/models/releases/download/aufr33-jarredou_MDX23C_DrumSep_model_v0.1/aufr33-jarredou_DrumSep_model_mdx23c_ep_141_sdr_10.8059.ckpt",
            "config": "https://github.com/jarredou/models/releases/download/aufr33-jarredou_MDX23C_DrumSep_model_v0.1/aufr33-jarredou_DrumSep_model_mdx23c_ep_141_sdr_10.8059.yaml"
        },
        "needs_config_edit": False
    },
    "4STEMS-SCNet_XL_MUSDB18 (by ZFTurbo)": {
        "model_type": "scnet",
        "config_path": "config_musdb18_scnet_xl.yaml",
        "start_check_point": "model_scnet_ep_54_sdr_9.8051.ckpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.13/model_scnet_ep_54_sdr_9.8051.ckpt",
            "config": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.13/config_musdb18_scnet_xl.yaml"
        },
        "needs_config_edit": False
    },
    "4STEMS-SCNet_Large (by starrytong)": {
        "model_type": "scnet",
        "config_path": "config_musdb18_scnet_large_starrytong.yaml",
        "start_check_point": "SCNet-large_starrytong_fixed.ckpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.9/SCNet-large_starrytong_fixed.ckpt",
            "config": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.9/config_musdb18_scnet_large_starrytong.yaml"
        },
        "needs_config_edit": False
    },
    "4STEMS-SCNet_MUSDB18 (by starrytong)": {
        "model_type": "scnet",
        "config_path": "config_musdb18_scnet.yaml",
        "start_check_point": "scnet_checkpoint_musdb18.ckpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v.1.0.6/scnet_checkpoint_musdb18.ckpt",
            "config": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v.1.0.6/config_musdb18_scnet.yaml"
        },
        "needs_config_edit": False
    },
    "4STEMS-BS-Roformer_MUSDB18 (by ZFTurbo)": {
        "model_type": "bs_roformer",
        "config_path": "config_bs_roformer_384_8_2_485100.yaml",
        "start_check_point": "model_bs_roformer_ep_17_sdr_9.6568.ckpt",
        "urls": {
            "ckpt": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.12/model_bs_roformer_ep_17_sdr_9.6568.ckpt",
            "config": "https://github.com/ZFTurbo/Music-Source-Separation-Training/releases/download/v1.0.12/config_bs_roformer_384_8_2_485100.yaml"
        },
        "needs_config_edit": True
    },
    "DE-REVERB-MDX23C (by aufr33 & jarredou)": {
        "model_type": "mdx23c",
        "config_path": "config_dereverb_mdx23c.yaml",
        "start_check_point": "dereverb_mdx23c_sdr_6.9096.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/jarredou/aufr33_jarredou_MDXv3_DeReverb/resolve/main/dereverb_mdx23c_sdr_6.9096.ckpt",
            "config": "https://huggingface.co/jarredou/aufr33_jarredou_MDXv3_DeReverb/resolve/main/config_dereverb_mdx23c.yaml"
        },
        "needs_config_edit": False
    },
    "DE-REVERB-MelBand-Roformer aggr./v2/19.1729 (by anvuew)": {
        "model_type": "mel_band_roformer",
        "config_path": "dereverb_mel_band_roformer_anvuew.yaml",
        "start_check_point": "dereverb_mel_band_roformer_anvuew_sdr_19.1729.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/anvuew/dereverb_mel_band_roformer/resolve/main/dereverb_mel_band_roformer_anvuew_sdr_19.1729.ckpt",
            "config": "https://huggingface.co/anvuew/dereverb_mel_band_roformer/resolve/main/dereverb_mel_band_roformer_anvuew.yaml"
        },
        "needs_config_edit": True
    },
    "DE-REVERB-Echo-MelBand-Roformer (by Sucial)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_dereverb-echo_mel_band_roformer.yaml",
        "start_check_point": "dereverb-echo_mel_band_roformer_sdr_10.0169.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/Sucial/Dereverb-Echo_Mel_Band_Roformer/resolve/main/dereverb-echo_mel_band_roformer_sdr_10.0169.ckpt",
            "config": "https://huggingface.co/Sucial/Dereverb-Echo_Mel_Band_Roformer/resolve/main/config_dereverb-echo_mel_band_roformer.yaml"
        },
        "needs_config_edit": True
    },
    "DENOISE-MelBand-Roformer-1 (by aufr33)": {
        "model_type": "mel_band_roformer",
        "config_path": "model_mel_band_roformer_denoise.yaml",
        "start_check_point": "denoise_mel_band_roformer_aufr33_sdr_27.9959.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/jarredou/aufr33_MelBand_Denoise/resolve/main/denoise_mel_band_roformer_aufr33_sdr_27.9959.ckpt",
            "config": "https://huggingface.co/jarredou/aufr33_MelBand_Denoise/resolve/main/model_mel_band_roformer_denoise.yaml"
        },
        "needs_config_edit": True
    },
    "DENOISE-MelBand-Roformer-2 (by aufr33)": {
        "model_type": "mel_band_roformer",
        "config_path": "model_mel_band_roformer_denoise.yaml",
        "start_check_point": "denoise_mel_band_roformer_aufr33_aggr_sdr_27.9768.ckpt",
        "urls": {
            "ckpt": "https://huggingface.co/jarredou/aufr33_MelBand_Denoise/resolve/main/denoise_mel_band_roformer_aufr33_aggr_sdr_27.9768.ckpt",
            "config": "https://huggingface.co/jarredou/aufr33_MelBand_Denoise/resolve/main/model_mel_band_roformer_denoise.yaml"
        },
        "needs_config_edit": True
    },
    "DEBLEED-MelBand-Roformer (by unwa/97chris)": {
        "model_type": "mel_band_roformer",
        "config_path": "config_bleed_suppressor_v1.yaml",
        "start_check_point": "bleed_suppressor_v1.ckpt",
        "urls": {
            "ckpt": "https://shared.multimedia.workers.dev/download/1/other/bleed_suppressor_v1.ckpt",
            "config": "https://shared.multimedia.workers.dev/download/1/other/config_bleed_suppressor_v1.yaml"
        },
        "needs_config_edit": True
    }
}

def get_model_config(model_name: str, path: str | None = None):
    """
    Returns model configuration based on the model name.
    Returns: (model_type, config_path, start_check_point, config_urls)
    """
    
    if model_name not in configs:
        raise ValueError(f"Model {model_name} not found in configurations")
    
    if path:
        configs[model_name]["config_path"]       = os.path.join(path, configs[model_name]["config_path"])
        configs[model_name]["start_check_point"] = os.path.join(path, configs[model_name]["start_check_point"])
    
    return configs[model_name]