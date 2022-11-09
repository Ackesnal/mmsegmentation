_base_ = './upernet_vit-b16_mln_512x512_80k_ade20k.py'

model = dict(
    # pretrained='pretrain/deit_small_patch16_224-cd65a155.pth',
    pretrained='pretrained/upernet_deit-s16_512x512_80k_ade20k_20210624_095228-afc93ec2.pth',
    backbone=dict(num_heads=6, embed_dims=384, drop_path_rate=0.1),
    decode_head=dict(num_classes=150, in_channels=[384, 384, 384, 384]),
    neck=None,
    auxiliary_head=dict(num_classes=150, in_channels=384))
