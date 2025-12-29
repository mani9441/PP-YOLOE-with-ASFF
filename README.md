# **PP-YOLOE + ASFF (Work in Progress)**

This repository contains **lightweight modifications** to the MMYOLO implementation of **PP-YOLOE**, adding **Adaptive Spatial Feature Fusion (ASFF)** to the neck and an **SE-augmented backbone** to improve multi-scale representation, especially under partial occlusion and small-object scenarios.

⚠️ **NOTE:**  
This project is **under active research and development**.  
The design, experiments, and results are **preliminary** and may change before any official publication.

***

## 📌 **Abstract (Short Summary)**

Single-stage detectors like PP-YOLOE may lose important details when fusing features across scales using fixed, hand-crafted fusion strategies.
This project integrates **Adaptive Spatial Feature Fusion (ASFF)** into the PP-YOLOE neck and introduces a **stage-1 SE module** in the backbone to adaptively emphasize informative regions across scales.
On custom datasets with occlusion and fine-grained categories (e.g., seal tags), the modified model aims for **more consistent multi-scale features and improved localization stability**, while keeping inference efficiency close to the original PP-YOLOE.

***

## 🧩 **Purpose of This Repository**

This is a **patch-style repo**, containing only the **modified files and newly added modules**, not the full MMYOLO project.
It is designed to overlay seamlessly onto an existing MMYOLO installation.

This repository includes:

- Modified **PP-YOLOE neck** (`PPYOLOECSPPAFPN`) with a new `fusion_mode` supporting **ASFF** (and an experimental MFWF variant).  
- Modified **backbone** with a **stage-1 SE block** (`PPYOLOECSPResNetSEStage1`).  
- A **custom config** for a 3-class dataset (`Seal`, `Tag_White`, `Tag_Yellow`).  
- Utility module implementing **ASFF** and **MFWF** fusion blocks for PP-YOLOE necks.  

***

## 📁 **Repository Structure**

```text
PP-YOLOE-with-ASFF/
│
├── mmyolo/
│   ├── models/
│   │   ├── backbones/
│   │   │   └── ppyoloe_cspresnet_se_stage1.py
│   │   ├── necks/
│   │   │   ├── base_yolo_neck.py
│   │   │   ├── ppyoloe_csppan.py
│   │   │   └── ppyolo_neck_adaptive_fusion.py
│   │   └── ...
│   └── ...
│
├── configs/
│   └── ppyoloe/
│       └── ppyoloe_m_custom_seal.py
│
└── README.md
```

> Only altered modules and new implementations are included.  
> Overlay/merge these paths into the original **MMYOLO** source tree.

***

## ⚙️ **Installation & Usage**

### 1. Clone the original MMYOLO repository

```bash
git clone https://github.com/open-mmlab/mmyolo
cd mmyolo
```

Set up MMYOLO and its dependencies following the official instructions (MMCV, MMDetection, etc.).

### 2. Clone this patch repository

```bash
git clone https://github.com/mani9441/PP-YOLOE-with-ASFF
```

### 3. Apply the modifications

From inside the **MMYOLO root**:

```bash
cp -r ../PPYOLOE-with-ASFF/mmyolo/* mmyolo/
cp -r ../PPYOLOE-with-ASFF/configs/* configs/
```

Adjust the relative paths above depending on where you place this repo.

### 4. Train the model

```bash
python tools/train.py configs/ppyoloe/ppyoloe_m_custom_seal.py
```

In the config:

- `fusion_mode='asff'` enables adaptive spatial feature fusion in `PPYOLOECSPPAFPN`.  
- `class_name = ('Seal', 'Tag_White', 'Tag_Yellow')` defines the 3-class setup for the custom dataset.  

### 5. Evaluate

```bash
python tools/test.py configs/ppyoloe/ppyoloe_m_custom_seal.py \
                     work_dirs/ppyoloe_m_custom_seal/epoch_*.pth
```

Update the path to the checkpoint according to your training output.

---

## 📊 **Current Status (Work in Progress)**

| Component                           | Status         |
| ----------------------------------- | -------------  |
| ASFF module implementation          | ✔ Completed    |
| MFWF (channel-weighted fusion)      | ✔ Prototype    |
| Integration into PP-YOLOE neck      | ✔ Completed    |
| SE-augmented PP-YOLOE backbone      | ✔ Completed    |
| Custom Seal/Tag config              | ✔ Completed    |
| Full-scale training & tuning        | ⏳ In progress |
| Ablation vs. vanilla PP-YOLOE       | ⏳ Planned     |
| Paper draft / combined ASFF + PIoU  | ⏳ Exploring   |

> Early experiments suggest **more stable multi-scale features** and better behavior on partially occluded or small targets, but **final benchmarks are still pending**.  

***

## 🔬 **Research Goal**

This project is part of an ongoing effort on:

- **Adaptive multi-scale fusion** (ASFF, MFWF) for single-stage detectors.
- **Attention-enhanced backbones** for shallow feature refinement (SE at stage 1).  
- Robust detection under **occlusion, truncation, and fine-grained classes** (e.g., tags on seals).  
- Exploring combinations with **PIoU-style losses** for a fully occlusion-aware PP-YOLOE variant.

When the approach, experiments, and code stabilize, it may be consolidated into a unified **ASFF + PIoU + SE** framework and prepared for formal publication.

***

## 📝 **Citation (Temporary Placeholder)**

Until a formal paper is available, you may reference this work informally as:

```text
Work in progress — “PP-YOLOE with adaptive spatial feature fusion (ASFF) and SE-augmented backbone for occlusion-aware detection”.
Formal citation will be added upon publication.
```

***

## 🧑‍💻 Author

**Manikanta Kalyanam**

- **Role:** Project Maintainer & Sole Developer  
- **GitHub:** [@mani9441](https://github.com/mani9441)  
- **Contact:** (e.g., LinkedIn or email – add your preferred channel)  

> If you use this project or its methodology in research, please consider mentioning or crediting **Manikanta Kalyanam** appropriately.  

***

## 🤝 **Contributions & Feedback**

Feedback, discussions, and contributions are welcome.  
Suggestions that help improve the **neck fusion design**, **backbone attention**, **experiments**, or **integration with other PP-YOLOE variants** are especially appreciated.
