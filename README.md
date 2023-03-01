# gopro-framegrab

 *Notes: developed to extract underwater gopro video survey for orthomosaic process for the sea cucumber project, but should be capable of general use (mp4 videos) as well*

## Quickstart
1. Clone repository to your desired local directory: `git clone https://github.com/joanlyq/gopro-video-framegrab.git`
2. Change directory to inside repo: `cd ./gopro-video-framegrab`
3. Open Terminal (MacOS or Linux) or Anaconda prompt (Windows) and create **conda[^1] environment** from yml file: `conda env create -f environment.yml`
4. Activate the conda environment: `conda activate framegrab`
5. Run `python main.py <path to the video or folders>`

[^1]: If you prefer using other virtual environment or need help to install conda environment, please refer to the following sections

### Requirements
You can also install the required libraries to your preferred environment (the version may vary)
- python=3.9.16
- opencv=4.6.0
- tqdm=4.64.1
- gst-plugins-base=1.18.5
- gst-plugins-good=1.18.5
- gstreamer=1.18.5

### Need help to install conda (Anaconda/Miniconda)
Conda is an open-source package and environment management system that runs on Windows, macOS, and Linux. Please refer to the [Anaconda official website](https://docs.anaconda.com/anaconda/install/) to install conda on your machine. 

[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is preferred as it takes less space on your machine and install less dependent files. However, both Anaconda and Miniconda will work with this repo.