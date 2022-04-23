from search import grid_search
from tools.config import load_specific_config
from trainer import wrap
import socket

if __name__ == '__main__':
    assert socket.gethostname() == 'dell-PowerEdge-T640'
    # config_file = "configs/LastFM/config-ALastFM-BPR+ELCB-OLT.yaml"
    # config_file = "configs/AIV/config-AIV-GMF+ELCB-MN-OLT.yaml"
    # config_file = "configs/LastFM/config-ALastFM-GMF+ELCB-MN-OLT.yaml"
    # config_file = "configs/ML1M/config-GMF+ELCB+MN-ML1M-OLT.yaml"
    # config_file = "configs/ML10M/config-ML10M-GMF+ELCB+MN-OLT.yaml"
    # config_file = "configs/AIV/config-AIV-GMF-OLT.yaml"
    # config_file = "configs/LastFM/config-ALastFM-GMF-OLT.yaml"
    # config_file = "configs/ML1M/config-GMF-ML1M-OLT.yaml"
    config_file = "configs/ML10M/config-ML10M-GMF-OLT.yaml"
    cfg = load_specific_config(config_file)
    cfg['cuda'] = "1"
    cfg['analysis/record_boundary'] = True
    cfg['log_folder'] = 'logs_analysis'
    cfg['evaluator_args/checkpoint_save'] = True
    # cfg['analysis/record_corrupted'] = True
    # cfg['model/boundary_as_zero'] = True
    # cfg['evaluator_time'] = 100

    gpus = [0, 1, 2, 3] * 2
    # gpus = [0, 1, 2, 3] * 5 + [0] * 5
    wrap(cfg)
    # grid_search(gpus, cfg)

