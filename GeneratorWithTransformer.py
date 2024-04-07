def serialize_inputs(force_field_data, structure_info_data):
    # 假设 force_field_data 和 structure_info_data 已经是预处理后的张量
    
    # 数值标准化 (这里只是示例，实际应用中需要根据数据的具体范围进行标准化)
    force_field_data_normalized = (force_field_data - force_field_data.min()) / (force_field_data.max() - force_field_data.min())
    
    # 独热编码结构信息 (示例，实际应用中可能需要根据具体的类别数据进行独热编码)
    structure_info_encoded = torch.nn.functional.one_hot(structure_info_data.to(torch.int64), num_classes=10)  # 假设有10个类别
    
    # 融合序列
    combined_sequence = torch.cat([force_field_data_normalized, structure_info_encoded.float()], dim=-1)
    
class GeneratorWithTransformer(nn.Module):
    def __init__(self, force_field_dim, structure_info_dim, image_channels=3):
        super(GeneratorWithTransformer, self).__init__()
        # 图像特征提取
        self.image_feature_extractor = nn.Sequential(
            nn.Conv2d(in_channels=image_channels, out_channels=64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            # 可能还有更多层...
        )
        
        # Transformer结构用于处理力场和结构信息
        self.transformer_encoder_layer = TransformerEncoderLayer(d_model=force_field_dim + structure_info_dim, nhead=8)
        self.transformer_encoder = TransformerEncoder(self.transformer_encoder_layer, num_layers=6)
        
        # 特征融合和输出处理部分可能需要根据实际情况进行调整
        self.final_processor = nn.Sequential(
            # 根据融合特征设计更多处理层...
        )

    def forward(self, image_input, force_field, structure_info):
        image_features = self.image_feature_extractor(image_input)
        # 假设force_field和structure_info已经合并并准备好作为序列输入
        combined_sequence = torch.cat([force_field, structure_info], dim=-1)
        sequence_features = self.transformer_encoder(combined_sequence.unsqueeze(0))
        
        # 特征融合，这里简单地将它们连接起来，实际应用中可能需要更复杂的操作
        combined_features = torch.cat([image_features.flatten(start_dim=1), sequence_features.flatten(start_dim=1)], dim=1)
        
        output = self.final_processor(combined_features)
        return output
