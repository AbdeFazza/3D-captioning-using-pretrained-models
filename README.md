# Project Overview
- This project focuses on automating the generation of descriptive captions for 3D objects, leveraging pre-trained models and a multi-view rendering approach.
- The system integrates rendering, image captioning, and caption fusion to create accurate and detailed descriptions of 3D assets.
- Inspired by the Cap3D methodology, the pipeline emphasizes scalability, computational efficiency, and adaptability to future advancements.

# Objectives
- *Automated Caption Generation*: Generate captions for 3D objects using multi-view rendered images.
- *Efficiency*: Employ computationally lightweight models for scalability without extensive fine-tuning.
- *Caption Fusion*: Merge captions from multiple views into a single coherent description.
- *Adaptability*: Support future upgrades to improved pre-trained models and rendering libraries.

# Pipeline
- Data Preparation:
  - Download 3D models from the Objaverse dataset.
  - Render 2D images from eight specific viewpoints using Blender.
- Image Captioning:
  - Use the Paligemma model to generate captions for each rendered image.
- Caption Fusion:
  - Consolidate captions from all viewpoints using the Gemma 2 model.
- Post-Processing:
  - Clean and format captions for readability and downstream integration.

# Tools and Frameworks
- *Python*: Core programming language for the pipeline.
- *Blender*: Rendering tool for generating 2D views of 3D objects.
- *JAX*: Library for high-performance computations in captioning and fusion tasks.
- *Objaverse Dataset*: Source of 3D models for testing the pipeline.
- *Paligemma and Gemma 2 Models*: Pre-trained models for captioning and fusion.
- *Jupyter Notebook*: Development environment for pipeline implementation.

# Usage
1. Download 3D Objects:
   - Feel free to dowload your own objects -in .glb format- or run the _objaverse-download-simple-script_ file to download some samples from the _Objaverse_ dataset.
   - Then add the objects paths to the _object_path_pkl_ (.pkl) file.
   - Use the _edit_pkl_file_ file to edit .pkl files.
2. Rendering
   - Run the following script to render images from 3D models: <br>
   path\to\blender -b -P .\scripts\blender_render_script.py -- --object_path_pkl .\scripts\assets\example_object_path_multiple_examples.pkl
2. Caption Generation and Fusion
   - Generate and fuse captions for the rendered images by running the _image-captioning-captions-fusion-v2_ file.
