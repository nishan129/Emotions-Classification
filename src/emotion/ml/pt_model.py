import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel
from sklearn.model_selection import train_test_split
import random


train_dataloader = DataLoader( batch_size=32, shuffle=True)
val_dataloader = DataLoader(batch_size=32)

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
    
    
    
    
num_classes =6  
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device_ids = [0, 1]  



model = EmotionClassifierWithConv(model, num_classes)
model = nn.DataParallel(model, device_ids=device_ids)
model = model.to(device)



optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
criterion = nn.CrossEntropyLoss()


num_epochs = 3

for epoch in range(num_epochs):
    model.train()
    total_loss = 0.0
    total_correct = 0
    
    
    for batch in train_dataloader:
        input_ids, attention_mask, label = batch
        
        input_ids, attention_mask, label = input_ids.to(device), attention_mask.to(device), label.to(device)
        
        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask)
        
        labels = label.to(device).long()
        outputs = outputs.float()
        
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        
        total_loss += loss.item()
        _, predicted = torch.max(outputs,1)
        total_correct += (predicted == labels).sum().item()
        
    train_loss = total_loss/ len(train_dataloader)
    train_accuracy = total_correct / len(train_dataloader)
    
    #validation step
    model.eval()
    total_val_loss = 0.0
    total_val_correct = 0
    val_predicted = []
    val_labels = []
    
    
    with torch.no_grad():
        for batch in val_dataloader:
            input_ids, attention_mask, labels = batch
            
            input_ids, attention_mask, labels = input_ids.to(device), attention_mask.to(device), labels.to(device)
            
            outputs = model(input_ids, attention_mask)
            labels = labels.to(device).long()
            
            outputs = outputs.float()
            
            loss = criterion(outputs, labels)
            
            total_val_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total_val_correct += (predicted == labels).sum().item()
            val_predicted.extend(predicted.cpu().numpy())
            val_labels.extend(labels.cpu().numpy())