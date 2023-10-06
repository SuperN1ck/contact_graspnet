import pathlib
import time

import numpy as np
import tyro
from inference_class import ContactGraspNetInference


def main(archive_dir: pathlib.Path, visualize: bool=False, overwrite: bool=True):
    """
    Visualize is currently broken
    """
    assert archive_dir.exists()

    with archive_dir.open("rb") as f:
        archive = np.load(f)
        rgb_uint8 = archive["rgb"]
        depth = archive["depth"]
        depth_K = archive["intrinsic_matrix"]
        mask = archive["mask"]

    if depth.ndim == 3:
        depth = depth[..., 0]

    if mask.ndim == 3:
        mask = mask[..., 0]

    contactgraspnet = ContactGraspNetInference()

    start_time = time.time()
    pc_full, pc_colors, pred_grasps_cam, scores = contactgraspnet.predict(
        rgb_uint8, depth, depth_K, mask
    )
    inference_time = time.time() - start_time

    pred_grasps_cam = np.concatenate([arr for arr in pred_grasps_cam.values()])
    scores = np.concatenate([arr for arr in scores.values()])

    # np.save(data_path / "pc_full.npy", pc_full)
    # np.save(data_path / "pc_colors.npy", pc_colors)

    # Overwrite the results
    archive_dir_out = archive_dir.with_suffix("" if overwrite else ".out")

    with archive_dir_out.open("wb") as f: 
        np.savez(
            f,
            pred_grasps_cam=pred_grasps_cam,
            scores=scores,
            inference_time=inference_time
        )

    # Seems broken?  
    # if not visualize:
    #     return

    # contactgraspnet.visualize_results(rgb_uint8, mask, pc_full, pc_colors, pred_grasps_cam, scores)

if __name__ == "__main__":
    tyro.cli(main)
