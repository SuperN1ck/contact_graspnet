# Installation

## Get the code
```bash
git clone git@github.com:SuperN1ck/contact_graspnet.git -b inference_single_file
git clone git@github.com:chisarie/uois.git -b inference
```

## Original Installation
```bash
cd contact_graspnet
conda env create -f contact_graspnet_env.yml --prefix ./env 
conda activate ./env
pip install scikit-image torch==1.5.1 torch torchvision==0.6.1
```

## Updated Version
Most importantly to install the correct tensorflow version with your CUDA version. Below was tested with CUDA Toolkit version `11.7`, i.e. this is what is needed for `tensorflow==2.9`

```[bash]
conda create --prefix ./env python=3.8 -y
conda activate ./env
pip install tensorflow==2.9 tensorflow-gpu==2.9 opencv-python-headless pyyaml==5.4.1 pyrender tqdm mayavi pyqt5 scikit-image tyro open3d 
pip install git+https://github.com/SuperN1ck/casino.git
pip install torch==2.0.1+cu117 torchvision==0.15.2+cu117 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu117
pip install -e ../uois
```

### "Installing" a different CUDA version into a conda environment
Create an `etc` file
```[bash]
mkdir -p env/etc/conda/
```
And create two files
```[bash]
> cat env/etc/conda/activate.d/env_vars.sh 
#!/bin/sh

export PATH_BAK=$PATH
export LD_LIBRARY_PATH_BAK=$LD_LIBRARY_PATH
export LIBRARY_PATH_BAK=$LIBRARY_PATH

export CUDA_HOME=/usr/local/cuda-11.7 # UPDATE HERE IF NOT USING 11.7
export PATH=$CUDA_HOME/bin:$CUDA_HOME/include:$CUDA_HOME/lib:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
export LIBRARY_PATH=$CUDA_HOME/lib64:$LIBRARY_PATH
```
And
```
> cat env/etc/conda/deactivate.d/env_vars.sh 
#!/bin/sh

export PATH="$PATH_BAK"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH_BAK"
export LIBRARY_PATH="$LIBRARY_PATH_BAK"
```

## Post-Install
After you have successfully create a env, don't forget to recompile `pointnet2 tf_ops`:
```bash
sh compile_pointnet_tfops.sh
```
*If you use a different CUDA Toolkit version other than `11.7`, make sure to update it in `compile_pointnet_tfops.sh`*

## [DEPRECATED] Installation in a 30 series gpu (Eugenios way/Github: `env2`)

- From https://github.com/NVlabs/contact_graspnet/issues/19#issuecomment-1179489804

```bash
conda create --name contact_graspnet python=3.8
conda activate contact_graspnet
conda install -c conda-forge cudatoolkit=11.3
conda install -c conda-forge cudnn=8.2
pip install tensorflow==2.5 tensorflow-gpu==2.5 opencv-python-headless pyyaml==5.4.1 pyrender tqdm mayavi pyqt5

pip install scikit-image==0.19 torch torchvision
pip install -e ../uois
```
