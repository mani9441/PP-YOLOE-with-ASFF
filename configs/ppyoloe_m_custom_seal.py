_base_ = './ppyoloe_plus_s_fast_8xb8-80e_coco.py'


# Dataset root
data_root = 'Dataset/' # replace with COCO formated dataset root dir path
class_name = ('Seal', 'Tag_White', 'Tag_Yellow') # replace with your own classes
num_classes = len(class_name)
metainfo = dict(classes=class_name)


# Model config
model = dict(
    bbox_head=dict(
        head_module=dict(num_classes=num_classes)
    ),
    neck=dict(
        type='PPYOLOECSPPAFPN',
        use_spp=False,
        fusion_mode='asff',  #  by @manikanta
    ),
    train_cfg=dict(
        initial_assigner=dict(num_classes=num_classes),
        assigner=dict(num_classes=num_classes)
    )
)


# 🔧 Dataloaders
train_dataloader = dict(
    batch_size=6,
    num_workers=4,
    dataset=dict(
        type='YOLOv5CocoDataset',
        data_root=data_root,
        metainfo=metainfo,
        ann_file='train/_annotations.coco.json',
        data_prefix=dict(img='train/'),

    )
)

val_dataloader = dict(
    batch_size=6,
    num_workers=4,
    dataset=dict(
        type='YOLOv5CocoDataset',
        data_root=data_root,
        metainfo=metainfo,
        ann_file='valid/_annotations.coco.json',
        data_prefix=dict(img='valid/')
    )
)


test_dataloader = dict(
    batch_size=6,
    num_workers=4,
    dataset=dict(
        type='YOLOv5CocoDataset',
        data_root=data_root,
        metainfo=metainfo,
        ann_file='test/_annotations.coco.json',   
        data_prefix=dict(img='test/')       
    )
)

# Evaluators

val_evaluator = dict(ann_file=data_root + 'valid/_annotations.coco.json')
test_evaluator = dict(ann_file=data_root + 'test/_annotations.coco.json')

# Training schedule
max_epochs = 100
train_cfg = dict(max_epochs=max_epochs, val_interval=10)

# Logger & checkpoints
default_hooks = dict(
    checkpoint=dict(interval=10, max_keep_ckpts=2, save_best='auto'),
    logger=dict(type='LoggerHook', interval=5),
    param_scheduler=dict(
        warmup_min_iter=10,
        warmup_epochs=3,
        total_epochs=int(max_epochs * 1.2)
    )
)

# Load pretrained weights (still use PP-YOLOE-S pretrained)
load_from = 'https://download.openmmlab.com/mmyolo/v0/ppyoloe/ppyoloe_plus_s_fast_8xb8-80e_coco/ppyoloe_plus_s_fast_8xb8-80e_coco_20230101_154052-9fee7619.pth'

visualizer = dict(
    vis_backends=[dict(type='LocalVisBackend')]
)

optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=5e-4)
)
