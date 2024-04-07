import torch
from torch import nn
from torch.nn import TransformerEncoder, TransformerEncoderLayer

class GeneratorWithMultiInput(nn.Module):
    def __init__(self):
        super(GeneratorWithMultiInput, self).__init__()
        # 图像特征提取
        self.image_feature_extractor = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            # 可能还有更多层...
        )
        
        # 力场和结构信息处理
        self.non_image_processor = nn.Sequential(
            nn.Linear(in_features=force_field_dim + structure_info_dim, out_channels=128),
            nn.ReLU(),
            # 可能还有更多层...
        )
        
        # 特征融合后的处理
        self.combined_feature_processor = nn.Sequential(
            # 设计一些层来处理融合后的特征...
        )

    def forward(self, image_input, force_field, structure_info):
        image_features = self.image_feature_extractor(image_input)
        non_image_input = torch.cat([force_field, structure_info], dim=1)
        non_image_features = self.non_image_processor(non_image_input)
        
        # 融合特征
        combined_features = torch.cat([image_features, non_image_features], dim=1)
        
        # 处理融合后的特征
        output = self.combined_feature_processor(combined_features)
        return output
