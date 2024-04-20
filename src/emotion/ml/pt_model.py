import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel
from sklearn.model_selection import train_test_split
import random


class EmotionClassifierWithConv(nn.Module):
    def __init__(self, transformer_model, num_classes, kernel_size=3, num_filters=256):
        super(EmotionClassifierWithConv, self).__init__()
        self.transformer = transformer_model
        self.conv = nn.Conv1d(in_channels=768, out_channels=num_filters, kernel_size=kernel_size, padding=1)  # Adjust padding
        self.fc = nn.Linear(num_filters, num_classes)
    
    def forward(self, input_ids, attention_mask):
        output = self.transformer(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = output.pooler_output
        pooled_output = pooled_output.unsqueeze(2)
        
        conv_out = F.relu(self.conv(pooled_output))
        pooled_conv_out, _ = torch.max(conv_out, dim=2)  
        logits = self.fc(pooled_conv_out)
        return logits
