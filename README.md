---

# 3D Captioning with Pretrained Models  

## Project Overview  
This project automates the generation of descriptive captions for 3D objects, leveraging pre-trained models and a multi-view rendering approach.  
- The system integrates **3D model rendering**, **image captioning**, and **caption fusion** to produce detailed and accurate textual descriptions of 3D assets.  
- Inspired by the methodology outlined in the research paper *[Scalable 3D Captioning with Pretrained Models](https://arxiv.org/pdf/2306.07279)*.  
- The pipeline emphasizes scalability, computational efficiency, and adaptability to future advancements.  

---

## Objectives  
- **Automated Caption Generation**: Generate captions for 3D objects using multi-view rendered images.  
- **Efficiency**: Employ computationally lightweight models to minimize resource demands.  
- **Caption Fusion**: Merge captions from multiple views into a single coherent description.  
- **Adaptability**: Ensure support for future upgrades to improved pre-trained models and rendering libraries.  

---

## Pipeline  

### 1. Data Preparation  
- Download 3D models from the Objaverse dataset.  
- Render 2D images from eight specific viewpoints using Blender.  

### 2. Image Captioning  
- Use the **Paligemma** model to generate captions for each rendered image.  

### 3. Caption Fusion  
- Consolidate captions from all viewpoints using the **Gemma 2** model.  

### 4. Post-Processing  
- Clean and format captions for readability and downstream integration.  

---

## Tools and Frameworks  
- **Python**: Core programming language for the pipeline.  
- **Blender**: Tool for rendering 3D models into 2D images.  
- **JAX**: Library for high-performance computations in captioning and fusion tasks.  
- **Objaverse Dataset**: Primary source of 3D models.  
- **Paligemma and Gemma 2 Models**: Pre-trained models used for image captioning and caption fusion.  
- **Jupyter Notebook**: Development environment for interactive implementation.  

---

## Usage  

### Step 1: Download 3D Objects  
- Use your own `.glb` files or run the `objaverse-download-simple-script` to fetch samples from the Objaverse dataset.  
- Add the paths of the downloaded objects to the `.pkl` file, such as `object_path_pkl`. Use the `edit_pkl_file` script to modify `.pkl` files as needed.  

### Step 2: Rendering  
- Render 2D images of the 3D models using Blender:  
  ```bash  
  path\to\blender -b -P ./scripts/blender_render_script.py -- --object_path_pkl ./scripts/assets/example_object_path_multiple_examples.pkl  
  ```  

### Step 3: Caption Generation and Fusion  
- Generate and fuse captions for rendered images by running:  
  ```bash  
  python ./scripts/image-captioning-captions-fusion-v2.py  
  ```  

---

## Citation  
If you find this project or code useful, please consider citing the following research works:  

```bibtex  
@article{luo2023scalable,  
      title={Scalable 3D Captioning with Pretrained Models},  
      author={Luo, Tiange and Rockwell, Chris and Lee, Honglak and Johnson, Justin},  
      journal={arXiv preprint arXiv:2306.07279},  
      year={2023}  
}  

@article{luo2024view,  
      title={View Selection for 3D Captioning via Diffusion Ranking},  
      author={Luo, Tiange and Johnson, Justin and Lee, Honglak},  
      journal={arXiv preprint arXiv:2404.07984},  
      year={2024}  
}  
```  

---
