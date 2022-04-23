from search import grid_search
import socket

if __name__ == '__main__':
    assert socket.gethostname() == 'GCRAZGDL0273'
    # gpus = [0, 1, 3, 2] * 1 + [1] * 5 + [0, 3] * 3
    # gpus = [0, 3, 2] * 2 + [0, 3] * 3
    gpus = [0] * 4
    # gpus = [1] * 5
    # config_file = "configs/AIV/LGN.yaml"
    # config_file = "configs/AIV/UmBPR.yaml"
    config_file = "configs/AIV/SmBPR.yaml"
    # config_file = "configs/AIV/UmLGN.yaml"
    # config_file = "configs/AIV/UmBPR-debug.yaml"
    grid_search(gpus, config_file)
