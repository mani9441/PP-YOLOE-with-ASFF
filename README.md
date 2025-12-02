# **PP-YOLOE + PIoU Loss (Work in Progress)**

This repository contains **lightweight modifications** to the MMYOLO implementation of **PP-YOLOE**, introducing a new **Perceptual IoU (PIoU) loss** aimed at improving bounding box localization under partial occlusion and truncation.

⚠️ **NOTE:**
This project is **under active research and development**.
The method, experiments, and results are **preliminary** and may change as the work progresses or before an official publication.


## 📌 **Abstract (Short Summary)**

Object detectors often struggle under partial occlusion due to limitations in standard IoU-based losses.
This project introduces a **Perceptual IoU (PIoU)** loss—a corner-aware extension of IoU that enforces perceptual boundary consistency.
When integrated into PP-YOLOE, PIoU aims to improve localization stability for occluded targets.
Initial results on COCO and custom occlusion datasets show **promising improvements**, while maintaining inference efficiency.



## 🧩 **Purpose of This Repository**

This is a **patch-style repo**, containing only the **modified files and new modules**, instead of the full MMYOLO project.
It is designed to be lightweight and easy to integrate into any existing MMYOLO environment.

Contents include:

* Modified **backbone**, **neck**, and **head** components
* Newly added **PIoU loss module**
* Config files for training PP-YOLOE with PIoU
* Documentation for applying the patch


## 📁 **Repository Structure**

```
your-repo/
│
├── mmyolo/
│   ├── models/
│   │   ├── backbones/
│   │   ├── necks/
│   │   ├── heads/
│   │   └── losses/
│   │       └── piou_loss.py
│   └── ...
│
├── configs/
│   └── ppyoloe/
│       └── piou_ppyoloe_s.py
│
└── README.md
```

> Only altered modules and new implementations are included.
> Merge/overlay them with the original MMYOLO tree.



## ⚙️ **Installation & Usage**

### 1. Clone the original MMYOLO repository

```bash
git clone https://github.com/open-mmlab/mmyolo
cd mmyolo
```

### 2. Clone this patch repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>
```

### 3. Apply the modifications

```bash
cp -r <your-repo-name>/mmyolo/* mmyolo/
cp -r <your-repo-name>/configs/* configs/
```

### 4. Train the model

```bash
python tools/train.py configs/ppyoloe/piou_ppyoloe_s.py
```

### 5. Evaluate

```bash
python tools/test.py configs/ppyoloe/piou_ppyoloe_s.py \
                     work_dirs/piou_ppyoloe_s/epoch_*.pth
```



## 📊 **Current Status (Work in Progress)**

| Component                      | Status        |
| ------------------------------ | ------------- |
| PIoU loss implementation       | ✔ Completed   |
| Integration into PP-YOLOE head | ✔ Completed   |
| Backbone/neck adjustments      | ✔ Completed   |
| COCO training                  | ⏳ In progress |
| Ablation studies               | ⏳ Planned     |
| Paper draft                    | ⏳ Ongoing     |

> Preliminary results show **promising gains**, especially for occluded objects.
> Final benchmarks will be added after experimental completion.



## 🔬 **Research Goal**

This project is part of an ongoing research effort exploring:

* Corner-sensitive loss functions
* Perceptual consistency for bounding boxes
* Occlusion-aware object detection
* Extensions of PP-YOLOE for challenging real-world datasets

If the project matures, it may be prepared for submission to a conference or journal.



## 📝 **Citation (Temporary Placeholder)**

Until an official paper is published, please cite this work informally:

```
Work in progress — Formal citation will be added upon publication.
```

---

## 🤝 **Contributions & Feedback**

Feedback, discussions, and contributions are welcome.
Since this is an early-stage research project, suggestions that help improve architecture, experiments, and design are appreciated.


